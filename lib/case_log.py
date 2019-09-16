from config.config import *
import json

def case_log(case_name,url,header,data,except_resp,resp_cade,resp_text):

    if isinstance(data,dict):
       data=json.dumps(data)

    logging.info("测试用例：{}".format(case_name))
    logging.info("url：{}".format(url))
    logging.info("headers：{}".format(header))
    logging.info("请求数据：{}".format(data))
    logging.info("期望结果：{}".format(except_resp))
    logging.info("实际状态码：{}".format(resp_cade))
    logging.info("实际结果：{}".format(resp_text))