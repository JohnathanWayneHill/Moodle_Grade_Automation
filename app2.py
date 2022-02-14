import undetected_chromedriver.v2 as uc
from selenium.webdriver.common.by import By
from module.download_files import time_to_sleep
import getpass


def click_button(element_name: str, id_name: str, button_name: str) -> None:
    ''' 
    Finds and clicks button.
    '''
    # broke here
    button = driver.find_element(By.XPATH,
                                 '//' + element_name + '[@' + id_name + "='" + button_name + "']")
    button.click()
    time_to_sleep()


def send_info(info_type: str, info: str) -> None:
    ''' 
    Sends info to form and clicks next button. 
    '''
    form = driver.find_element(By.XPATH,
                               "//input[@type='" + info_type + "']")
    time_to_sleep()
    form.send_keys(info)
    time_to_sleep()
    
    # click next button
    click_button('span', 'jsname', 'V67aGc')


def select_week() -> str:
    ''' 
    Select week. 
    '''
    # menu for week selection
    week_titles = {'1': 'Week 1: Bootcamp Kick-Off & Introduction to Python',
                   '2': 'Week 2: For Loops and Functions',
                   '3': 'Week 3: Introduction to Data Structures',
                   '4': 'Week 4: Object-Oriented Programming and Data Structures',
                   '5': 'Week 5: All About Algorithms'}
    while True:
        # select week
        print('Select one of following weeks: ')
        print(
            (''.join([i + ') ' + week_titles[i] + '\n'for i in week_titles])))
        week = input('Download week: ')
        if week in week_titles:
            break
        print("Enter weeks 1-5\n")

    return week_titles[week]


# options = uc.ChromeOptions()
# options.add_argument('--headless') # hide browser
driver = uc.Chrome()  # options=options)

homepage = "https://learn.nucamp.co/"
driver.get(homepage)

# select login button
login = driver.find_element(By.ID, "pre-login-form")
time_to_sleep()
login.submit()  # click
time_to_sleep()


# login via Google
click_button('a', 'title', 'Google')  # broke here
email = input("Enter email: ")
password = getpass.getpass("Enter password: ")  # hide when typing
send_info('email', email)
send_info('password', password)

# go to Python Fundamentals page
driver.get("https://learn.nucamp.co/course/view.php?id=29")

week_title = select_week()

# how to clean up ?
target_week = driver.find_element(By.PARTIAL_LINK_TEXT, week_title)
target_week.click()
