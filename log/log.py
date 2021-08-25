from loguru import logger
import os
import time
timestr=time.strftime("%Y-%m-%d",time.localtime())
print(timestr)
if os.path.exists("/Users/xuewenliang/PycharmProjects/new_interface testing/base/log/"+timestr)==False:
    os.mkdir(timestr)
logger.add("/Users/xuewenliang/PycharmProjects/new_interface testing/base/log/{}/".format(timestr)+timestr+".log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
def write_debug(content):
    logger.debug(str(content))

# logger.info("这是一条info日志")
# logger.error("错误")
# logger.add("file2.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}")
# logger.debug("That's it, beautiful and simple logging!")
