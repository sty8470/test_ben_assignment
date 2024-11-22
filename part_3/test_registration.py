"""
Part 3: Automated Testing Challenge (optional writing the full script)

Scenario:
having the page hosted in this server: http://13.209.85.69/

Task:
Write a script that automates the test for the page hosted above.

Requirements:
pip install pytest selenium

Rum Command:
pytest test_registration.py

Run Command with Report:
pytest test_registration.py -v --html=report.html
"""

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import time

# URL of the application to test
BASE_URL = "http://13.209.85.69/"

@pytest.fixture
def browser():
    """Fixture to initialize and quit the browser."""
    options = Options()
    options.add_argument("--headless")  # Run in headless mode (optional)
    driver = webdriver.Chrome(service=Service("/path/to/chromedriver"), options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_valid_registration(browser):
    """Test case: Valid registration process."""
    browser.get(BASE_URL)

    # Locate form fields and fill them
    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    email = browser.find_element(By.NAME, "email")
    subscribe_checkbox = browser.find_element(By.NAME, "subscribe")
    submit_button = browser.find_element(By.NAME, "submit")

    username.send_keys("testuser")
    password.send_keys("TestPassword123")
    email.send_keys("test@example.com")
    subscribe_checkbox.click()
    submit_button.click()

    # Verify successful registration
    success_message = browser.find_element(By.ID, "success-message")
    assert success_message.text == "Registration successful!"

def test_missing_email(browser):
    """Test case: Registration fails when email is missing."""
    browser.get(BASE_URL)

    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    subscribe_checkbox = browser.find_element(By.NAME, "subscribe")
    submit_button = browser.find_element(By.NAME, "submit")

    username.send_keys("testuser")
    password.send_keys("TestPassword123")
    subscribe_checkbox.click()
    submit_button.click()

    # Verify error message for missing email
    error_message = browser.find_element(By.ID, "error-message")
    assert "Email is required" in error_message.text

def test_invalid_email_format(browser):
    """Test case: Registration fails with an invalid email format."""
    browser.get(BASE_URL)

    username = browser.find_element(By.NAME, "username")
    password = browser.find_element(By.NAME, "password")
    email = browser.find_element(By.NAME, "email")
    subscribe_checkbox = browser.find_element(By.NAME, "subscribe")
    submit_button = browser.find_element(By.NAME, "submit")

    username.send_keys("testuser")
    password.send_keys("TestPassword123")
    email.send_keys("invalid-email")
    subscribe_checkbox.click()
    submit_button.click()

    # Verify error message for invalid email format
    error_message = browser.find_element(By.ID, "error-message")
    assert "Invalid email format" in error_message.text
