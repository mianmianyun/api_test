import unittest
from HTMLTestReportCN import HTMLTestRunner
from lib.send_email import send_mail
from config.config import *

suit=unittest.defaultTestLoader.discover(test_path)
with open(report_file,'wb') as f:
    HTMLTestRunner(stream=f,title="report",description="api test",tester="sun").run(suit)

#f.close()
send_mail()





