import subprocess
import time
import sys,os

args = sys.argv
test_name = args[1]

cwd = os.getcwd()

start = time.time()
if test_name == 'test':
    subprocess.Popen(f'python -m pytest {cwd}\\tests --alluredir=.\\allure-results', shell=True).wait()
else:
    subprocess.Popen(f'python -m pytest {cwd}\\tests\\{test_name}.py --alluredir=.\\allure-results', shell=True).wait()
end = time.time() - start
print(end)
subprocess.Popen('allure serve allure-results', shell=True).wait()