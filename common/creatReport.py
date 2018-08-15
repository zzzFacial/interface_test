import os,time
from common import getResult as GR
from common import interfaceTest as INTF
from common import readTestCase as RT
import readConfig as config

caselist=[]#用于存放获取的测试用例
result=GR.getResult()#创建生成结果的对象
con=config.Readconfig()#创建读取配置文件的对象
testcase=RT.readTestCase()#创建读取测试用例的对象
interface=INTF.interfaceTest()#创建执行测试的对象


username=con.get_email("testuser")#读取config文件中的testuser参数


path=os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
casePath='%s/testCase/testcase.xls'%path


caselist=testcase.getCase(casePath)#获取文件的测试用例
res_flag,fail_tips,testtime=interface.interfaceTest(caselist)#执行测试用例
result_path=result.copy_execl(casePath,res_flag,fail_tips)#生成测试结果的excel文件
caselist1=testcase.getCase(result_path)
report_path='%s/result/%s_report.html'%(path,time.strftime('%Y%m%d%H%M'))
titles="%s_接口測試報告"%time.strftime('%Y%m%d')

def getnum():
    passNum=0
    failNum=0
    casenum=len(caselist1)
    for i in range(casenum):
        if caselist1[i][7]=='pass':
            passNum=passNum+1
        else:
            failNum=failNum+1
    return passNum,failNum




def title(titles):
    title = '''<!DOCTYPE html>
	<html lang="en">
	<head>
		<meta charset="UTF-8">
		<title>%s</title>
		<style type="text/css">
			td{ width:40px; height:50px;}
			body{background-repeat:no-repeat;background-size: cover;}
		</style>
	</head>
	<body background="../Image/11.jpg">
	''' % (titles)
    return title


connent = '''
<div style='width: 1170px;margin-left: 20%'>
<h1>接口测试报告</h1>'''


def time( starttime,testtime,username, passNum, failNum):
    beijing = '''
		<p><strong>开始时间:</strong> %s</p>
		<p><strong>测试耗时:</strong> %s秒</p>
		<p><strong>测试人員:</strong> %s</p>
		<p><strong>结果:</strong> 
		
			<span >Pass: <strong >%s</strong>
			Fail: <strong >%s</strong>
			        </span></p>                  
			    <p ><strong>测试详情如下:</strong></p>  </div> ''' % (starttime,testtime,username, passNum, failNum)
    return beijing


shanghai = '''
        <p> </p>
        <table border='2'cellspacing='1' cellpadding='1' width='1100'align="center" >
		<tr >
            <td><strong>用例名字</strong></td>
            <td><strong>url</strong></td>
            <td><strong>请求方式</strong></td>
            <td><strong>Headers</strong></td>
            <td><strong>参数</strong></td>
            <td><strong>预期结果</strong></td>
            <td><strong>失败信息</strong></td>
            <td><strong>pass/fail</strong></td>  
        </tr>
    '''


def passfail(tend):
    if tend == 'pass':
        htl = ' <td bgcolor="green">pass</td>'

    else:
        htl = ' <td bgcolor="red">fail</td>'

    return htl



def ceshixiangqing(name, url, meth,header,params,yuqi,message,result):
    xiangqing = '''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>   
                %s 
        </tr>

    ''' %(name, url, meth, header,params,yuqi,message,result)
    return xiangqing


weibu = '''
	</table>

    </body>
    </html>'''


passNum,failNum=getnum()
def result(titles,testtime,username,passNum,failNum,caselist1):
    relus=''
    for i in range(len(caselist1)):
        relus+=ceshixiangqing(caselist1[i][0],caselist1[i][1],caselist1[i][2],caselist1[i][3],caselist1[i][4],int(caselist1[i][5]),caselist1[i][6],passfail(caselist1[i][7]))
    text=title(titles)+connent+time(caselist1[0][7],testtime,username,passNum,failNum)+shanghai+relus+weibu
    return text

def creatHtml(titles,testtime,username,passNum,failNum,caselist1):
    texts=result(titles,testtime,username,passNum,failNum,caselist1)
    with open(report_path,'wb') as f:
        f.write(texts.encode('utf-8'))

    return texts

def runCreatHtml():
    texts=creatHtml(titles,testtime,username,passNum,failNum,caselist1)
    return texts

