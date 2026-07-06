from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

EMAIL = "kanishka123@gmail.com"

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

try:
    driver.get("https://tichi-app-webapp-stage.web.app")
    print("Application Opened")

    # Click Sign In
    sign_in = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Sign In']")
        )
    )
    sign_in.click()
    print("Sign In Clicked")

    # Enter Email
    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    email.clear()
    email.send_keys(EMAIL)

    # Click Continue
    continue_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Continue']")
        )
    )
    continue_btn.click()
    print("Continue Clicked")

    # Wait for Password field
    password_field = wait.until(
        EC.visibility_of_element_located((By.ID, "password"))
    )

    # Leave Password Empty
    password_field.clear()
    password_field.send_keys(Keys.TAB)

    # Click Login
    login_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Login']")
        )
    )

    login_btn.click()
    print("Login Clicked")

    # Wait for validation message
    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Password')]")
        )
    )

    # Assertion
    assert error_message.is_displayed(), "Password validation message not displayed."

    # Screenshot
    driver.save_screenshot("empty_password.png")
    print("Empty Password Screenshot Saved")

except Exception as e:
    print("Error:", e)
    driver.save_screenshot("error_empty_password.png")

finally:
    print("Closing Browser...")
    driver.quit()