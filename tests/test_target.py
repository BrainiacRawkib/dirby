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
        assert target.valid() == True

    def test_invalid_port(self):
        host = 'foo.example.com'
        args = {
            'host': host,
            'port': 65536,
            'scheme': 'https'
        }
        target = Target(args)
        assert isinstance(target, Target)
        assert target.valid() == False

    def test_invalid_scheme(self):
        host = 'foo.example.com'
        args = {
            'host': host,
            'port': 443,
            'scheme': 'hello'
        }
        target = Target(args)
        assert isinstance(target, Target)
        assert target.valid() == False
