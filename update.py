import os
git_url = input("Enter your git url : ")
os.system('git add .')
os.system('git status')
os.system('git commit -m "updated file"')
os.system('git push origin master')

print("Your Repository is successfully Updated!!")