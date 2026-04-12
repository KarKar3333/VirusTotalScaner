from vt_api import get_file_report


def test_get_file_report_invalid():
    result = get_file_report("invalidhash")
    assert result is None or isinstance(result, dict)