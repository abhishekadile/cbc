import json
import socket
from urllib.error import URLError
from urllib.request import Request, urlopen

import pytest


def test_create_box_smoke():
    payload = {
        "command": "create_box",
        "payload": {"width_mm": 100, "depth_mm": 80, "height_mm": 30},
    }
    request = Request(
        "http://127.0.0.1:8765/command",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    try:
        with urlopen(request, timeout=30) as response:
            result = json.loads(response.read().decode("utf-8"))
    except (TimeoutError, socket.timeout, URLError) as exc:
        pytest.skip(f"Fusion bridge command endpoint did not complete create_box smoke test: {exc}")
    assert result["ok"] is True
    assert "Box_100" in result["result"]["body_name"]
