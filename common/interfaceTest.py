import requests,ast,datetime

class interfaceTest:
    def __init__(self):
        pass

    def interfaceTest(self,caselist):
        res_flags=[] #存放每条用例的测试结果（pass或者fail）
        fail_tips=[] #存放失败的用例的提示信息

        print("*"*25+"\n接口测试开始,测试结果如下\n\n")
        now1=datetime.datetime.now()
        for case in caselist:
            try:
                """
                获取用例的具体信息
                """
                casename=case[0]
                case_url=case[1]
                method=case[2]
                header=case[3]
                params=case[4]
                qiwang=int(case[5])
            except Exception:
                print("测试用例数据不正确，请修改！！！")

            if method=='get':
                a=ast.literal_eval(header) #把字段信息转换成dict格式

                if params!='':
                    case_url = case_url + '?' + params
                    #print("URL:"+case_url)
                else:
                    pass
                #print(case_url)
                result=requests.get(case_url,headers=a)
                code=result.status_code
                if code!=qiwang:
                    print("%s:用例执行失败:"%casename + result.text)
                    res_flags.append('fail')
                    fail_tips.append(result.text)
                else:
                    print("%s:用例执行成功"%casename)
                    res_flags.append('pass')
                    fail_tips.append('')
                # else:
                #     case_url=case_url+'?'+params
                #     print("URL:"+case_url)
                #     result = requests.get(case_url, headers=a)
                #     code = result.status_code
                #     if code != qiwang:
                #         print("%s:用例执行失败:" % casename + result.text)
                #         res_flags.append('fail')
                #         fail_tips.append(result.text)
                #
                #     else:
                #         print("%s:用例执行成功" % casename)
                #         res_flags.append('pass')
                #         fail_tips.append('')
            else:
                a=ast.literal_eval(header)#把字段信息转换成dict格式
                b=ast.literal_eval(params)#把字段信息转换成dict格式
                result=requests.post(case_url,headers=a,json=b)
                code = result.status_code
                if code != qiwang:
                    print("%s:用例执行失败:"%case[0] + result.text)
                    res_flags.append('fail')
                    fail_tips.append(result.text)

                else:
                    print("%s:用例执行成功"%case[0])
                    res_flags.append('pass')
                    fail_tips.append('')
        now2 = datetime.datetime.now()
        testtime = (now2-now1).total_seconds() #得到执行用例的时间。
        testtime=round(testtime,2)#时间保留小数点后两位
        print("\n\n接口测试结束\n"+"*"*25+"")
        return res_flags,fail_tips,testtime