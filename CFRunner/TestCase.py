import re
from CFRunner import  exception
from CFRunner.compat import basestring
import os,time,random
from  Common.common_OpFile import operate_File


variable_regexp = r"\$([\w_]+)"

def extract_variables(content):
    """ extract all variable names from content, which is in format $variable
    @param (str) content
    @return (list) variable name list

    e.g. $variable => ["variable"]
         /blog/$postid => ["postid"]
         /$var1/$var2 => ["var1", "var2"]
         abc => []
    """
    try:
        return re.findall(variable_regexp, content)
    except TypeError:
        return []


class TestcaseLoader(object):
    def __init__(self,path):
        self.path = path
        self.file_mapping = self.__load_file__()

    def __load_file__(self):
        print('我被调用了')

        oper = operate_File(self.path)
        file_list = oper.read_file()
        test_list= []
        if not isinstance(file_list,list):
            raise exception.FileFormatError("API format error: {}".format(self.path))
        for list_item in file_list:
            if not isinstance(list_item, dict) or len(list_item) != 1:
                raise exception.FileFormatError("API format error: {}".format(self.path))
            else:
                test_list.append(list_item.get('test'))


        return test_list

    def request_parm(self):


        request_mapping = []
        for item in self.file_mapping:
            #print(item.get('test'))
            request_dic = item.get('request')

            if not isinstance(request_dic,dict):
                raise exception.FileFormatError("API format error: {}".format(self.path))
            request_mapping.append(request_dic)

        return  request_mapping

    def extract_parm(self):
        extract_mapping = []
        for item in self.file_mapping:

            extract_dic = item.get('extract')
            if isinstance(extract_dic,dict):
                extract_mapping.append(extract_dic)

        return  extract_mapping







class TestcaseParser(object):

    def __init__(self, variables={}):
        self.update_binded_variables(variables)



    def update_binded_variables(self, variables):
        """ bind variables to current testcase parser
        @param (dict) variables, variables binds mapping
            {
                "authorization": "a83de0ff8d2e896dbd8efb81ba14e17d",
                "random": "A2dEx",
                "data": {"name": "user", "password": "123456"},
                "uuid": 1000
            }
        """
        self.variables = variables


    def _get_bind_item(self, item_type, item_name):
        if item_type == "variable":
            if item_name in self.variables:
                return self.variables[item_name]
        else:
            raise exception.ParamsError("bind item should only be function or variable.")





    def get_bind_variable(self, variable_name):
        return self._get_bind_item("variable", variable_name)





    def _eval_content_variables(self, content):
        """ replace all variables of string content with mapping value.
        @param (str) content
        @return (str) parsed content

        e.g.
            variable_mapping = {
                "var_1": "abc",
                "var_2": "def"
            }
            $var_1 => "abc"
            $var_1#XYZ => "abc#XYZ"
            /$var_1/$var_2/var3 => "/abc/def/var3"
            ${func($var_1, $var_2, xyz)} => "${func(abc, def, xyz)}"
        """
        variables_list = extract_variables(content)
        for variable_name in variables_list:
            variable_value = self.get_bind_variable(variable_name)

            if "${}".format(variable_name) == content:
                # content is a variable
                content = variable_value
            else:
                # content contains one or several variables
                content = content.replace(
                    "${}".format(variable_name),
                    str(variable_value), 1
                )

        return content

    def eval_content_with_bindings(self, content):
        """ parse content recursively, each variable and function in content will be evaluated.

        @param (dict) content in any data structure
            {
                "url": "http://127.0.0.1:5000/api/users/$uid/${add_two_nums(1, 1)}",
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json",
                    "authorization": "$authorization",
                    "random": "$random",
                    "sum": "${add_two_nums(1, 2)}"
                },
                "body": "$data"
            }
        @return (dict) parsed content with evaluated bind values
            {
                "url": "http://127.0.0.1:5000/api/users/1000/2",
                "method": "POST",
                "headers": {
                    "Content-Type": "application/json",
                    "authorization": "a83de0ff8d2e896dbd8efb81ba14e17d",
                    "random": "A2dEx",
                    "sum": 3
                },
                "body": {"name": "user", "password": "123456"}
            }
        """
        if content is None:
            return None

        if isinstance(content, (list, tuple)):
            return [
                self.eval_content_with_bindings(item)
                for item in content
            ]

        if isinstance(content, dict):
            evaluated_data = {}
            for key, value in content.items():
                eval_key = self.eval_content_with_bindings(key)
                eval_value = self.eval_content_with_bindings(value)
                evaluated_data[eval_key] = eval_value

            return evaluated_data

        if isinstance(content, basestring):

            # content is in string format here
            content = content.strip()

            # replace functions with evaluated value
            # Notice: _eval_content_functions must be called before _eval_content_variables


            # replace variables with binding value
            content = self._eval_content_variables(content)

        return content



if __name__ =='__main__':
    variables = {
        "uid": "1000",
        "random": "A2dEx",
        "authorization": "a83de0ff8d2e896dbd8efb81ba14e17d",
        "data": {"name": "user", "password": "123456"},
        "token": 'sssssss'
    }

    #testcase_parser=TestcaseParser(variables)
    testcase_template = {
        "url": "http://127.0.0.1:5000/api/users/$uid/",
        "method": "POST",
        "headers": {
            "Content-Type": "application/json",
            "authorization": "$authorization",
            "random": "$random",

        },
        "body": "$data",
        "index":{
            "name":{
                "token": "$token"
            }
        }
    }

    #result = testcase_parser.eval_content_with_bindings(testcase_template)
    #print(result)

    load =TestcaseLoader('../data/test_one/xeenho.yaml')
    print(load.request_parm()[0]['data'])
    for var_k,var_v in load.request_parm()[0]['data'].items():
        result = var_k+'='+var_v
        print(result)
    load.extract_parm()