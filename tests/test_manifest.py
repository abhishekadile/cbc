from cbc_scanner.acquisition.manifest import generate_initial_manifest

def test_manifest():
    m = generate_initial_manifest("scan_123", "demo_pi_only", "imx296")
    assert m["scan_id"] == "scan_123"
    assert "created_at" in m
    assert m["images"] == []
