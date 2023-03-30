import subprocess
for p in ['cd D:\\Nikita\\PythonProject\\Python_Test_v', 'python -m pytest D:\\Nikita\\PythonProject\\Python_Test_v\\tests\\test_3.py --alluredir=.\\allure-results', 'allure serve allure-results' ]:
    subprocess.Popen(p, shell=True).wait()
