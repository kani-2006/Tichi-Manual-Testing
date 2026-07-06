from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import traceback
import time

EMAIL = "kanishka123@gmail.com"
PASSWORD = "Kanishka@123456789"

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

    # Wait for Password field
    password = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    password.clear()
    password.send_keys(PASSWORD)
    print("Password Entered")

    # Click Login / Sign In
    login = wait.until(
    EC.element_to_be_clickable(
        (By.XPATH, "//button[@type='submit']")
    )
)

    login.click()
    print("Login Clicked")

    time.sleep(5)

    driver.save_screenshot("valid_login_success.png")
    print("Valid Login Successful")

except TimeoutException:
    print("Timeout: Password page did not appear.")
    traceback.print_exc()
    driver.save_screenshot("timeout_error.png")

except Exception as e:
    print("Test Failed:", e)
    traceback.print_exc()
    driver.save_screenshot("valid_login_error.png")

finally:
    print("Closing Browser...")
    driver.quit()