import pytest

@pytest.fixture(params=["chrome", "firefox", "safari"])
def browser(request):
    return request.param

def test_browser(browser):
    assert browser in ["chrome", "firefox", "safari"]