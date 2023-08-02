from helpers import difference


def test_difference_should_raise():
    str1 = "abc"
    str2 = "abcd"

    assert difference(str1, str2) is False


def test_difference_should_pass():
    str1 = "abc"
    str2 = "abc"

    assert difference(str1, str2)
