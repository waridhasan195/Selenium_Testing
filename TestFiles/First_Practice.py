

import sys
sys.path.append('D:\\New_Start\\Selenium\\Selenium_Testing')

from Contstans_Material.Contstant import Base_URL

import selenium
from selenium import webdriver
import os


class TestCases(webdriver.Chrome):
    def __init__(self, driver_path = "D:/New_Start/Selenium/Selenium_Testing/Drivers/chromedriver_win32/chromedriver.exe"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(TestCases, self).__init__(options=options)
        self.implicitly_wait(40)
        self.maximize_window()
        print("Setup Complete")
        

    def Land_Page(self):
        self.get(Base_URL)
        print("Browser")
        


        
        
        

        




    