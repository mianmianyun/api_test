import xlrd

def excel_to_list(excel_name,sheet):
    data_list=[]
    wb=xlrd.open_workbook(excel_name)  #打开表
    sh=wb.sheet_by_name(sheet)         #在表中找到该sheet
    headers=sh.row_values(0)    #第一行的值
    for i in range(1,sh.nrows):
        d=dict(zip(headers,sh.row_values(i)))  #将标题和每行的数据组装成字典
        data_list.append(d)
    return data_list

def get_case_data(data_list,case_name):
    for case_data in data_list:
        if case_name == case_data['case_name']: #如果字典数据与用例名称一致
            return case_data

if __name__ == '__main__':
    data_list=excel_to_list("test_user_data.xlsx","TestUserLogin")
    case_data=get_case_data(data_list,"test_user_login_normal")
    print(case_data)






