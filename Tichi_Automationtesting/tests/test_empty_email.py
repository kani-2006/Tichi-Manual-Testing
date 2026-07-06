from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

    # Wait until Email field is visible
    email = wait.until(
        EC.visibility_of_element_located((By.ID, "email"))
    )

    # Leave Email field empty
    email.clear()

    # Click Continue
    continue_btn = wait.until(
        EC.element_to_be_clickable(
            (By.XPATH, "//button[normalize-space()='Continue']")
        )
    )
    continue_btn.click()
    print("Continue Clicked")

    # Wait for validation message
    error_message = wait.until(
        EC.visibility_of_element_located(
            (By.XPATH, "//*[contains(text(),'Email')]")
        )
    )

    # Assertion
    assert error_message.is_displayed(), "Validation message is not displayed."

    # Screenshot
    driver.save_screenshot("empty_email.png")
    print("Empty Email Screenshot Saved")

except Exception as e:
    print("Error:", e)
    driver.save_screenshot("error_empty_email.png")

finally:
    print("Closing Browser...")
    driver.quit()