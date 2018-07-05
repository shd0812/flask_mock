from  Common.common_OpFile import operate_File
from  Common.common_Logger import myLog
import re
from  tmp_test.test1 import client
from tmp_test import factory_func





logger = myLog.getLog()



# 通过字符串获取最终vaule
def get_value_fromdic(p_dic,p_str):
    if isinstance(p_dic,dict):
        if isinstance(p_str,str):
            try:
                if '.' in p_str:
                    str_list = p_str.split('.')
                    tmp = p_dic
                    for x in range(len(str_list)):
                        result_data = str_list[x]
                        if isinstance(tmp, dict):
                            tmp = tmp.get(result_data,'不存在的key')
                        elif isinstance(tmp, list):
                            tmp = tmp[int(result_data)]
                    result_value = tmp
                    return result_value
                else:
                    return p_dic.get(p_str)
            except Exception as e:
                logger.error('出错了，{}'.format(e))




class load_Case(object):
    def __init__(self,path):
        op = operate_File(path)
        self.file_context = op.read_file()
        print(self.file_context)
        self.parm_list=[]
        self.extrac_dic={}

    def init_Parm(self):
        if isinstance(self.file_context,list):
            for item in self.file_context:
                if isinstance(item,dict):
                    request_data=get_value_fromdic(item,'test.request')
                    self.parm_list.append(request_data)
                else:
                    logger.error('出错了，item不是字典，item{}'.format(item))

            return self.parm_list
        else:
            logger.error('出错了，self.file_context不是数组，self.file_context{}'.format(self.file_context))




if __name__ == '__main__':
    case = load_Case('../data/test_one/test_one.yaml')
   # response={"status_code": 200, "msg": "success", "user_id": 26}


    parm_list=case.init_Parm()
    for item in parm_list:
        url = item.get('url')
        data=item.get('data')
        resopnse = client(url,data=data)
        extract = item.get('extract')
        if not extract :
            pass
        else:
            op = operate_File(extract)
            op.write_file()


        print(resopnse)



