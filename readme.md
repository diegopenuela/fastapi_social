# VIRTUALENV

virtualenv -p python3 venv
source venv/bin/activate
pip freeze > requirements.txt
pip install -r requirements.txt


# GITHUB 
git config --local user.email "myemail"
git config --local user.name "myusername"

mkdir my_project
cd my_project
touch .gitignore
git init
git status
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://diegopenuela: (MYTOKEN) @github.com/diegopenuela/fastapi_social.git

git remote set-url origin https://diegopenuela: (MYTOKEN) @github.com/diegopenuela/fastapi_social.git
git push -u origin main

# FASTAPI
uvicorn app.main:app --reload 

http://127.0.0.1:8000/redoc
http://127.0.0.1:8000/docs

