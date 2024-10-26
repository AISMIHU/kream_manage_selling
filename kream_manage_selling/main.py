from kream_manage_selling.kream_config.kream_login import kream_login
from kream_manage_selling.driver import chrome_driver

def main():
    driver = chrome_driver()
    if not kream_login(driver):
        print("failed login")
    driver.quit()
        

if __name__ == "__main__":
    main()