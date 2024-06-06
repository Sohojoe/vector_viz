import pytest
from hello_world import HelloWorld


def test_hello_world(capsys):
    hw = HelloWorld()
    hw.say_hello()
    captured = capsys.readouterr()
    assert captured.out == "Hello, World!\n"
    assert captured.err == ""