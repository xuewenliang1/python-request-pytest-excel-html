from xlrd import open_workbook
import json
import file_path

file_url = file_path.get_path()
print("文件路径为：", file_url)


class ExcelVarles:
    case_ID = "用例id"
    case_Name = "用例名称"
    case_url = "用例地址"
    case_method = "请求方法"
    case_data = "请求参数"
    case_herader = "请求头"
    case_perposition = "前置条件"
    case_isrun = "是否执行"
    case_code = "状态码"
    case_result = "预期结果"
    case_practice = "实际结果"
    case_index = "行数"


class OperaitionExcel():
    def ReadExcel_row(self):
        data = []
        file = open_workbook(file_url)
        sheet = file.sheet_by_index(0)
        nrow = sheet.nrows
        print(nrow)
        title = sheet.row_values(0)
        for i in range(1, nrow):
            print(sheet.row_values(i))
            value = sheet.row_values(i)
            value_dict=dict(zip(title, value))
            print(value_dict)
            param=value_dict.get("请求参数")
            param_dict={}
            param_list=param.split("&")
            value_dict["行数"] = i
            for i in param_list:
                param_dict[i.split("=")[0]]=i.split("=")[1]
            value_dict["请求参数"]=param_dict
            data.append(value_dict)
            print(data)

        return data

    def ReadExcel_col(self):
        file = open_workbook(file_url)
        sheet = file.sheet_by_index(0)
        clos = sheet.nrows
        print(clos)
        col_value = []
        for s in range(0, clos):
            print(sheet.col_values(s))
            a = sheet.col_values(s)
            col_value.append(a)

        return col_value


if __name__ == '__main__':
    OperaitionExcel().ReadExcel_row()
