
# Brand Engagement Network Inc. - Selection Process Assignment

This repository contains the solutions to the tasks provided for the second step of the selection process for Brand Engagement Network Inc. The tasks are divided into six parts covering test case writing, bug identification, automated testing, performance testing, problem-solving, and tool proficiency.

---

## Table of Contents

1. [Part 1: Test Case Writing](#part-1-test-case-writing)
2. [Part 2: Bug Identification and Reporting](#part-2-bug-identification-and-reporting)
3. [Part 3: Automated Testing Challenge](#part-3-automated-testing-challenge)
4. [Part 4: Performance Testing](#part-4-performance-testing)
5. [Part 5: Problem-Solving Questions](#part-5-problem-solving-questions)
6. [Part 6: Tool Proficiency](#part-6-tool-proficiency)

---

## Part 1: Test Case Writing

**Scenario**: A new feature allows users to register an account through a form with the fields: username, password, email, and a "Subscribe to newsletter" checkbox.

### Test Cases:
- **Functional Test Cases**:
  1. Verify that the form successfully submits with valid data.
  2. Verify that an error message appears for invalid email formats.
  3. Ensure the "Subscribe to newsletter" checkbox is optional.

- **Boundary Test Cases**:
  1. Test the username field for its minimum and maximum character limits.
  2. Check if the password field accepts edge values (e.g., shortest valid password).

- **Edge Test Cases**:
  1. Verify behavior when fields are left blank.
  2. Check if duplicate emails trigger an error.

---

## Part 2: Bug Identification and Reporting

**Scenario**: Testing the web application hosted at `http://13.209.85.69/`.

### Bug Report Example:
- **Summary**: Registration form does not validate email properly.
- **Steps to Reproduce**:
  1. Open `http://13.209.85.69/`.
  2. Enter an invalid email format (e.g., "user@com").
  3. Submit the form.
- **Expected Result**: Form should display an error message like "Invalid email format."
- **Actual Result**: The form accepts invalid email and proceeds to the next step.
- **Severity**: High

---

## Part 3: Automated Testing Challenge

**Scenario**: Automate tests for the page hosted at `http://13.209.85.69/`.

### Tools:
- Python with Selenium.

### Script Example:
Automating the test for form validation:
```python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://13.209.85.69/")

# Enter invalid email
email_input = driver.find_element(By.ID, "email")
email_input.send_keys("invalid_email")
email_input.send_keys(Keys.RETURN)

# Check for error message
error_message = driver.find_element(By.CLASS_NAME, "error")
assert "Invalid email format" in error_message.text

driver.quit()
