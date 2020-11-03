from http import HTTPStatus

from test.base import Base


class TestHealthcheck(Base):
    def test_healthcheck(self):
        assert self.api.is_alive().status_code == HTTPStatus.OK
