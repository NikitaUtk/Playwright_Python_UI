import subprocess
subprocess.Popen('cd D:\\Nikita\\PythonProject\\Python_Test_v', shell=True).wait()
# subprocess.Popen('python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_1.py --alluredir=.\\allure-results', shell=True).wait()
# subprocess.Popen('python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_2.py --alluredir=.\\allure-results', shell=True).wait()
# subprocess.Popen('python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_3.py --alluredir=.\\allure-results', shell=True).wait()
# subprocess.Popen('python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_4.py --alluredir=.\\allure-results', shell=True).wait()
# subprocess.Popen('python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_5.py --alluredir=.\\allure-results', shell=True).wait()
subprocess.Popen('python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_5_1.py --alluredir=.\\allure-results', shell=True).wait()
# subprocess.Popen('python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_6.py --alluredir=.\\allure-results', shell=True).wait()
# subprocess.Popen('python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_6_1.py --alluredir=.\\allure-results', shell=True).wait()
subprocess.Popen('allure serve allure-results', shell=True).wait()