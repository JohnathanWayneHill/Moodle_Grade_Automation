'''
Driver code for Moodle grade automation tool.
'''
# from dotenv import load_dotenv  # pip3 install python-dotenv, for login functionality
from selenium import webdriver
# pip install undetected-chromedriver \\\\ put version in requirements.txt
import undetected_chromedriver.v2 as uc  # catch me if you can
from module import download_files as df

# TODO: change filenames from original name to
#            student_name_workshop[week number].[extension]


def main():
    # path to Chrome webdriver
    #driver = webdriver.Chrome('../webdriver/chromedriver')
    driver = uc.Chrome()
    print("driver")
    driver.get("https://learn.nucamp.co/")
    input("Login then press enter.")
    df.time_to_sleep()
    print("navigate to NuCamp page")

    # navigate to python fundamentals class
    driver.get("https://learn.nucamp.co/course/view.php?id=29")
    print("navigate to python page")
    df.time_to_sleep()
    print("select week")
    week = df.select_week()
    df.time_to_sleep()

    print("navigate to selected week")
    # navigate to selected week
    df.click_week_module_link(driver, week)
    df.time_to_sleep()

    print("navigate to weekly assignment")
    # navigate to weekly assignment
    df.click_weekly_assignment_link(driver)  # BROKE HERE
    time_to_sleep()

    # select cohort
    cohort = df.select_cohort_from_list(driver)
    df.time_to_sleep()

    # navigate to cohort
    df.click_cohort(driver, cohort)
    df.time_to_sleep()

    # navigate to grading page
    df.click_grade_button(driver)
    df.time_to_sleep()

    # download assignment and capture assignment name
    assignment_name = df.download_student_assignment(driver)
    df.time_to_sleep()
    # capture student name
    student_name = df.capture_student_name(driver)
    df.time_to_sleep()
    # list of all student names; change when while loop added
    grading_info = []
    grading_info.append((student_name, assignment_name))
    df.time_to_sleep()
    # write assignment info to csv in parent directory
    df.capture_assignment_info(grading_info)

    driver.quit()


if __name__ == '__main__':
    main()
