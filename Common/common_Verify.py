from Common.common_OpFile import operate_File
from Common.common_Logger import *
logger = myLog.getLog()
import operator

def eq_verify(check_data,path):
    if not path:
        path='../TestData/gm/valid.yaml'
    op =operate_File(path)
    d=op.read_file()
    expect_list=d.get('expect')
    #print(expect_list)
    for item in expect_list:
        logger.debug('期待的hahahahahhaha{}'.format(item))
        key,=item

        temp_li=key.split('.')
        logger.debug('期待的keykeykeykey----{}'.format(temp_li))
        logger.debug('传输过来的----{}'.format(check_data))
        tmp= check_data
        for x in range(len(temp_li)):
            result_data = temp_li[x]
            if isinstance(tmp,dict):

                tmp=tmp.get(result_data)

            elif isinstance(tmp,list):
                tmp=tmp[int(result_data)]

        check_str=tmp
        expect_str = item.get(key)
        logger.info('要检查的字符{},期待的字符{}'.format(check_str,expect_str))

        if check_str == expect_str:
            pass
        else:
            raise Exception('不相等，要检查的是{},期望的是{}'.format(check_str,expect_str))

def isExit_Key(expect_list,dic):
    tmp_list=[]
    flag=1
    print(dic)
    while flag==1:
        tmp_dic=dic
        for k, v in tmp_dic.items():
            if isinstance(v,dict):
                tmp_dic =v
                flag =1
            else:
                tmp_list+=k
    print(tmp_list)

if __name__ == '__main__':
    tmp_dic = {
        'name':'shen',
        'sex': 5,
        'province':'henan',
        'vls': [1,2,3],
        'index':{
            'p':'t'
        }
    }

    p_dic = {
        'name':'shen',
        'sex': 5,
        'province':'henan',
        'vls': [1,2,3],
        'index':{
            'p':'t'
        }
    }

    isExit_Key([1],p_dic)