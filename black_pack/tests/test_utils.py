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


def test_split_comma_with_bracket_balance():
    tokens = black_pack.split_comma_with_bracket_balance("")
    assert len(tokens) == 1
    assert tokens[0] == ""

    tokens = black_pack.split_comma_with_bracket_balance(",")
    assert len(tokens) == 1
    assert tokens[0] == ""

    tokens = black_pack.split_comma_with_bracket_balance("hello")
    assert len(tokens) == 1
    assert tokens[0] == "hello"

    tokens = black_pack.split_comma_with_bracket_balance("abc,def")
    assert len(tokens) == 2
    assert tokens[0] == "abc"
    assert tokens[1] == "def"

    tokens = black_pack.split_comma_with_bracket_balance("key1=value1,\nkey2=value2")
    assert len(tokens) == 2
    assert tokens[0] == "key1=value1"
    assert tokens[1] == "\nkey2=value2"

    tokens = black_pack.split_comma_with_bracket_balance("a,b,c")
    assert len(tokens) == 3
    assert tokens[0] == "a"
    assert tokens[1] == "b"
    assert tokens[2] == "c"

    tokens = black_pack.split_comma_with_bracket_balance("a,b,c,")
    assert len(tokens) == 3
    assert tokens[0] == "a"
    assert tokens[1] == "b"
    assert tokens[2] == "c"


def test_parse_kwargs_of_python_function():
    kwargs = black_pack.parse_kwargs_of_python_function("key=value")
    assert "key" in kwargs
    assert kwargs["key"] == "value"

    kwargs = black_pack.parse_kwargs_of_python_function("ka=va,kb=vb")
    assert "ka" in kwargs
    assert kwargs["ka"] == "va"

    assert "kb" in kwargs
    assert kwargs["kb"] == "vb"

    kwargs = black_pack.parse_kwargs_of_python_function(
        s=(
            'name="a",'
            'version=v,'
            'description=("text goes here"),'
            'long_description=long_description,'
            'long_description_content_type="text/x-rst",'
            'url="https://github.com/abc/a",'
            'author="my name",'
            'author_email="my@mail.net",'
            'packages=["name",],'
            'package_data={"name": [os.path.join("res", "*")]},'
        )
    )
    assert "name" in kwargs
    assert kwargs["name"] == '"a"'

    assert "version" in kwargs
    assert kwargs["version"] == "v"

    assert "description" in kwargs
    assert kwargs["description"] == '("text goes here")'

    assert "long_description" in kwargs
    assert kwargs["long_description"] == "long_description"

    assert "url" in kwargs
    assert kwargs["url"] == '"https://github.com/abc/a"'

    assert "packages" in kwargs
    assert kwargs["packages"] == '["name",]'

    assert "package_data" in kwargs
    assert kwargs["package_data"] == '{"name": [os.path.join("res", "*")]}'


def test_tokenize_restructured_text_image_reference():
    ref = black_pack.tokenize_restructured_text_image_reference(
        txt=(
            ".. |Img| image:: https://my-image.svg"
            "    :target: https://meta-about-my-image.com/my/image"
        )
    )

    assert "key" in ref
    assert ref["key"] == "Img"

    assert "image" in ref
    assert ref["image"] == "https://my-image.svg"

    assert "target" in ref
    assert ref["target"] == "https://meta-about-my-image.com/my/image"
