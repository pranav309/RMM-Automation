import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers", "execute_when_called: Execute test case only when explicitly called"
    )
