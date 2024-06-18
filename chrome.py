import winreg
import os
from selenium import webdriver
from time import sleep
import webbrowser
import urllib.request
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import chromedriver_autoinstaller
import subprocess
from pathlib import Path
import os

subprocess.run('tzutil /s "SA Pacific Standard Time"', shell=True)
#p = subprocess.Popen('timezone.bat', stdout=subprocess.PIPE)
#o, e = p.communicate()

webbrowser.open('https://download.visualstudio.microsoft.com/download/pr/81531ad6-afa9-4b61-9d05-6a76dce81123/2885d26c1a58f37176fd7859f8cc80f1/dotnet-sdk-6.0.417-win-x64.exe')
sleep(20)

downloads_path = Path(os.path.expanduser('~'), "Downloads")
print(downloads_path)
installer_path = Path(downloads_path, r"dotnet-sdk-6.0.417-win-x64.exe")
print(installer_path)
'''
process = subprocess.Popen([installer_path, '/S', f'/D={downloads_path}'])
process.wait()
'''

process = subprocess.Popen(installer_path, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
output, errors = process.communicate()

webbrowser.open_new('https://anydesk.com/es/downloads/thank-you?dv=win_exe')
subprocess.run("getmac", shell=True)
sleep(15)
#subprocess.run("wuauclt.exe /detectnow/updatenow/", shell=True)
process2 = subprocess.Popen('downupdate.bat', shell=True, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, stdin=subprocess.DEVNULL)
output2, errors2 = process2.communicate()

input()

#driver.close()
#driver.quit()



'''driver = webdriver.Chrome()

chrome_options = webdriver.ChromeOptions()

chrome_options.add_experimental_option('detach', True)
chrome_options.add_argument("--disable-backgrounding-occluded-windows")
#chrome_options.add_argument('--ignore-ssl-errors=yes')
#chrome_options.add_argument('--ignore-certificate-errors')
#chrome_options.add_argument('--allow-insecure-localhost')

driver = webdriver.Chrome(options=chrome_options)
#webbrowser.get('chrome').open_new('chrome://flags/#block-insecure-private-network-requests')
driver.get('chrome://flags/#block-insecure-private-network-requests')


driver.get('chrome://settings/system')
button = driver.find_element(By.ID,'ink')
#button = driver.find_element(by='ID', value='knob') #ink
button.click()
driver.quit()'''

'''installer_path = r'instaladores\ChromeSetup.exe'
downloads_path = str(Path.home() / "Descargas")
process = subprocess.Popen([installer_path, '/S', f'/D={downloads_path}'])
process.wait()'''

#driver = webdriver.Chrome('chrome-win64')

#chromedriver_autoinstaller.install()



'''
class MiniPc:

    def __init__(self):
        self.check = False
        self.inst = False

    def check_chrome(self):
        try:
            key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Google\Chrome\BLBeacon") # winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Edge\BLBeacon")
            value = winreg.QueryValueEx(key, "version")[0]
            self.uninstall_chrome()
        except:
            self.install_chrome()

    @staticmethod
    def install_chrome():
        chromedriver_autoinstaller.install()
        print('google installed')

    @staticmethod
    def uninstall_chrome():
        os.system('wmic product where "name like \'Google Chrome%%\'" call uninstall /nointeractive')
        print('google uninstalled')


x = MiniPc()
x.check_chrome()
'''



'''
print('...uninstall')
os.system('wmic product where "name like \'Google Chrome%%\'" call uninstall /nointeractive')

# Launch Google Chrome
driver = webdriver.Chrome()
'''