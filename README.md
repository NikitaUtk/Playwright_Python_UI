# Playwright python

**Project setup**

```
cd playwright_python

pip install virtualenv
virtualenv venv
source venv/bin/activate

pip install -r requirements.txt

install scoop in powerShell
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
irm get.scoop.sh | iex
install allure
scoop install allure


```

**Starting auto tests**

```
python -m pytest --alluredir=./allure-results
-----genearate allure page
allure serve allure-results
```
