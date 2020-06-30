'''
I Need A Vacation (In the US)

Steps:
1) get a list of all US states, display to the user (in a not-ugly manner)
2) let the user pick the state they want to go to
3) dynamically scrape Trip Advisor Top Attractions for that state - Selenium
4) generate a list of the top 10(?)/most popular things to do - pandas
If there is enough time:
5) let the user add what they want to their list of things to do
6) map the locations with distances, display to the user
'''


import us
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys




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
# dynamically scrape Trip Advisor Top Attractions for that state - Selenium
driver = webdriver.Chrome()
driver.get("https://www.tripadvisor.com/Attractions")



