from typing import List

import pytest

from .common import BaseTestRule


class TestSlackToken(BaseTestRule):


    def lines(self, request) -> List[str]:
        return request.param

    @pytest.fixture
    def rule_name(self) -> str:
        return "Slack Webhook"
