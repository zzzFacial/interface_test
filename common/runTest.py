
from common import configEmail
from common import creatReport as report
from common import creatLogs
#creatLogs.console_out('logging.log')
email=configEmail.email()#创建发送邮件的对象
try:
    testx=report.runCreatHtml()#生成测试报告
    print("成功生成接口测试报告！")
except :
    print("接口報告生成失敗！！！！！！！！")
    exit(1)
email.sendEmail(testx)




