import pytest

"""

Part 1: Test Case Writing
Scenario: A new feature in a web application allows users to register an account. 
The registration form includes fields for username, password, email, and a "Subscribe to newsletter" checkbox.

Task
: Write a set of test cases covering functional, boundary, and edge 
"""

# A mock function simulating the registration process
def register_user(username, password, email, subscribe_to_newsletter):
    """
    Simulates a user registration process. For simplicity, returns a success
    message if all inputs are valid, otherwise raises a ValueError.
    """
    if not username or len(username) < 3 or len(username) > 20:
        raise ValueError("Username must be between 3 and 20 characters.")
    if not password or len(password) < 8 or len(password) > 30:
        raise ValueError("Password must be between 8 and 30 characters.")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format.")
    return {"status": "success", "subscribe": subscribe_to_newsletter}


# Test Cases

# Functional Test Cases
def test_valid_registration():
    """Test valid inputs for the registration process."""
    result = register_user("testuser", "password123", "test@example.com", True)
    assert result["status"] == "success"
    assert result["subscribe"] == True

def test_optional_newsletter_subscription():
    """Test registration without subscribing to the newsletter."""
    result = register_user("testuser", "password123", "test@example.com", False)
    assert result["subscribe"] == False

# Boundary Test Cases
def test_username_min_length():
    """Test username with the minimum allowed length."""
    result = register_user("usr", "password123", "test@example.com", True)
    assert result["status"] == "success"

def test_username_max_length():
    """Test username with the maximum allowed length."""
    result = register_user("a" * 20, "password123", "test@example.com", True)
    assert result["status"] == "success"

def test_password_min_length():
    """Test password with the minimum allowed length."""
    result = register_user("testuser", "pass1234", "test@example.com", True)
    assert result["status"] == "success"

def test_password_max_length():
    """Test password with the maximum allowed length."""
    result = register_user("testuser", "p" * 30, "test@example.com", True)
    assert result["status"] == "success"

# Edge Test Cases
def test_empty_username():
    """Test registration with an empty username."""
    with pytest.raises(ValueError, match="Username must be between 3 and 20 characters."):
        register_user("", "password123", "test@example.com", True)

def test_invalid_email_format():
    """Test registration with an invalid email."""
    with pytest.raises(ValueError, match="Invalid email format."):
        register_user("testuser", "password123", "invalidemail", True)

def test_password_too_short():
    """Test password that is too short."""
    with pytest.raises(ValueError, match="Password must be between 8 and 30 characters."):
        register_user("testuser", "short", "test@example.com", True)

def test_username_with_special_characters():
    """Test username with special characters."""
    with pytest.raises(ValueError, match="Username must be between 3 and 20 characters."):
        register_user("user!@#", "password123", "test@example.com", True)
