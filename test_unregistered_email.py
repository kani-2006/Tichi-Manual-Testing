from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import traceback

EMAIL = "not_registered_12345@gmail.com"

driver = webdriver.Chrome()
driver.maximize_window()

wait = WebDriverWait(driver, 20)

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

    # Enter Unregistered Email
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

    # Verify Sign Up page is displayed
    first_name = wait.until(
        EC.visibility_of_element_located((By.ID, "firstName"))
    )

    assert first_name.is_displayed(), "Sign Up page did not open."

    print("Sign Up Page Displayed Successfully")

    # Screenshot
    driver.save_screenshot("unregistered_email.png")
    print("Screenshot Saved")

except TimeoutException:
    print("Timeout: Expected element was not found.")
    traceback.print_exc()
    driver.save_screenshot("timeout_unregistered_email.png")

except Exception as e:
    print("Test Failed:", e)
    traceback.print_exc()
    driver.save_screenshot("error_unregistered_email.png")

finally:
    print("Closing Browser...")
    driver.quit()