import xlrd,time,os
from xlutils import copy

path=os.path.dirname(os.path.dirname(__file__))
class getResult:
    def __init__(self):
        pass

    def copy_execl(seif,file_path, res_flags, fail_tips):
        book = xlrd.open_workbook(file_path)
        new_book = copy.copy(book)
        sheet = new_book.get_sheet(0)
        i = 1
        for res_flag, fail_tip in zip(res_flags, fail_tips):
            sheet.write(i, 6, u'%s' % fail_tip)
            #sheet.write(i, 7, u'%s' % time.strftime('%Y%m%d%H%M%S'))
            sheet.write(i, 7, u'%s' % res_flag)
            i = i + 1
        result_path='%s/result/%s_接口测试结果.xls'%(path,time.strftime('%Y%m%d%H%M'))
        new_book.save(result_path)
        return result_path