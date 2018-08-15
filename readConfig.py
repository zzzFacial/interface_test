"""
读取config.ini文件里面的信息
"""
import os
import codecs
import configparser
proDir=os.path.split(os.path.realpath(__file__))[0]#获取当前文件的绝对路径
configPath=os.path.join(proDir,"config.ini")

class Readconfig:
    def __init__(self):
        fd=open(configPath)
        data=fd.read()

        if data[:2]==codecs.BOM_UTF8:
            data=data[2:]
            file=codecs.open(configPath,"w")
            file.write(data)
            file.close()
        fd.close()

        self.cf=configparser.ConfigParser()
        self.cf.read(configPath)


    def get_email(self,name):
        value=self.cf.get("EMAIL",name)
        return value

    # def get_filePath(self,name):
    #     value=self.cf.get("TESTCASE",name)
    #     return value

