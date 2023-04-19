# Verify that Java was installed correctly
Write-Host "Verifying Java installation"
java --version

# Verify that Python was installed correctly
Write-Host "Verifying Python installation"
python --version

# Install required python modules with pip
Write-Host "Installing required python modules with pip"
pip install -r requirements.txt

# Install playwright browser engine
Write-Host "Installing Playwright browser engine"
playwright install chromium

# install allure with scoop manager
Write-Host "Installing Allure with Scoop package manager"
Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
#Invoke-Expression (New-Object System.Net.WebClient).DownloadString('https://get.scoop.sh')
irm get.scoop.sh | iex
scoop install allure