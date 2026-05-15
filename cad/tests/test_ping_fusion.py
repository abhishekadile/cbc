from urllib.request import urlopen


def test_ping_fusion_bridge_responds():
    with urlopen("http://127.0.0.1:8765/health", timeout=5) as response:
        body = response.read().decode("utf-8")
    assert '"ok": true' in body or '"ok":true' in body
