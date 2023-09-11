import black_pack


def test_has_any_upper():
    assert not black_pack.has_any_upper("")
    assert not black_pack.has_any_upper("abc")
    assert not black_pack.has_any_upper("123")
    assert black_pack.has_any_upper("A")
    assert black_pack.has_any_upper("aA")
    assert black_pack.has_any_upper("Aa")
    assert black_pack.has_any_upper("ABC")
    assert black_pack.has_any_upper("awe123ABC")
