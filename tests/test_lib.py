from bbquote.lib import get_quote


def test_get_quote():
    assert get_quote() != ""
