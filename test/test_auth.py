"""Tests for authentication and user management"""

import pytest

from smart_home_app.main import SmartHome
from smart_home_app.schemas.user import UserSchema


@pytest.fixture
def app():
    """Create a new SmartHome instance for each test"""
    return SmartHome()


class TestAuthentication:
    """Test cases for authentication methods"""

    def test_valid_login(self, app):
        """Test successful login with valid credentials"""
        test_email = "john19@hotmail.com"
        test_password = "password123"

        user_id = app.current_user.authenticate(test_email, test_password)

        user_data = app.current_user.get(user_id)

        assert user_data.email == test_email
        assert user_data.name == "John"

    def test_invalid_login(self, app):
        """Test login with invalid credentials"""
        with pytest.raises(ValueError):
            app.current_user.authenticate("wrong@email.com", "wrongpass")

    def test_user_creation(self, app):
        """Test user creation with valid data"""
        test_user = UserSchema(
            id=1000,
            name="New User Test",
            email="new@example.com",
            password="password123",
            dob=None,
        )

        app.current_user.create(test_user)
        retrieved_user = app.current_user.get(1000)

        assert retrieved_user.name == "New User Test"
        assert retrieved_user.email == "new@example.com"

    def test_get_nonexistent_user(self, app):
        """Test retrieving a user that doesn't exist"""
        with pytest.raises(ValueError):
            app.current_user.get(0)

    def test_create_existing_user(self, app):
        """Test creating a user that already exists"""
        test_user = UserSchema(
            id=1001,
            name="Existing User Test",
            email="john19@hotmail.com",
            password="password123",
            dob=None,
        )

        with pytest.raises(ValueError):
            app.current_user.create(test_user)

    @pytest.fixture(autouse=True)
    def cleanup(self, app):
        """Cleanup test data after each test"""
        yield

        test_email = "new@example.com"
        database = app.current_user._database
        database.data = [user for user in database.data if user["email"] != test_email]
        database.save_data()
