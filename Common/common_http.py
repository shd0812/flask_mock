import requests
from Common.common_Logger import *
import json

logger = myLog.getLog()



class Base_Requests(object):
    def __init__(self, method, host, params_url):
        self.host = host
        self.method = method
        self.params_url = params_url
        self.client = requests.Session()

    def sxs_Api(self, special=0,**kwargs):
        if self.params_url =='':
            url=self.host
        else:
            url = self.host + self.params_url
        logger.debug('请求地址为：%s' %url)

        #print(kwargs)
        if self.method == 'POST':
            if special ==1:
                kwargs = kwargs['data']
            elif special ==0:
                kwargs = kwargs['data']['data']
            logger.debug('请求数据为：%s' % kwargs)

            r = self.client.post(url, data=kwargs)

            r.encoding = 'UTF-8'
            if r.status_code == 200:
                try:
                    result = r.text
                    logger.debug('返回结果为：%s' % result)
                    return result
                except:
                    return r.text
            else:
                logger.debug('返回失败结果为：%s' % r.status_code)
        elif self.method == 'GET':
            r = self.client.get(url, params=kwargs)
            r.encoding = 'UTF-8'
            if r.status_code == 200:
                result = json.loads(r.text)
                logger.debug('请求结果为：%s' % result)
                return result