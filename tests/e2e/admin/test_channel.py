def test_channel_curd(staff_client):
    res = staff_client.post(
        "/admin/channel/create",
        data={
            "name": "test channel",
            "is_active": True,
            "slug": "test_channel_slug",
            "currency_code": "usa",
        }
    )
    channel_id = res.json()["item"]["id"]
    assert channel_id
