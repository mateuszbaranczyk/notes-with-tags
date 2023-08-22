import pytest

from tests.conftest import override_get_db


@pytest.fixture
def session():
    return override_get_db
