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
Part 4: Performance Testing
Scenario: Cloud service for handling up to 10,000 concurrent users.

Plan:
Objectives:

Assess maximum load capacity.
Measure response times under peak load.
Identify potential bottlenecks.
Tools:

Apache JMeter: Chosen for its scalability, support for concurrent user simulations, and wide community support.
Test Cases:

Simulate 10,000 users signing up simultaneously.
Simulate 5,000 concurrent login requests.
Simulate 2,000 users making helper function calls, such as password reset.
Metrics:

Response time.
Throughput (requests per second).
Error rate (percentage of failed requests).
Environment:

Cloud server with auto-scaling enabled.
Network bandwidth of 100 Mbps.
A database configured with a high read/write performance.
Analysis:

Generate detailed graphs and reports for response time and throughput.
Analyze error patterns in the server logs.
Evaluate scalability of the system under various load conditions.
Part 5: Problem-Solving Questions
Scenario 1: Higher Bugs in New Features
Steps to Handle:

Conduct a root cause analysis (RCA) meeting with developers, testers, and product managers to identify gaps.
Review requirements and design documentation for ambiguities.
Compare the test coverage for previous releases versus the current release.
Improve the testing process:
Include more comprehensive unit, integration, and regression tests.
Introduce peer code reviews to catch potential issues early.
Solutions for Future:

Create a checklist for feature completeness before testing begins.
Conduct a knowledge-sharing session to align the understanding of requirements.
Scenario 2: Transition to Automated Testing
Steps to Ensure a Smooth Transition:

Training:

Organize workshops to teach programming basics relevant to test automation.
Introduce team members to automation tools like Selenium or PyTest.
Start Small:

Begin automating repetitive and low-complexity test cases to build confidence.
Collaboration:

Pair experienced developers with testers for mentorship.
Highlight Benefits:

Emphasize faster test cycles and reduced manual effort, freeing time for exploratory testing.
Part 6: Tool Proficiency
Task 1: Bug Report in JIRA
Example JIRA bug report:

Summary: Registration form accepts invalid email.
Description: The registration form does not validate email properly, allowing invalid formats like "user@com".
Steps to Reproduce:
Navigate to the registration page.
Enter an invalid email and submit the form.
Expected Result: Error message for invalid email.
Actual Result: Form accepts invalid email.
Priority: High.
Task 2: Postman Collection
Collection includes CRUD requests:
Create User
Retrieve User
Update User
Delete User
Test scripts validate response status and body:
Example: Ensure 201 Created status for a successful user creation.
