import sys

sys.path.append("/Users/xuewenliang/PycharmProjects/new_interface testing/base/utils")
import pytest
from log import log
from utils import http_method
from utils import reader_excel
from utils import WriteExcel

ExcelVarles = reader_excel.ExcelVarles
rq = http_method.method()
print("接口请求后返回数据为：", rq)

data = reader_excel.OperaitionExcel().ReadExcel_row()  # 数据内容


# print("获取的data数据为：",data)
class Test_case():
    @pytest.mark.parametrize('data', data)  # pytest参数化数据
    # def setUp(self,data):
    #     self.url=data[ExcelVarles.case_url]
    def test_gwyc_api(self, data):
        print(data)
        headers = data[ExcelVarles.case_herader]  # 请求头为空判断
        if len(str(headers).split()) == 0:
            pass
        elif len(str(headers)) >= 0:
            headers = headers

        params = data[ExcelVarles.case_data]  # 参数值为空判断
        print(params)
        if len(str(params).split()) == 0:
            pass
        elif len(str(params).split()) >= 0:

            params = params

        case_code = int(data[ExcelVarles.case_code])

        # def case_result_assert(r):  # 断言code和预期结果
        #     assert r.json()['code'] == case_code
        #     assert r.json()[ExcelVarles.case_result] in json.dumps(r.json(), ensure_ascii=False)

        if data[ExcelVarles.case_method] == 'get':
            print("before")
            r = rq.run_method(
                url=data[ExcelVarles.case_url],
                data=params,
                method='get',
                headers=headers
            )
            print("222")

            content = r.json()

            print(content)

            # case_result_assert(r=r)
        elif data[ExcelVarles.case_method] == 'post':
            print("end")
            print("url为：", data[ExcelVarles.case_url])
            print("请求参数为：", params)
            r = rq.run_method(
                url=data[ExcelVarles.case_url],
                data=params,
                method='post',
                headers=headers
            )

            content = r.json()
            print("content数据为：", content)
            # case_result_assert(r)
            print("下标数据为：", data[ExcelVarles.case_index])
            WriteExcel.writeExcel(data[ExcelVarles.case_index], str(content))
