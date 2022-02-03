# cool but bad idea

'''
# select login button
login = driver.find_element_by_id("pre-login-form")
time_to_sleep()
login.submit()
time_to_sleep()

# login via Google
login_by_google = driver.find_element_by_xpath("//a[@title='Google']")
time_to_sleep()
login_by_google.click()
time_to_sleep()

os.chdir("..")  # move to parent directory
load_dotenv()
email = os.environ.get("EMAIL")
password = os.environ.get("PASSWORD")
os.chdir("Moodle_Grade_Automation")

login_email = driver.find_element_by_xpath("//input[@type='email']")
time_to_sleep()
login_email.send_keys(email)
time_to_sleep()
next_button = driver.find_element_by_xpath("//span[@jsname='V67aGc']")
time_to_sleep()
next_button.click()
time_to_sleep()

login_password = driver.find_element_by_xpath("//input[@type='password']")
time_to_sleep()
login_password.send_keys(password)
time_to_sleep()
next_button = driver.find_element_by_xpath("//span[@jsname='V67aGc']")
next_button.click()
time_to_sleep()
'''
