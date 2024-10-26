# kream_login.py
from ..driver import chrome_driver  # 상위 폴더(kream_manage_selling)에서 driver 가져오기
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import json
import os
import time


class XpathSelectors:
    ID_INPUT_1 = '//*[@id="wrap"]/div[3]/div/div/div[1]/div/input'
    ID_INPUT_2 = '//*[@id="wrap"]/div[3]/div/form/div[1]/div/input'

    PW_INPUT_1 = '//*[@id="wrap"]/div[3]/div/div/div[2]/div/input'
    PW_INPUT_2 = '//*[@id="wrap"]/div[3]/div/form/div[2]/div/input'

    LOGIN_BTN_1 = '//*[@id="wrap"]/div[3]/div/div/div[3]/a'
    LOGIN_BTN_2 = '//*[@id="wrap"]/div[3]/div/form/div[3]/button'

def kream_login(driver):
    kream_login_success_boolean = False # 변수 초기화

    if driver is None:
        driver = chrome_driver()
    driver.get("https://www.kream.co.kr/login")

    # account.json에서 'site'=='kream'인 아이디 비밀번호 가져오기
    kream_id, kream_pw = load_account_data()

    if kream_id == None:
        kream_login_success_boolean = False
        return kream_login_success_boolean
    
    # find id input xpath
    try:
        id_xpath = driver.find_element(By.XPATH, XpathSelectors.ID_INPUT_1)
    except NoSuchElementException:
        try:
            id_xpath = driver.find_element(By.XPATH, XpathSelectors.ID_INPUT_2)
        except NoSuchElementException:
            print("ID XPATH 값을 찾을 수 없습니다.")
            kream_login_success_boolean = False
            return kream_login_success_boolean
        
    # find pw input xpath
    try:
        pw_xpath = driver.find_element(By.XPATH, XpathSelectors.PW_INPUT_1)
    except NoSuchElementException:
        try:
            pw_xpath = driver.find_element(By.XPATH, XpathSelectors.PW_INPUT_2)
        except NoSuchElementException:
            print("PW XPATH 값을 찾을 수 없습니다 ")
            kream_login_success_boolean = False
            return kream_login_success_boolean
    
    # find login btn xpath
    try:
        login_btn_xpath = driver.find_element(By.XPATH, XpathSelectors.LOGIN_BTN_1)
    except NoSuchElementException:
        try:
            login_btn_xpath = driver.find_element(By.XPATH, XpathSelectors.LOGIN_BTN_2)
        except NoSuchElementException:
            print("LOGIN BTN 값을 찾지 못했습니다.")
            kream_login_success_boolean = False
            return kream_login_success_boolean
        
    # 로그인 실행
    try:
        id_xpath.send_keys(kream_id)
        pw_xpath.send_keys(kream_pw)
        time.sleep(3)
        login_btn_xpath.click()
    except NoSuchElementException:
        print("Element not found!")  # 요소를 찾지 못했을 때
        kream_login_success_boolean = False
        return kream_login_success_boolean
    time.sleep(5)
    if driver.current_url == "https://kream.co.kr/":
        kream_login_success_boolean = True
        return kream_login_success_boolean
    return kream_login_success_boolean

def load_account_data():
    # account.json 파일이 있는지 확인하고, 있으면 "kream" 사이트의 ID와 PW 필드를 채운다.
        if os.path.exists('./data/account.json'):
            with open('./data/account.json', 'r') as json_file:
                account_data_list = json.load(json_file)
                # account_data_list가 리스트인지 확인하고, site가 'kream'인 항목을 찾음
                for account_data in account_data_list:
                    if account_data.get("site") == "kream":
                        kream_id = account_data.get("id","")
                        kream_pw = account_data.get("pw","")
                        print("Kream 계정 정보가 불러와졌습니다.")
                        return kream_id, kream_pw
                print("Kream 계정 정보가 없습니다.")
                kream_id, kream_pw = None,None
                return kream_id, kream_pw
        else:
            print("account.json 파일이 존재하지 않습니다.")
            kream_id, kream_pw = None, None
            return kream_id, kream_pw