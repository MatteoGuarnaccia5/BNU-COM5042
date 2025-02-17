from unittest.mock import patch

import pytest

from smart_home_app.main import SmartHome


@pytest.fixture
def app():
    """Create a new SmartHome instance for each test"""
    return SmartHome()


class TestMainMenu:
    """Test cases for main menu"""

    @patch("builtins.input")
    def test_valid_menu_choice(self, mock_input, app):
        """Test valid menu choice selection"""
        mock_input.side_effect = ["1"]

        with patch.object(app, "login") as mock_login:
            mock_login.side_effect = SystemExit()

            with pytest.raises(SystemExit):
                app.start()

            mock_login.assert_called_once()

    @patch("builtins.input")
    def test_invalid_menu_choice(self, mock_input, app):
        """Test menu choice selection"""
        mock_input.side_effect = ["invalid", "1"]

        with patch.object(app, "login") as mock_login:
            mock_login.side_effect = SystemExit()

            with pytest.raises(SystemExit):
                app.start()

            mock_input.assert_called()
            mock_login.assert_called_once()

    @patch("builtins.input")
    def test_menu_option(self, mock_input, app):
        """Test other menu choice selection"""
        mock_input.side_effect = ["2"]

        with patch.object(app, "sign_up") as mock_login:
            mock_login.side_effect = SystemExit()

            with pytest.raises(SystemExit):
                app.start()

            mock_login.assert_called_once()
