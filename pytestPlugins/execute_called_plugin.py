import pytest


def pytest_addoption(parser):
    parser.addoption("--execute-called", action="store_true", help="Execute called test cases.")


def pytest_collection_modifyitems(config, items):
    if not config.getoption("--execute-called"):
        # Remove test cases marked with the execute_when_called marker
        items[:] = [item for item in items if "execute_when_called" not in item.keywords]


class ExecuteCalledPlugin:
    def pytest_configure(self, config):
        config.addinivalue_line("markers", "execute_when_called: Execute test case only when explicitly called")
