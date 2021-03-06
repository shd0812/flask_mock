import pymysql
from Common.common_OpFile import operate_File
from Common.common_Logger import *

logger = myLog.getLog()

class hh_DB():

    # print(host,type(port),user,passwd)
    def __init__(self, db_name,file_name):
        operate_file = operate_File(file_name)
        data = operate_file.read_file()
        host = data['mysql_config']['host']
        port = int(data['mysql_config']['port'])
        user = data['mysql_config']['account']
        passwd = data['mysql_config']['passwd']
        print(host)
        try:
            self.db = pymysql.connect(host=host, port=port \
                                      , user=user, passwd=passwd \
                                      , db=db_name, use_unicode=True, charset='utf8')
        except Exception as e:
            print(port)
            logger.error('mysql 连接失败,端口号为{},错误信息为{}'.format(port,e))

        else:
            self.cursor = self.db.cursor(cursor=pymysql.cursors.DictCursor)  # 转化为字典

    def get_data(self, sql, *k):
        try:
            self.cursor.execute(sql, k)
        except Exception as e:
            print('sql执行失败')
            print(sql)
            logger.error('sql执行失败，sql为：{},错误信息为:{}'.format(sql,e))
            return 'sql_error', e
        else:
            self.db.commit()
            print(type(self.cursor.fetchall()))
            if self.cursor.fetchall():
                return self.cursor.fetchall()
            else:
                return ''

if __name__=='__main__':
    db=hh_DB('sxs_vault','../config.ini')
