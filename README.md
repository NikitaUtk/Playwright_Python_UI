# Playwright python

**Project setup**

```
cd playwright_python

pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

Для установки allure сначала необходимо установить scoop через powershell
Необходимо по очереди запустить 4 команды которые указаны ниже
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
scoop install allure


```

**Starting auto tests**

```
python -m pytest --alluredir=./allure-results
-----genearate allure page
allure serve allure-results
```
