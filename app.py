# code by savir singh
# Feedite Status App

from selenium import webdriver
from PIL import Image
import imagehash
from flask import *

app = Flask(__name__)

@app.route("/check_login_page")
def check_login():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
 
    login_page = "https://feedite.pythonanywhere.com/login"
     
    driver.get(login_page)
    driver.save_screenshot("login_page.png")

    lh = imagehash.average_hash(Image.open('login_page.png')) 
    lh2 = imagehash.average_hash(Image.open('correct_login_page.png')) 
    m = 8

    if lh-lh2<m:
      return "OK"
    else:
      return "Not OK"

@app.route("/check_signup_page")
def check_signup():
    driver = webdriver.Chrome(executable_path="chromedriver.exe")
 
    signup_page = "https://feedite.pythonanywhere.com/signup/"

    driver.get(signup_page)
    driver.save_screenshot("signup_page.png")

    lh3 = imagehash.average_hash(Image.open('signup_page.png')) 
    lh4 = imagehash.average_hash(Image.open('correct_signup_page.png')) 
    m2 = 8

    if lh3-lh4<m2:
      return "OK"
    else:
      return "Not OK"

if __name__=='__main__':
    app.run(debug=True)
