import black_pack


def test_has_any_upper():
    assert not black_pack.has_any_upper("")
    assert not black_pack.has_any_upper("abc")
    assert not black_pack.has_any_upper("123")
