#!/usr/bin/env python
import pytest
from dirby.target import Target


class TestTarget():
    def test_creation(self):
        host = 'foo.example.com'
        args = {'host': host}
        target = Target(args)
        assert isinstance(target)
        assert target.scheme == 'https'
        assert target.host == host
        assert target.port == 443
        assert target.url() == "https://foo.example.com:443"
