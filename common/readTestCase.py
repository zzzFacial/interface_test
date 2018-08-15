import xlrd
class readTestCase:
    def __init__(self):
        pass


    def getCase(self,file_path):
        case_list = []  # 用来存放每一条用例的信息
        try:
            # print(file_path)
            book=xlrd.open_workbook(file_path)
        except Exception as e:
            print("读取测试用例文件时，文件路径不正确！！")
            print(e)
            exit(1)

        sheet=book.sheet_by_index(0) #获取第一个sheet页
        rows=sheet.nrows #获取总的case条数
        for i in range(rows):
            if i!=0:
                case_list.append(sheet.row_values(i))
        return case_list


