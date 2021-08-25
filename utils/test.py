import requests
import reader_excel
from bs4 import BeautifulSoup
Excelvars=reader_excel.ExcelVarles()
data=reader_excel.OperaitionExcel().ReadExcel_row()
print("获取的URL为：",data[Excelvars.case_url])
class HTTP():
    def request(self,url,params):
        rq=requests.post(url,params)
        print("测试结果为：",rq)
        return rq









