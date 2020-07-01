'''
I Need A Vacation (In the US)

Steps:
1) get a list of all US states, display to the user (in a not-ugly manner)
2) let the user pick the state they want to go to
3) dynamically scrape Trip Advisor Top Attractions for that state
4) generate a list of the top 10(?)/most popular things to do - pandas
If there is enough time:
5) let the user add what they want to their list of things to do
6) map the locations with distances, display to the user
'''


import us
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException




# step 1
# get a list of all US states, display to the user
states = us.states.STATES
states = [state.name for state in states]
states = ', '.join(states)

# step 2
# let the user pick the state they want to go to
print("\nHere is a list of the US states: \n")
print(states)
visit_state = input("\nWhich state would you like to visit: ")

# step 3
# dynamically scrape Trip Advisor Top Attractions for that state
driver = webdriver.Chrome()
driver.get("https://www.tripadvisor.com/Search?q=Oregon&searchSessionId=CAACC22D5A827F2C2C5B482A8BC3987D1593554732925ssid&searchNearby=false&sid=95CFA2941911FF8F49348AE8E406E01C1593554756143&blockRedirect=true")
# find the search bar on the Trip Advisor Attractions page
search_bar = driver.find_element_by_id("mainSearch")
# clear the search bar and enter user input
search_bar.clear()
search_bar.send_keys(visit_state)
# "press enter" and submitting the search
search_bar.send_keys(Keys.RETURN)
# click on the first result, which is the state page (Trip Advisor resets to a general search)
first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]')))
first_result.click()
# click on the "Things to do" tab to get a list of popular activities in the state
try:
    things_to_do_tab = WebDriverWait(driver, 10).until( 
        EC.presence_of_element_located((By.TAG_NAME, '<a class="_1yB-kafB" href="/Attractions-g28958-Activities-Oregon.html" title="Things to Do"><span class="_28xP7Srb"><span class="_1Qo7YQ01">Things to Do</span><span class="KFRgbk1H"><span class="_1nX8jnDZ _2HBN-k68 _3LkX-HIr"></span></span></span></a>')) 
    )
    things_to_do_tab.click()
finally:
    print("done")


