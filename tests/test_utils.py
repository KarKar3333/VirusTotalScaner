from utils import base64_url_encode, parse_stats


def test_base64_url_encode():
    url = "https://example.com"
    encoded = base64_url_encode(url)
    assert isinstance(encoded, str)


def test_parse_stats():
    stats = {"malicious": 1, "harmless": 10}
    result = parse_stats(stats)
    assert "Malicious" in result