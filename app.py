'''
Driver code for Moodle grade automation tool.
'''
from dotenv import load_dotenv  # pip3 install python-dotenv
from selenium import webdriver
# pip install undetected-chromedriver
import undetected_chromedriver.v2 as uc  # catch me if you can
import time
import random
import os
import csv


def time_to_sleep():  # catch me if you can
    round = random.randint(1, 4)
    num = random.uniform(0, 10)
    const = 10 ** round
    num_round = (((num) * const) // 1) / const
    print(num_round)
    time.sleep(num_round)


def select_week():
    # select week
    while True:
        weeks = [str(i) for i in range(1, 6)]
        # select week
        print('Select one of following weeks: ')
        print((''.join([i + ') ' + ' week ' + i + '\n'for i in weeks])))
        week = input('Download week: ')
        if week in weeks:
            break
        print("Enter weeks 1-4\n")
    return week


def click_week_module_link(driver, week):
    week_title = {'1': 'Week 1: Bootcamp Kick-Off & Introduction to Python',
                  '2': 'Week 2: For Loops and Functions',
                  '3': 'Week 3: Introduction to Data Structures',
                  '4': 'Week 4: Object-Oriented Programming and Data Structures',
                  '5': 'Week 5: All About Algorithms'}

    # enter week module
    target_week = driver.find_element_by_partial_link_text(week_title[week])
    time_to_sleep()
    target_week.click()


def click_weekly_assignment_link(driver):
    # select assignment link
    # put back?
    #assignment_link = driver.find_element_by_xpath("//span[@class='instancename']")
    list_of_hrefs = driver.find_elements_by_tag_name("a")
    print("getting hrefs")
    assignment_hrefs = [
        i for i in list_of_hrefs if 'assign' in i.get_attribute('href')]
    print("getting assignment hrefs")
    assignment_link = assignment_hrefs[2].get_attribute("href")
    print("getting second href")
    time_to_sleep()
    driver.get(assignment_link)
    print("navigate to assignment page")


'''
# select grade button 
grade_button = driver.find_element_by_xpath(
    "//a[@class='btn btn-primary ml-1']")
'''


def select_cohort_from_list(driver):
    # to select cohorts
    options = driver.find_elements_by_tag_name("option")
    # finding is.digit() because "seperate groups" option values are digits,
    #    rest are links
    cohorts = [i.get_attribute("text")
               for i in options if i.get_attribute("value").isdigit()]
    ls_tups_cohorts = [(str(num), ch) for num, ch in list(enumerate(cohorts))]
    cohort_options = {ch[0]: ch[1] for ch in ls_tups_cohorts}
    print(options[0])
    print(options[0].get_attribute("text"))
    while True:
        print("select cohort: ")
        print(''.join([i + ') ' + cohort_options[i] +
              '\n' for i in cohort_options]))
        option = input('select option: ')
        if option in cohort_options:
            break
        print("choose again\n")
    return cohort_options[option]


def click_cohort(driver, select):
    cohort = driver.find_element_by_xpath("//*[text()='" + select + "']")
    cohort.click()


def click_grade_button(driver):
    # click grade button
    grade_button = driver.find_element_by_xpath(
        "//a[@class='btn btn-primary ml-1']")
    grade_button.click()


def download_student_assignment(driver):
    # link to download assignment
    list_of_hrefs = driver.find_elements_by_tag_name("a")
    link = [i for i in list_of_hrefs if i.get_attribute(
        "target") == '_blank'][0]
    assignment_name = link.get_attribute("text")
    link.click()
    return assignment_name


def capture_student_name(driver):
    # getting student name
    links = driver.find_elements_by_tag_name("a")
    links_text = [i.get_attribute("text") for i in links]
    student = links_text[4]
    student_info = student.split("\n")
    student_name = student_info[2].strip()
    return student_name


def capture_assignment_info(grading_info):
    # write (student_name, filename) to csv file - to be used in bash script
    os.chdir('../grade_data')
    with open('grade_data.csv', 'w') as file:
        csv_file = csv.writer(file)
        for row in grading_info:
            csv_file.writerow(row)
    os.chdir('../Moodle_Grade_Automation')

# TODO: change filenames from original name to
#            student_name_workshop[week number].[extension]


def main():
    # path to Chrome webdriver
    #driver = webdriver.Chrome('../webdriver/chromedriver')
    driver = uc.Chrome()
    print("driver")
    driver.get("https://learn.nucamp.co/")
    input("Login then press enter.")
    time_to_sleep()
    print("navigate to NuCamp page")

    # navigate to python fundamentals class
    driver.get("https://learn.nucamp.co/course/view.php?id=29")
    print("navigate to python page")
    time_to_sleep()
    print("select week")
    week = select_week()
    time_to_sleep()

    print("navigate to selected week")
    # navigate to selected week
    click_week_module_link(driver, week)
    time_to_sleep()

    print("navigate to weekly assignment")
    # navigate to weekly assignment
    click_weekly_assignment_link(driver)  # BROKE HERE
    time_to_sleep()

    # select cohort
    cohort = select_cohort_from_list(driver)
    time_to_sleep()

    # navigate to cohort
    click_cohort(driver, cohort)
    time_to_sleep()

    # navigate to grading page
    click_grade_button(driver)
    time_to_sleep()

    # download assignment and capture assignment name
    assignment_name = download_student_assignment(driver)
    time_to_sleep()
    # capture student name
    student_name = capture_student_name(driver)
    time_to_sleep()
    # list of all student names; change when while loop added
    grading_info = []
    grading_info.append((student_name, assignment_name))
    time_to_sleep()
    # write assignment info to csv in parent directory
    capture_assignment_info(grading_info)

    driver.quit()


if __name__ == '__main__':
    main()
