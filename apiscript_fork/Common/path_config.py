import os
# 项目路径
project_dir = os.path.split(os.path.split(os.path.realpath(__file__),)[0])[0]
# 日志路径
log_path = os.path.join(project_dir, "log")
# excel测试数据路径
exc_path = os.path.join(project_dir,  "testCase", "test_Case.xlsx")

# 测试报告路径
report_path = os.path.join(project_dir, "HTML_report", "report.html")

#为什么有的路径要精确到文件，有的路径不需要，是什么决定因素决定的
# if __name__ == '__main__':


