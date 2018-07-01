import time
import datetime


class hh_Time():
    #获取当前时间戳
    def getTimestamp(self):
        time_now = int(time.time())
        #转换成当地时间
        time_local = time.localtime(time_now)
        #转换新的时间格式
        dt= time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)
        return  int(timestamp)

    # 时间转时间戳
    def time_tran(self, s_time):
        # 转换成时间数组
        timeArray = time.strptime(s_time, "%Y-%m-%d %H:%M:%S")
        # 转换成时间戳
        timestamp = time.mktime(timeArray)
        return int(timestamp)

        # 时间戳转换成时间
    def tamp_tran(self, s_tamp):
            # 转换成localtime
        time_local = time.localtime(s_tamp)
            # 转换成新的时间格式(2016-05-05 20:28:54)
        dt = time.strftime("%Y-%m-%d %H:%M:%S", time_local)
        return dt

    def getNow(self):
        nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')#现在
        return nowTime


if __name__=='__main__':
    hh=hh_Time()
    print(hh.getTimestamp())
    print(vars(hh_Time))