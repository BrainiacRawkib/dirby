#!/usr/bin/env python
import pytest
from dirby.target import Target


class TestTarget():
    def test_creation(self):
        host = 'foo.example.com'
        args = {
            'host': host,
            'port': 443,
            'scheme': 'https'
        }
        target = Target(args)
        assert isinstance(target, Target)
        assert target.scheme == 'https'
        assert target.host == host
        assert target.port == 443
        assert target.url() == "https://foo.example.com:443/"
