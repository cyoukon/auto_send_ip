import get_ip
import send_email
import threading
from log import write_log
import config


def check_ip():
    try:
        new_ip = get_ip_obj.public_ip()

        write_log(new_ip, False)

        global my_public_ip
        if my_public_ip != new_ip:
            my_public_ip = new_ip
            text = '公网IP：' + new_ip + '\n' + '内网IP：' + get_ip_obj.get_host_ip()
            send_email_obj = send_email.SendEmail(text)
            send_email_obj.send()
    except:
        write_log('check_ip出错')
    t = threading.Timer(config.frequency, check_ip)
    t.start()

if __name__ == "__main__":
    get_ip_obj = get_ip.GetIp()
    my_public_ip = ''
    check_ip()
