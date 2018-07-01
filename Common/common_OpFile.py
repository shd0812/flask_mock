import os
from yaml import  load
from configparser import ConfigParser
import json
import platform
from Common.common_Logger import  *
logger = myLog.getLog()
# 操作文件类
class operate_File():

    def __init__(self,file_name):
        if not file_name:
            logger.error('文件名不能为空,文件名为{}'.format(file_name))
        else:
            self.file_name=file_name
    #获取路径
    def get_path(self):
        path=os.path.dirname( __file__)
        parent_path=os.path.dirname(path)
        grand_path=os.path.join(parent_path,self.file_name)
        if platform.system() == 'Windows':
            logger.debug('系统为windows')
            if '\..' in grand_path:
                final_path=grand_path.replace('\../','/')
                return final_path
        elif platform.system() == 'Linux':
            if '/../' in grand_path:
                final_path = grand_path.replace('/../','/')

                logger.debug('linux上地址为{}'.format(grand_path))
                return final_path
        else:
            logger.error('暂未考虑其他平台的处理')
    #读取文件
    def read_file(self):
        path=self.get_path()
        logger.debug('路径为{}'.format(path))
        if  'yaml'in self.file_name:
            try:
                with open(path, 'rb') as pf:
                    data=load(pf)
                return data
            except Exception as e:
                logger.error('读取出错了，{}'.format(e))
                return  e
        elif 'ini' in self.file_name:
            config=ConfigParser()
            try:
                config.read(path)
                return config
            except Exception as e:
                logger.error('读取出错了，{}'.format(e))
                return  e
    def write_file(self,text):
        with open(self.get_path(),'w') as pf:
            pf.write(text)


if __name__=='__main__':
    #op =operate_File('../TestData/gm/valid.yaml')
    #d=op.read_file()

    check_data={
            'test_name':'用户信息查询',
            'parm':{
                'service':'bind_url',
                'body':[{
                    'index':{
                        'name':'shen',
                        'vals':[111111,222222]
                    }
                    }]
                }

            }


    op = operate_File('../data/test_one/extract')
    op.write_file(json.dumps(check_data))



