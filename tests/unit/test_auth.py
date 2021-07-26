from tifa.auth import decode_jwt, gen_jwt


def test_jwt():
    token = gen_jwt("staff:1", 30)
    payload = decode_jwt(token)
    assert payload["sub"] == "staff:1"
