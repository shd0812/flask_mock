import os
from yaml import  load
from configparser import ConfigParser
# 操作文件类
class operate_File():

    def __init__(self,file_name):
        self.file_name=file_name
    #获取路径
    def get_path(self):
        path=os.path.dirname( __file__)
        parent_path=os.path.dirname(path)
        grand_path=os.path.join(parent_path,self.file_name)

        if '\..' in grand_path:
            final_path=grand_path.replace('\../','/')
        return final_path
    #读取文件
    def read_file(self):
        path=self.get_path()

        if  'yaml'in self.file_name:
            print(path)
            with open(path, 'rb') as pf:
                data=load(pf)
            return data
        elif 'ini' in self.file_name:
            config=ConfigParser()
            config.read(path)
            return config


if __name__=='__main__':
    op =operate_File('../data/ssinvest.yaml')
    print(op.read_file())

