from urllib.parse import urlparse
from ats.utils import initialize_webdriver
from ats.common import get_additional_questions


field_dict = {
    "greenhouse": "//div[@class='field']",
    "catsone": "//div[contains(@class, 'required form-group')]",
    "applytojob": "//div[@class='form-group']",
    "naukri": "",
}


def get_ats(url):
    parsed_url = urlparse(url)
    url_netloc = parsed_url.netloc
    res = [key for key in field_dict if key in url_netloc]
    return res[0] if res else None


def get_field(ats):
    return field_dict.get(ats, None)


def fetch_additional_questions(link):
    # link = "https://boards.greenhouse.io/urbanfootprint/jobs/4761674004#app"
    # link = "https://jbb.applytojob.com/apply/KdTYeKphZ9/IT-Project-Engineer"
    # link = "https://moseleyarchitects.catsone.com/careers/8011-General/jobs/16005026-Interior-Designer/apply?apply=no"

    ats = get_ats(link)
    if ats is None:
        return {'status': 'error', 'message': 'ATS not supported'}

    fields = get_field(ats)
    if fields is None:
        return {'status': 'error', 'message': 'Fields not found'}
    elif fields == "":
        return {'status': 'success', 'additional questions found': 'This job board does not have additional questions'}

    with initialize_webdriver(headless=False) as driver:
        driver.get(link)
        try:
            aqs = get_additional_questions(driver, fields)
            print(aqs)
            response = {
                'status': 'success',
                'additional questions found': len(aqs)
            }
        except Exception as e:
            response = {'status': 'error', 'message': e}

        return response
