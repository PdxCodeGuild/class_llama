'''
I REALLY Need A Vacation (In the US)

Steps:
1) get a list of all US states, display to the user
2) let the user pick the state they want to go to
3) scrape Trip Advisor Top Attractions for that state
4) generate a list of the top 10(?)/most popular things to do - pandas
If there is enough time:
5) let the user add what they want to their list of things to do
6) map the locations with distances, display to the user
'''


import us
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# go back to Beautifulsoup?




# step 1
# get a list of all US states, display to the user
states = us.states.STATES
states = [state.name for state in states]
states = ', '.join(states)

# step 2
# let the user pick the state they want to go to
print("\nHere is a list of the US states: \n")
print(states)
visit_state = input("\nWhich state would you like to visit (capitalize the state or use the capitalized two-letter abbreviation): ")

# step 3
# scrape Trip Advisor Top Attractions for that state
driver = webdriver.Chrome()
if visit_state in ["Alabama","AL"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28922-Activities-Alabama.html")
elif visit_state in ["Alaska","AK"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28923-Activities-Alaska.html")
elif visit_state in ["Arizona","AZ"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28924-Activities-Arizona.html")
elif visit_state in ["Arkansas","AR"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28925-Activities-Arkansas.html")
elif visit_state in ["California","CA"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28926-Activities-California.html")
elif visit_state in ["Colorado","CO"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28927-Activities-Colorado.html")
elif visit_state in ["Connecticut","CT"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28928-Activities-Connecticut.html")
elif visit_state in ["Delaware","DE"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28929-Activities-Delaware.html")
elif visit_state in ["Florida","FL"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28930-Activities-Florida.html")
elif visit_state in ["Georgia","GA"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28931-Activities-Georgia.html")
elif visit_state in ["Hawaii","HI"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28932-Activities-Hawaii.html")
elif visit_state in ["Idaho","ID"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28933-Activities-Idaho.html")
elif visit_state in ["Illinois","IL"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28934-Activities-Illinois.html")
elif visit_state in ["Indiana","IN"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28935-Activities-Indiana.html")
elif visit_state in ["Iowa","IA"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28936-Activities-Iowa.html")
elif visit_state in ["Kansas","KS"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28937-Activities-Kansas.html")
elif visit_state in ["Kentucky","KY"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28938-Activities-Kentucky.html")
elif visit_state in ["Louisiana","LA"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28939-Activities-Louisiana.html")
elif visit_state in ["Maine","ME"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28940-Activities-Maine.html")
elif visit_state in ["Maryland","MD"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28941-Activities-Maryland.html")
elif visit_state in ["Massachusetts","MA"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28942-Activities-Massachusetts.html")
elif visit_state in ["Michigan","MI"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28943-Activities-Michigan.html")
elif visit_state in ["Minnesota","MN"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28944-Activities-Minnesota.html")
elif visit_state in ["Mississippi","MS"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28945-Activities-Mississippi.html")
elif visit_state in ["Missouri","MO"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28946-Activities-Missouri.html")
elif visit_state in ["Montana","MT"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28947-Activities-Montana.html")
elif visit_state in ["Nebraska","NE"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28948-Activities-Nebraska.html")
elif visit_state in ["Nevada","NV"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28949-Activities-Nevada.html")
elif visit_state in ["New Hampshire","NH"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28950-Activities-New_Hampshire.html")
elif visit_state in ["New Jersey","NJ"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28951-Activities-New_Jersey.html")
elif visit_state in ["New Mexico","NM"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28952-Activities-New_Mexico.html")
elif visit_state in ["New York","NY"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28953-Activities-New_York.html")
elif visit_state in ["North Carolina","NC"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28954-Activities-North_Carolina.html")
elif visit_state in ["North Dakota","ND"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28955-Activities-North_Dakota.html")
elif visit_state in ["Ohio","OH"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28956-Activities-Ohio.html")
elif visit_state in ["Oklahoma","OK"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28957-Activities-Oklahoma.html")
elif visit_state in ["Oregon","OR"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28958-Activities-Oregon.html")
elif visit_state in ["Pennsyvania","PA"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28959-Activities-Pennsylvania.html")
elif visit_state in ["Rhode Island","RI"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28960-Activities-Rhode_Island.html")
elif visit_state in ["South Carolina","SC"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28961-Activities-South_Carolina.html")
elif visit_state in ["South Dakota","SD"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28962-Activities-South_Dakota.html")
elif visit_state in ["Tennessee","TN"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28963-Activities-Tennessee.html")
elif visit_state in ["Texas","TX"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28964-Activities-Texas.html")
elif visit_state in ["Utah","UT"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28965-Activities-Utah.html")
elif visit_state in ["Vermont","VT"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28966-Activities-Vermont.html")
elif visit_state in ["Virginia","VA"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28967-Activities-Virginia.html")
elif visit_state in ["Washington","WA"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28968-Activities-Washington.html")
elif visit_state in ["West Virginia","WV"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28971-Activities-West_Virginia.html")
elif visit_state in ["Wisconsin","WI"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28972-Activities-Wisconsin.html")
elif visit_state in ["Wyoming","WY"]:
    driver.get("https://www.tripadvisor.com/Attractions-g28973-Activities-Wyoming.html")


# Here is the pretty version of searching for things to do based off the user's state selection:
# driver = webdriver.Chrome()
# driver.get("https://www.tripadvisor.com/Search?q=Oregon&searchSessionId=CAACC22D5A827F2C2C5B482A8BC3987D1593554732925ssid&searchNearby=false&sid=95CFA2941911FF8F49348AE8E406E01C1593554756143&blockRedirect=true")
# search_bar = driver.find_element_by_id("mainSearch")
# search_bar.clear()
# search_bar.send_keys(visit_state)
# search_bar.send_keys(Keys.RETURN)
# first_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="BODY_BLOCK_JQUERY_REFLOW"]/div[2]/div/div[2]/div/div/div/div/div[1]/div/div[1]/div/div[3]/div/div[1]/div/div[2]/div/div/div/div/div/div/div[2]')))
# first_result.click()
# state_dropdown = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="component_7"]/div/div[2]/header/div/nav/a[1]')))
# state_dropdown.click()
# things_to_do_tab = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH, '//*[@id="lithium-root"]/main/div[6]/div/div/div/div[2]/span/div/div/div[1]/a[7]')))
# things_to_do_tab.click()


