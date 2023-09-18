import black_pack


def test_compare_version_string():
    assert black_pack.compare_version_string_greater_equal("0", "0")
    assert black_pack.compare_version_string_greater_equal("2", "1")
    assert not black_pack.compare_version_string_greater_equal("1", "2")

    assert black_pack.compare_version_string_greater_equal("0.0", "0")
    assert black_pack.compare_version_string_greater_equal("0.0", "0.0")
    assert black_pack.compare_version_string_greater_equal("0.0", "0.0.0")

    assert black_pack.compare_version_string_greater_equal("0.0.1", "0.0.0")
    assert not black_pack.compare_version_string_greater_equal(
        "0.0.0", "0.0.1"
    )

    assert not black_pack.compare_version_string_greater_equal(
        "1.2.3", "1.2.4"
    )
    assert black_pack.compare_version_string_greater_equal("1.2.4", "1.2.3")

    assert black_pack.compare_version_string_greater_equal("1.2.4b", "1.2.4a")
    assert not black_pack.compare_version_string_greater_equal(
        "1.2.4a", "1.2.4b"
    )
