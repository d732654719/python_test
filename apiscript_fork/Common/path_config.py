import os
# 项目路径
project_dir = os.path.split(os.path.split(os.path.realpath(__file__),)[0])[0]
# 日志路径
log_path = os.path.join(project_dir, "log")
# excel路径
exc_path = os.path.join(project_dir,"testCase","test_Case.xlsx")
print(exc_path)

# if __name__ == '__main__':


