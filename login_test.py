from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_login():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://ecommercebs.vercel.app/")
        
        # AI Command: Click Sign In
        driver.execute_script(
            'browserstack_executor: {"action": "aiAuthoring", "arguments": {"objective": "click on Sign In"}}'
        )
        
        # AI Command: Enter username
        driver.execute_script(
            'browserstack_executor: {"action": "aiAuthoring", "arguments": {"objective": "type demouser in username field"}}'
        )
        
        # AI Command: Enter password
        driver.execute_script(
            'browserstack_executor: {"action": "aiAuthoring", "arguments": {"objective": "type testingisfun99 in password field"}}'
        )
        
        # AI Command: Click Login
        driver.execute_script(
            'browserstack_executor: {"action": "aiAuthoring", "arguments": {"objective": "click on Log In"}}'
        )
        
        # Wait for login to complete
        time.sleep(2)
        
        # Verify login
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'demouser')]")))
        
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "passed", "reason": "Login successful"}}'
        )

    except Exception as e:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status": "failed", "reason": "Login failed"}}'
        )
        raise e
    finally:
        driver.quit()
