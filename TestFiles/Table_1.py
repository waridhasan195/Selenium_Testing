# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException

# table_rows = []
# options = webdriver.ChromeOptions() 
# options.add_argument("start-maximized")
# options.add_argument('disable-infobars')
# driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
# driver.get("https://www.investing.com/economic-calendar/investing.com-eur-usd-index-1155")
# show_more_button = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.genTbl.openTbl.ecHistoryTbl#eventHistoryTable1155 tr>th.left.symbol")))
# driver.execute_script("arguments[0].scrollIntoView(true);",show_more_button);
# myLength = len(WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.genTbl.openTbl.ecHistoryTbl#eventHistoryTable1155 tr[event_attr_id='1155']"))))
# while True:
#     try:
#         WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#showMoreHistory1155>a"))).click()
#         WebDriverWait(driver, 20).until(lambda driver: len(driver.find_elements_by_css_selector("table.genTbl.openTbl.ecHistoryTbl#eventHistoryTable1155 tr[event_attr_id='1155']")) > myLength)
#         table_rows = driver.find_elements_by_css_selector("table.genTbl.openTbl.ecHistoryTbl#eventHistoryTable1155 tr[event_attr_id='1155']")
#         myLength = len(table_rows)
#     except TimeoutException:
#         break
# for row in table_rows:
#     print(row.text)
# driver.quit()


















from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

table_rows = []
options = webdriver.ChromeOptions() 
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver=webdriver.Chrome(chrome_options=options, executable_path=r'C:\WebDrivers\chromedriver.exe')
driver.get("https://www.investing.com/economic-calendar/investing.com-eur-usd-index-1155")
show_more_button = WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "table.genTbl.openTbl.ecHistoryTbl#eventHistoryTable1155 tr>th.left.symbol")))
driver.execute_script("arguments[0].scrollIntoView(true);",show_more_button);
myLength = len(WebDriverWait(driver, 30).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "table.genTbl.openTbl.ecHistoryTbl#eventHistoryTable1155 tr[event_attr_id='1155']"))))
while True:
    try:
        WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div#showMoreHistory1155>a"))).click()
        WebDriverWait(driver, 30).until(lambda driver: len(driver.find_elements(By.CSS_SELECTOR, "table.genTbl.openTbl.ecHistoryTbl#eventHistoryTable1155 tr[event_attr_id='1155']")) > myLength)
        table_rows = driver.find_elements(By.CSS_SELECTOR, "table.genTbl.openTbl.ecHistoryTbl#eventHistoryTable1155 tr[event_attr_id='1155']")
        myLength = len(table_rows)
    except TimeoutException:
        break
for row in table_rows:
    print(row.text)
driver.quit()