1.common文件夹里存放的是常用的py文件
    configEmail.py用于配置自动发送邮件的相关配置
    creatLogs.py用于生成系统运行时的日志文件
    creatReport.py用于系统运行结束后生成的测试报告,默认生成html文件，并保存在result文件夹下面
    getResult.py 用于在测试用例的xls文件中插入测试结果信息
    interfaceTest.py用于进行接口测试，目前仅支持GET请求和post请求
    readTestCase.py用于读取testCase文件下面的测试用例，并返回到一个二维数组中
    runTest.py整个系统的运行文件

2.Image用于存放系统用到的图片
3.result存放生成测试报告的html文件和xls文件
4.testCase用保存接口的测试用例
5.config.ini配置信息
6.readConfig.py用于读取config文件里面的内容