from poetry_package import hello

def test_hello():
    assert hello() == "Hello from package"