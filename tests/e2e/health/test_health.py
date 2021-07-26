import pytest


@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/health/test_1_plus_1/2", 200, {"result": True}),
        ("/health/test/1_plus_1_2", 200, {"result": True}),
        ("/health/test/1_plus/_1_2", 404, None),
    ],
)
def test_get_path(health_client, path, expected_status, expected_response):
    resp = health_client.get(path)
    assert resp.status_code == expected_status
    if resp.status_code == 200:
        assert resp.json() == expected_response
