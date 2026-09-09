from employee import is_valid_email


def test_valid_email():
    assert is_valid_email("test@gmail.com") is True


def test_invalid_email():
    assert is_valid_email("test") is False


def test_email_without_domain():
    assert is_valid_email("test@") is False


def test_email_without_username():
    assert is_valid_email("@gmail.com") is False


def test_email_without_dot():
    assert is_valid_email("test@gmailcom") is False