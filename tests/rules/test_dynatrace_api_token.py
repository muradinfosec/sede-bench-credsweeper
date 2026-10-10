from typing import List

import pytest

from .common import BaseTestRule


class TestStripeApiKey(BaseTestRule):
    # Example from official site
    # https://www.dynatrace.com/support/help/dynatrace-api/basics/dynatrace-api-authentication/
    @pytest.fixture(

    def lines(self, request) -> List[str]:
        return request.param

    @pytest.fixture
    def rule_name(self) -> str:
        return "Dynatrace API Token"
