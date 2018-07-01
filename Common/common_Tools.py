import operator
import hashlib


#md5加密
def md5_str(str):
    b_str=bytes(str,encoding='utf-8')
    return hashlib.md5(b_str).hexdigest()



#字典排序
def dic_reverse(parm_dic,reverse_type=0):
    #result_dic={}
    if isinstance(parm_dic,dict):
        if reverse_type ==0: #正序
            result_dic=sorted(parm_dic.items(), key=operator.itemgetter(0),reverse=False)
        elif reverse_type==1: #倒序
            result_dic = sorted(parm_dic.items(), key=operator.itemgetter(0), reverse=True)
        else:
            result_dic='输入的排序类型不正确，请选择0或1'
    else:
        result_dic = '请输入字典'
    return result_dic

#列表排序
def list_reverse(parm_li,reverse_type=0):
    if isinstance(parm_li,list):
        if reverse_type ==0: #正序
            result_li=sorted(parm_li,reverse=False)
        elif reverse_type==1: #倒序
            result_li = sorted(parm_li, reverse=True)
        else:
            result_li='输入的排序类型不正确，请选择0或1'
    else:
        result_li = '请输入列表'
    return result_li

if __name__ =='__main__':
    print(md5_str('kkk'))



