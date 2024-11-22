Brand Engagement Network Inc. - Selection Process Assignment
This repository contains the solutions to the tasks provided for the second step of the selection process for Brand Engagement Network Inc. The tasks are divided into six parts covering test case writing, bug identification, automated testing, performance testing, problem-solving, and tool proficiency.

Table of Contents
Part 1: Test Case Writing
Part 2: Bug Identification and Reporting
Part 3: Automated Testing Challenge
Part 4: Performance Testing
Part 5: Problem-Solving Questions
Part 6: Tool Proficiency
Part 1: Test Case Writing
Scenario: A new feature allows users to register an account through a form with the fields: username, password, email, and a "Subscribe to newsletter" checkbox.

Test Cases:
Functional Test Cases:

Verify that the form successfully submits with valid data.
Verify that an error message appears for invalid email formats.
Ensure the "Subscribe to newsletter" checkbox is optional.
Boundary Test Cases:

Test the username field for its minimum and maximum character limits.
Check if the password field accepts edge values (e.g., shortest valid password).
Edge Test Cases:

Verify behavior when fields are left blank.
Check if duplicate emails trigger an error.
Part 2: Bug Identification and Reporting
Scenario: Testing the web application hosted at http://13.209.85.69/.

Bug Report Example:
Summary: Registration form does not validate email properly.
Steps to Reproduce:
Open http://13.209.85.69/.
Enter an invalid email format (e.g., "user@com").
Submit the form.
Expected Result: Form should display an error message like "Invalid email format."
Actual Result: The form accepts invalid email and proceeds to the next step.
Severity: High
Part 3: Automated Testing Challenge
Scenario: Automate tests for the page hosted at http://13.209.85.69/.

Tools:
Python with Selenium.
Script Example:
Automating the test for form validation:

python
Copy code
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

Apache JMeter: Chosen for its scalability and wide community support.
Test Cases:

Simulate 10,000 users signing up simultaneously.
Simulate 5,000 concurrent login requests.
Simulate 2,000 users making helper function calls.
Metrics:

Response time.
Throughput.
Error rate.
Environment:

Cloud server with auto-scaling enabled.
100 Mbps network bandwidth.
Analysis:

Generate detailed graphs of response time and throughput.
Analyze logs for error patterns or timeouts.
Part 5: Problem-Solving Questions
Scenario 1: Higher Bugs in New Features
Steps to Handle:

Conduct a root cause analysis (RCA) meeting with the team.
Review the requirements and design documentation for ambiguities.
Improve code review and testing processes by adding automated unit tests.
Scenario 2: Transition to Automated Testing
Steps to Ensure a Smooth Transition:

Provide basic programming training to team members.
Start with low-complexity tests for practice.
Highlight benefits such as faster test cycles and reliability.
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
Test scripts validate response status and body.
How to Use
Clone this repository:
bash
Copy code
git clone https://github.com/<your-username>/brand-engagement-network-task.git
Import Postman files:
User CRUD API.postman_collection.json
Local Environment.postman_environment.json
Run scripts in your local environment.
License
This project is open source and licensed under the MIT License.

