"""Test cases for menu options"""

from unittest.mock import patch

import pytest

from smart_home_app.main import SmartHome


@pytest.fixture
def app():
    """Create a new SmartHome instance for each test"""
    return SmartHome()


class TestMenuOptions:
    """Test cases for menu options"""

    @patch("builtins.input")
    def test_send_alert(self, mock_input, app):
        """Test sending emergency alert"""
        mock_input.side_effect = ["1"]

        with patch.object(app, "send_alert") as mock_alert:
            mock_alert.side_effect = SystemExit()

            with pytest.raises(SystemExit):
                app.main()

            mock_alert.assert_called_once()

    @patch("builtins.input")
    def test_energy_efficiency(self, mock_input, app):
        """Test energy efficiency menu option"""
        mock_input.side_effect = ["2"]

        with patch.object(app, "pick_appliance") as mock_appliance:
            mock_appliance.side_effect = SystemExit()

            with pytest.raises(SystemExit):
                app.main()

            mock_appliance.assert_called_once()

    @patch("builtins.input")
    def test_invalid_input(self, mock_input, app):
        """Test invalid input"""
        mock_input.side_effect = ["invalid", "1"]

        with patch.object(app, "main") as mock_main:
            mock_main.side_effect = SystemExit()

            with pytest.raises(SystemExit):
                app.main()

            mock_main.assert_called_once()
