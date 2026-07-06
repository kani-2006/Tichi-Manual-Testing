from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import traceback
import time

EMAIL = "kanishka123@gmail.com"

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 30)

try:
    print("Opening Application...")
    driver.get("https://tichi-app-webapp-stage.web.app")

    # Click Sign In
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Sign In']")
        )
    ).click()
    print("Sign In Clicked")

    # Enter Email
    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )
    email.clear()
    email.send_keys(EMAIL)
    print("Email Entered")

    # Click Continue
    wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Continue']")
        )
    ).click()
    print("Continue Clicked")

    # First Name
    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )
    first_name.clear()
    first_name.send_keys("Kanishka")
    print("First Name Entered")

    # Last Name
    last_name = wait.until(
        EC.visibility_of_element_located((By.ID, "lastName"))
    )
    last_name.clear()
    last_name.send_keys("KV")
    print("Last Name Entered")

    # Phone Number
    phone = wait.until(
        EC.visibility_of_element_located((By.ID, "phoneNumber"))
    )
    phone.clear()
    phone.send_keys("9876543210")
    print("Phone Number Entered")

    # Password
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )
    password.clear()
    password.send_keys("Kanishka@123456789")
    print("Password Entered")

    # Confirm Password
    confirm = wait.until(
        EC.visibility_of_element_located((By.ID, "confirmPassword"))
    )
    confirm.clear()
    confirm.send_keys("Kanishka@123456789")
    print("Confirm Password Entered")

    # Accept Terms & Conditions
    checkbox = wait.until(
    EC.presence_of_element_located((By.ID, "remember"))
    )

    driver.execute_script("arguments[0].scrollIntoView(true);", checkbox)
    driver.execute_script("arguments[0].focus();", checkbox)
    driver.execute_script("arguments[0].click();", checkbox)

    print("Terms and Conditions Accepted")
    # Click Sign Up
    signup = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Sign Up']")
        )
    )
    signup.click()
    print("Sign Up Clicked")

    time.sleep(3)

    driver.save_screenshot("signup_success.png")
    print("Sign Up Completed Successfully")

except TimeoutException:
    print("Timeout: Element not found.")
    traceback.print_exc()
    driver.save_screenshot("timeout_error.png")

except Exception as e:
    print("Test Failed:", e)
    traceback.print_exc()
    driver.save_screenshot("signup_error.png")

finally:
    print("Closing Browser...")
    driver.quit()