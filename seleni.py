from curses import KEY_NEXT
from encodings import search_function
from sre_constants import ASSERT
from selenium import webdriver 

base_url="https://testautomation-playground.herokuapp.com"
chorom = webdriver.Chrome(executable_path="C:\chromedriver.exe")
#driver.get("https://www.google.com")
#chorom.find_element_by_name("q")
#search_field = chorom.find_element('name','q')
#search_field.send_keys('tiba') 
#search_field.send_keys(Keys.ENTER)
chorom.get(f"{base_url}/forms.html")
chorom.find_element('id','check_python').click()
check1 = chorom.find_element('id','check_validate').text
assert check1 == 'PYTHON'
chorom.find_element('id','notes').send_keys('hello hello')
check2 = chorom.find_element('id','area_notes_validate')
assert check2 =='hello hello'
 