import copy

import pytest
from fastapi.testclient import TestClient

from src.app import activities, app

_INITIAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities_state():
    # Arrange
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))

    yield

    # Assert cleanup
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture()
def client():
    # Arrange
    test_client = TestClient(app)

    # Act
    return test_client
