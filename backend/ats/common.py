from selenium.webdriver.common.by import By


def clean_question(question):
    return question.replace("*", "").strip()


def get_attribute_and_value(element):
    elm_id = element.get_attribute("id")
    elm_name = element.get_attribute("name")
    attribute = ""
    value = ""
    if elm_id:
        attribute = "id"
        value = elm_id
    elif elm_name:
        attribute = "name"
        value = elm_name
    return attribute, value


def extended_xpath(element):
    attribute, value = get_attribute_and_value(element)
    tag = element.tag_name
    aria_label = element.get_attribute("aria-label")
    label = element.get_attribute("label")
    attr_value = element.get_attribute("value")
    if aria_label:
        xpath = f'//{tag}[@{attribute}="{value}" and @aria-label="{aria_label}"]'
    elif label:
        xpath = f'//{tag}[@{attribute}="{value}" and @label="{label}"]'
    elif attr_value:
        xpath = f'//{tag}[@{attribute}="{value}" and @value="{attr_value}"]'
    else:
        xpath = ""

    return xpath


def get_xpath(element):
    xpath = ""
    elm_type = element.get_attribute("type")
    tag = element.tag_name
    unique_elm = ["radio", "checkbox"]
    if elm_type in unique_elm:
        xpath = extended_xpath(element)
    if xpath == "":
        attribute, value = get_attribute_and_value(element)
        if attribute and value:
            xpath = f'//{tag}[@{attribute}="{value}"]'
        else:
            while element.tag_name != "body":
                index = 0
                for i, e in enumerate(element.find_elements(By.XPATH, "./preceding-sibling::*")):
                    if e.tag_name == element.tag_name:
                        index += 1
                # xpath = "/" + element.tag_name + "[" + str(index + 1) + "]" + xpath
                xpath = f"/{element.tag_name}[{index + 1}]{xpath}"
                element = element.find_element(By.XPATH, "./parent::*")
            xpath = "/" + xpath
    return xpath


def single_element(element):
    return get_xpath(element)


def multiple_input_element(driver, elements):
    questions = []
    xpaths = []
    for element in elements:
        placeholder = element.get_attribute("placeholder")
        questions.append(placeholder)
        xpaths.append(get_xpath(element))

    xpath_dict = dict(zip(questions, xpaths))
    return xpath_dict


def multiple_element(driver, elements):
    options = []
    xpaths = []
    for element in elements:
        option_element = element.find_element(By.XPATH, "./parent::*")
        option_text = driver.execute_script("return arguments[0].textContent;", option_element)
        options.append(option_text)
        xpaths.append(get_xpath(element))

    xpath_dict = dict(zip(options, xpaths))
    return xpath_dict


def dropdown_element(driver, element):
    options = element.find_elements(By.XPATH, './/option')
    option_values = []
    xpaths = []
    for option in options:
        option_text = driver.execute_script("return arguments[0].textContent;", option)
        option_values.append(option_text)
        xpaths.append(get_xpath(element))

    xpath_dict = dict(zip(option_values, xpaths))
    return xpath_dict


def display_hidden_elements(driver, element):
    driver.execute_script("arguments[0].style.display = 'block';", element)


primary_question_list = ['first name', 'last name', 'email', 'phone', 'resume', 'resume/cv', '']


def check_if_required(elm):
    elm_class = elm.get_attribute("class")
    if "required" in elm_class or elm.get_attribute("required") or elm.get_attribute("aria-required") or elm.get_attribute(
            "data-required") or elm.get_attribute("data-required-message") or elm.get_attribute(
            "data-validation-required-message") or elm.get_attribute("data-val-required"):
        return True
    else:
        return False


def get_additional_questions(driver, fields):
    print("Working on additional questions...")
    final_data = []
    for field in fields:
        complete_question = field.text
        raw_question = complete_question.split('\n')[0]
        question = complete_question.split('\n')[0]
        question = clean_question(question)
        if question.lower() not in primary_question_list:
            xpath = ""
            elm_type = ""
            long_response = False
            this_data = None
            is_required = "*" in raw_question
            check_required = check_if_required(field)
            if check_required or is_required:
                is_required = True
            placeholder = ""

            if field.find_elements(By.XPATH, './/select'):
                elm_type = "dropdown"
                elm = field.find_elements(By.XPATH, './/select')
                if is_required or check_if_required(elm[0]):
                    xpath = dropdown_element(driver, elm[0])

            elif field.find_elements(By.XPATH, './/input[@type!="hidden"]'):
                elm = field.find_elements(By.XPATH, './/input')
                if is_required or check_if_required(elm[0]):
                    elm_type = elm[0].get_attribute('type')
                    placeholder = elm[0].get_attribute('placeholder')
                    if elm_type in ['text', 'number', 'email', 'tel', 'file']:
                        if len(elm) > 1:
                            results = multiple_input_element(driver, elm)
                            if len(results) > 1:
                                for q_text, xpath in results.items():
                                    this_data = {
                                        'question_text': q_text,
                                        'full_question': complete_question,
                                        'placeholder': placeholder,
                                        'type': elm_type,
                                        'long_response': long_response,
                                        'xpath': xpath,
                                        'page': 0
                                    }
                                    final_data.append(this_data)
                        else:
                            xpath = single_element(elm[0])
                    elif elm_type in ['radio', 'checkbox']:
                        xpath = multiple_element(driver, elm)

            elif field.find_elements(By.XPATH, './/textarea'):
                elm_type = "textarea"
                long_response = True
                elm = field.find_elements(By.XPATH, './/textarea')
                placeholder = elm[0].get_attribute('placeholder')
                if is_required or check_if_required(elm[0]):
                    xpath = single_element(elm[0])

            if xpath and this_data is None:
                this_data = {
                    'question_text': question,
                    'full_question': complete_question,
                    'placeholder': placeholder,
                    'type': elm_type,
                    'long_response': long_response,
                    'xpath': xpath,
                    'page': 0
                }
                final_data.append(this_data)
    print("Done with additional questions...")
    return final_data




