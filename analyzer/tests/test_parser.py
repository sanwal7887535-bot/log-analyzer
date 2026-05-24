from analyzer.parser import parse_line


def test_valid_line():
    line = "2024-03-15T14:23:01Z 192.168.1.1 GET /api/users 200 142ms"

    result, status = parse_line(line)

    assert status == "OK"
    assert result["ip"] == "192.168.1.1"


def test_malformed_line():
    line = "INVALID LOG"

    result, status = parse_line(line)

    assert result is None
    assert status == "MALFORMED_LINE"