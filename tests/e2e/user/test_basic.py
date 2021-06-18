import pytest
from fastapi.testclient import TestClient

from tifa.app import create_app

app = create_app()

client = TestClient(app)


@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [
        ("/user/path/1_plus_1/2", 200, ""),
        ("/user/path/1_plus_1_2", 200, ""),
    ],
)
def test_get_path(path, expected_status, expected_response):
    response = client.get(path)
    assert response.status_code == expected_status
    # assert response.json() == expected_response


def test_websocket():
    with client.websocket_connect("/user/ws") as websocket:
        data = websocket.receive_json()
        assert data == {"msg": "Hello WebSocket"}
