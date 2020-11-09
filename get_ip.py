import requests
import urllib.request
import socket
from log import write_log


class GetIp():
    """用于获取IP地址的类"""

    def __init__(self):
        self.__url1 = "http://ip.42.pl/raw"
        self.__url2 = "http://ipv4.icanhazip.com/"
        self.__url3 = "http://www.trackip.net/"

    def __parse_ip(self):
        """解析__url3这个地址的信息,得到ip"""
        r = requests.get(self.__url3)
        txt = r.text
        ip = txt[txt.find('title')+6:txt.find('/title')-1]
        return ip

    def public_ip(self):
        """获取公网IP"""
        ip = '获取公网IP失败!!!'
        try:
            ip = str(urllib.request.urlopen(self.__url1).read())
        except:
            write_log('url1' + ip)
            try:
                ip = str(urllib.request.urlopen(self.__url2).read())
            except:
                write_log('url2' + ip)
                try:
                    ip = self.__parse_ip()
                except:
                    write_log('url3' + ip)
        return ip

    def get_host_ip(self):
        """
        查询本机ip地址
        :return: ip
        """
        ip = '获取内网IP失败'
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        except:
            write_log(ip)
        finally:
            if s is not None:
                s.close()
        return ip
