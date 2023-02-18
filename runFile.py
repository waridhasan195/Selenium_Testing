
from TestFiles.First_Practice import TestCases

print("selenium")
run = TestCases()
run.Land_Page()
run.Radio_Button(radio_option ='radio2')
run.Select_Country_By_Suggession_Class(Country = 'Bangladesh')
run.Dropdown(option = 'option2')
run.Checkbox('option2', 'option3')




