from utils import initialize_webdriver
from time import sleep
from pprint import pprint as p
from selenium.webdriver.common.by import By
from common import get_additional_questions

with initialize_webdriver() as driver:
    # link = "https://boards.greenhouse.io/urbanfootprint/jobs/4761674004#app"
    # link = "https://jbb.applytojob.com/apply/KdTYeKphZ9/IT-Project-Engineer"
    link = "https://moseleyarchitects.catsone.com/careers/8011-General/jobs/16005026-Interior-Designer/apply?apply=no"
    driver.get(link)

    # fields = driver.find_elements(By.XPATH, "//div[@class='field']")
    # fields = driver.find_elements(By.XPATH, "//div[@class='form-group']")
    fields = driver.find_elements(By.XPATH, "//div[contains(@class, 'required form-group')]")

    try:
        aqs = get_additional_questions(driver, fields)
    except Exception as e:
        print(e)
        aqs = {'status': 'error', 'message': e}

    p(aqs)

    print("Total number of Additional Questions: ", len(aqs))