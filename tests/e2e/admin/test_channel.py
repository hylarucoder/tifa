def test_channel_curd(staff_client):
    channel = staff_client.op(
        "/admin/channel/create",
        json={
            "name": "test channel",
            "isActive": True,
            "slug": "test_channel_slug",
            "currencyCode": "usa",
        },
    )
    assert channel["id"]
    assert channel["isActive"]

    channel = staff_client.op(
        "/admin/channel/update",
        json={
            "id": channel["id"],
            "name": "test channel",
            "isActive": False,
            "slug": "test_channel_slug",
            "currencyCode": "usa",
        },
    )
    assert not channel["isActive"]
