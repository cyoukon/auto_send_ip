import log

try:
    print(1/10)
    log.write_log()
    log.write_log('scu')
except:
    log.write_log()
    log.write_log('err')