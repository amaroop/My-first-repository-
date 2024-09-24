from selenium import webdriver
from selenium.webdriver.common.by import By

def get_driver():
  options = webdriver.ChromeOptions()
  options.add_argument("disable-infobars")
  options.add_argument("start-maximized")
  options.add_argument("disable-dev-shm-usage")
  options.add_argument("no-sandbox")
  options.add_experimental_option("excludeSwitches",["enable-automation"])
  options.add_argument("disable-blink-features=automatonControlled")

  driver = webdriver.Chrome(options=options)
  driver.get("https://automated.pythonanywhere.com")
  return driver

def clean_text(text)
def main():
    driver = get_driver()
    time.sleep(2)
    dynamic_element = driver.find_element(By.XPATH, "/html/body/div[1]/div/h1[2]")
    return dynamic_element.text

print(main())