# /usr/bin/python
# coding=utf-8
import traceback
import time


def write_log(msg='', write_file=True):
    try:
        now_time = '【' + \
            time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '】'

        log_str = ''
        if msg.strip() != '':
            log_str += now_time + msg + '\n'

        err = traceback.format_exc()
        if err.strip() != 'NoneType: None':
            log_str += now_time + err

        print(log_str)

        if write_file:
            with open('send_ip.log', 'a') as f:
                f.writelines(log_str + '\n')
    except Exception as e:
        print('防止程序奔溃，保险起见，这里再catch一层\n' + str(e))
