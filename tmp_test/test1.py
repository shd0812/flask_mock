import json
from Common.common_Logger import myLog

logger = myLog.getLog()

def client(url,**kwargs):
    #logger.debug('参数为{}'.format(kwargs))
    reponse = {}
    if url == '127.0.0.1/api/register/':
        if kwargs['data']['account']=='13521137793':
            reponse = {
                'status_code':200,
                'msg':'success',
                'user_id':26
                    }
        else:
            reponse={
                'status_code':400
            }
    else:
        if url == '127.0.0.1/api/login/':
            logger.debug('参数为{}'.format(kwargs['data']['user_id']))
            if kwargs['data']['user_id'] == '26' :
                reponse = {
                    'status_code': 200,
                    'msg': 'success'
            }
        else:
            reponse={
                'status_code':400
            }
    return json.dumps(reponse)



#op = operate_File('../data/test_one/test_one.yaml')
if __name__ =='__main__':
    url = '127.0.0.1/api/register/'
    parm_str1={
        'account':'13521137793',
        'password' :'123456'
    }
    result=client(url,data=parm_str1)
    print(result)
