

import sys
sys.path.append('D:\\New_Start\\Selenium\\Selenium_Testing')

from Contstans_Material.Contstant import Base_URL

import time
import selenium
from selenium import webdriver
import os
from selenium.webdriver.common.by import By


class TestCases(webdriver.Chrome):
    def __init__(self, driver_path = "D:/New_Start/Selenium/Selenium_Testing/Drivers/chromedriver_win32/chromedriver.exe"):
        self.driver_path = driver_path
        os.environ['PATH'] += self.driver_path
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        super(TestCases, self).__init__(options=options)
        self.implicitly_wait(40)
        self.maximize_window()
        print("Setup Complete.")
        

    def Land_Page(self):
        self.get(Base_URL)
        print("Browser Open.")
        title = self.title
        print("Title: ", title)
    
    def Radio_Button(self, radio_option):
        try:
            Radio_element = self.find_element(By.XPATH, f"//input[@value='{radio_option}']")
            Radio_element.click()
            print(f"Radio Option {radio_option} Clicked")
            Radio_Value = Radio_element.get_attribute('value')
            print(Radio_Value)
        except:
            print("Radio Option Face Problems, Please Check it out.")


    def Select_Country_By_Suggession_Class(self, Country):
        Suggession_Field = self.find_element(By.XPATH, "//input[@id='autocomplete']")
        Suggession_Field.clear()
        Suggession_Field.send_keys(Country)
        time.sleep(10)
        Suggession_Country = self.find_elements(By.XPATH, "//ul[@id='ui-id-1']/li/div")

        for country in Suggession_Country:
            a = country.get_attribute('innerHTML')
            try:
                if a == Country:
                    country.click()
                    print(f"{a} Clicked")
                else:
                    print("Search Again")
            except:
                print("No Country Found.")

            time.sleep(5)
        
    def Dropdown(self, option):
        Dropdown_field = self.find_element(By.XPATH, "//select[@id='dropdown-class-example']")
        Dropdown_field.click()
        print("Option Area Clicked")
        time.sleep(2)

        try:
            Dropdown_options = self.find_element(By.XPATH, f"//option[@value='{option}']")
            Dropdown_options.click()
            print(f"{option} Clicked.")
        except:
            print("Dropdown Option Not Valid Please Fix it.")
        time.sleep(5)

    def Checkbox(self, *checkbox_options):
        print("\nWorking on Multiple choice: ")

        Checkbox_Fields = self.find_elements(By.XPATH, '//input[@type="checkbox"]')

        for check_option in checkbox_options:
            for Checkbox in Checkbox_Fields:
                a = Checkbox.get_attribute('value')

                if a == check_option:
                    selected_option = self.find_element(By.XPATH, f'//input[@value="{check_option}"]')
                    selected_option.click()
                    dd = selected_option.get_attribute('value')
                    print(f"{dd} clicked.",)

        time.sleep(15)

    def PopUp(self, popup_value):

        popup_name = self.find_element(By.XPATH, "//input[@id='name']")
        popup_name.clear()
        popup_name.send_keys(popup_value)
        confirm_popup = self.find_element(By.XPATH, "//input[@id='confirmbtn']")
        confirm_popup.click()
        time.sleep(5)
        assert 'Warid' == popup_value, f"{popup_value}, Should be Warid"
        popup_message = self.switch_to.alert
        popup_message.accept("Accepted.")
        
        time.sleep(5)






        



        
        



        
        



        


        
        
        

        




    