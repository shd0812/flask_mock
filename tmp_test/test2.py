from  tmp_test.test1 import client
from  Common.common_OpFile import operate_File
import json
#op = operate_File('../data/test_one/test_one.yaml')
#file_data = op.read_file()

class load_Case(object):
    def __init__(self,path):
        self.path = path
    def get_caseData(self):
        op = operate_File(self.path)
        file_data = op.read_file()
        return file_data
    def get_parm(self):
        parm_data = []
        file_data = self.get_caseData()
        for item in file_data:
            print(item)
            if isinstance(item,dict):
                request_data=item.get('test').get('request')
                parm_data.append(request_data)
            else:
                print('error')
        return parm_data


if __name__ == '__main__':
    case = load_Case('../data/test_one/test_one.yaml')
    parm_list = case.get_parm()
    for item in parm_list:
        resopnse = client(item.get('url'),data=item.get('data'))
        print(resopnse)
