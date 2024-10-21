from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

# Wait until the Google search bar (input element) is loaded
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "q"))
)

# Keep the browser open for a while (or interact with it)
input("Press Enter to close the browser...")

# Close the browser
driver.quit()