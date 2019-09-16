import unittest
import requests
from api_test.lib.case_log import  *
from api_test.lib.read_excel import *
from api_test.config.config import *
import os

class TestUserLogin(unittest.TestCase):

    login_url="http://hm.xuyon.com/user/login"
    login_header={"Content-Type": "application/json"}

    @classmethod
    def setUpClass(cls):
        cls.data_list=excel_to_list(os.path.join(data_path, "test_user_data.xlsx"),"TestUserLogin")

    def test_user_login_normal(self): #用户正常登录的用例
        case_data=get_case_data(self.data_list,"test_user_login_normal")
        url=case_data['url']
        header=case_data['headers']
        header=json.loads(header)
        data=case_data['data']
        data=json.loads(data)
        excep_resp=case_data['execpt_resp']

        resp=requests.post(url=url,headers=header,data=json.dumps(data))
        case_log("test_user_login_normal",url,header,data,excep_resp,resp.status_code,resp.text)
        self.assertIn(excep_resp,resp.text)  #断言

    def test_user_login_password_wrong(self):
        case_data=get_case_data(self.data_list,"test_user_login_password_wrong")
        url=case_data['url']
        header=case_data['headers']
        header=json.loads(header)
        data=case_data['data']
        data=json.loads(data)
        excep_resp=case_data['execpt_resp']
        excep_resp=json.loads(excep_resp)

        resp=requests.post(url=url,headers=header,data=json.dumps(data)) #发送请求
        case_log("test_user_login_password_wrong",url,header,data,excep_resp,resp.status_code,resp.text)
        self.assertDictEqual(json.loads(resp.text),excep_resp)  #断言

if __name__=='__main__':
    unittest.main(verbosity=2)




