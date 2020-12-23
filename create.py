from selenium import webdriver
import time
import clipboard
import os

username = 'your_username'
password = 'your_password'
repo_name = input('Enter your Repository name : ')

driver = webdriver.Chrome('provide_path_of_your_chromedriver')
driver.get('https://github.com/')
signin = driver.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]')
signin.click()
u_name = driver.find_element_by_id('login_field')
u_name.send_keys(username)
login_password = driver.find_element_by_id('password')
login_password.send_keys(password)
submit = driver.find_element_by_name('commit')
submit.click()
new_repository = driver.find_element_by_xpath('//*[@id="repos-container"]/h2/a')
new_repository.click()
repository_name = driver.find_element_by_id('repository_name')
repository_name.send_keys(repo_name)
readme = driver.find_element_by_id('repository_auto_init')
readme.click()
create_repo = driver.find_element_by_xpath('//*[@id="new_repository"]/div[4]/button')
create_repo.submit()
driver.implicitly_wait(10)
clone_repo=driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/summary')
clone_repo.click()
clone_copy = driver.find_element_by_xpath('//*[@id="js-repo-pjax-container"]/div[2]/div/div[2]/div[1]/div[2]/span/get-repo/details/div/div/div[1]/div/tab-container/div[3]/div/div/clipboard-copy')
clone_copy.click()
git_url = clipboard.paste()
time.sleep(3)
driver.quit()

os.system('git init')
os.system('git add .')
os.system('git status')
os.system('git commit -m "Initial commit"')
os.system('git remote add origin '+git_url)
os.system('git pull --rebase origin master')
os.system('git push origin master')

print(repo_name+" repository created !!!")