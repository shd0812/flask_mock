from Common.common_OpDB import hh_DB
from Common import logger
hh = hh_DB('mock_db','../data/config.ini')

def insert_user(u_id,s_name,mobile,province):
    insert_sql = "INSERT INTO `mock_db`.`mock_user` (`id`, `name`, `mobile`, `province`) VALUES ( '%s','%s','%s','%s' )" % (u_id,s_name,mobile,province)
    print(insert_sql)
    data=hh.get_data(insert_sql)
    return data
#
def select_user(uid):
    sele_sql = "SELECT * FROM mock_user WHERE id = %s" % uid
    logger.setup_logger("DEBUG")
    logger.log_debug('正在执行查询sql%s' % sele_sql)
    data = hh.get_data(sele_sql)

    return data

if __name__ == '__main__':
    select_user(2)
    #insert_user(25,'孟燕京','18513071628','河南')