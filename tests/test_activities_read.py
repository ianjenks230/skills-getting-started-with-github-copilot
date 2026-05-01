def test_get_activities_returns_expected_shape(client):
    # Arrange
    required_keys = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert "Chess Club" in payload
    assert "Robotics Club" in payload
    for details in payload.values():
        assert required_keys.issubset(details.keys())
        assert isinstance(details["participants"], list)


def test_get_activities_contains_nine_activities(client):
    # Arrange
    expected_count = 9

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert len(payload) == expected_count
