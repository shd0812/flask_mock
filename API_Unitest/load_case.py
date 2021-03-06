from API_Unitest.utils import operate_File
from API_Unitest import exception


class TestLoad():

    @staticmethod
    def load_file(path):

        oper = operate_File(path)
        file_data=oper.read_file()
        config_dic = {}
        test_list= []
        if not isinstance(file_data,list):
            raise exception.FileFormatError("API format error: {}".format(path))
        for list_item in file_data:
            if not isinstance(list_item, dict) or len(list_item) != 1:
                raise exception.FileFormatError("API format error: {}".format(path))
            else:
                if list_item.get('config'):
                    config_dic = list_item.get('config')
                else:

                    test_list.append(list_item.get('test'))
        return config_dic,test_list