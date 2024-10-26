import undetected_chromedriver as uc

# no headless driver
def chrome_driver():
    options = uc.ChromeOptions()
    # 팝업 블록 popup block
    options.add_argument("--disable-popup-blocking")
    # 크롬 비밀번호 팝업 차단 chrome password leak detection : false
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(headless=False,options=options, use_subprocess=False)
    driver.set_window_size(900, 1200)
    return driver

# headless driver
def headless_chrome_driver():
    options = uc.ChromeOptions()
    # 팝업 블록 popup block
    options.add_argument("--disable-popup-blocking")
    # 크롬 비밀번호 팝업 차단 chrome password leak detection : false
    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.password_manager_leak_detection": False
    }
    options.add_experimental_option("prefs", prefs)

    driver = uc.Chrome(headless=True,options=options, use_subprocess=False)
    return driver