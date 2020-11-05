import configparser
import os



class readconfig:

    def __init__(self,file_path=None):
        if file_path:
            config_path =file_path
        else:
            config_path =os.path.join(os.path.dirname(__file__), '../config/config.ini')
            print(config_path)
        self.cf = configparser.ConfigParser()
        self.cf.read(config_path)  #读取配置文件


    def get_host_wx(self,param):
        valus=self.cf.get('Hosts-WX',param)
        return valus
        # secs =self.cf.sections()   # 获取文件中所有的section(一个配置文件中可以有多个配置， 每个section由[]包裹，即[section])，并以列表的形式返回)
        # print(secs)
        # options =self.cf.options("Hosts-WX")  # 获取某个section名为Hosts-WX所对应的键
        # print(options)
        # items = self.cf.items("Hosts-WX")  # 获取section名为Hosts-WX所对应的全部键值对
        # print(items)
        # host = self.cf.get("Hosts-WX", "host")  # 获取[Hosts-WX]中host对应的值
        # print(host)

if __name__=='__main__':
    ts=readconfig()
    host=ts.get_host('host')
    print(host)