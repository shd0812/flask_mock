from XennHo.Basc_Http import  Base_Requests
from  XennHo.utils import get_Param,input_parm
from XennHo.utils import open_Yaml
from CFRunner import response
from CFRunner.testcase import TestcaseParser,TestcaseLoader

def xx_post(url,**kwargs):
    method = 'POST'
    host = 'https://mi.shaxiaoseng.com:4433/Xeenho/'
    client = Base_Requests(method, host, url)

    result=client.sxs_Api(data=kwargs)
    return result

def register_query(url,path):
    dic = get_Param(path)
    #print('参数%s' % dic)
    result=xx_post(url,data=dic)
    return result

def send_post(parm_url,str):
    print(str)
    dic = input_parm(str)
    if dic =='输入参数不合法':
        return dic
    else:
        result=xx_post(parm_url,data=dic)
        return result

def tmp_func(var_dic):
    for var_k, var_v in var_dic.items():
        result = var_k + '=' + var_v+'_m'
        return result

if __name__=='__main__':
    #path='C:/Users/shd/Desktop/测试文档/星火投资/星火脚本/用例/新用户注册.yaml'
    #data=register_query('register',path)  query_userbidrepayinfo  query_useraccount


    test_list = TestcaseLoader('../data/test_one/xeenho.yaml').request_parm()
    test_ex = TestcaseLoader('../data/test_one/xeenho.yaml').extract_parm()
   # print(test_list)

    for x in range(len(test_list)):
        url = test_list[x].get('url')
        parm_data=tmp_func(test_list[x].get('data'))
       # print(parm_data)
        if '$' in parm_data:
            raise Exception
        else:
            data = send_post(url, parm_data)
            resp_obj = response.ResponseObject(data)
            extract_binds_dict = resp_obj.extract_response(test_ex)
            print(extract_binds_dict)
            if '$' in str(test_list[x+1]):
                testcase_parser = TestcaseParser(variables=extract_binds_dict)
                test_list[x + 1]=testcase_parser.eval_content_with_bindings(test_list[x+1])

                print(test_list[x+1],test_list)

            print(data.text)


    parm_str = 'platform_uid=3000000419294000_m'
   # data=send_post('query_useraccount',parm_str)
    #resp_obj = response.ResponseObject(data)
    #print(resp_obj.extract_field('content.records.0.platform_uid'))
    #extract_binds_list = [
     #   {"platform_uid": "content.records.0.platform_uid"}]
    #extract_binds_dict = resp_obj.extract_response(extract_binds_list)
    #print(extract_binds_dict)

    parm_dic = {

            "test": {
                "name": "api_login",
                "request": {
                    "url": "register",
                    "data": {
                        'platform_uid':'$platform_uid'
                    }
                }

            }

    }
   # print(parm_dic)
    #testcase_parser = TestcaseParser(extract_binds_dict)
    #result = testcase_parser.eval_content_with_bindings(parm_dic)
    #print(result)
    #print(data.text)

