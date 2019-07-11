#!/usr/bin/env python
import pytest
from dirby.scan_engine import ScanEngine
from dirby.target import Target


class TestScanEngine():
    def test_creation(self):
        host = 'foo.example.com'
        args = {
            'host': host,
            'port': 443,
            'scheme': 'https'
        }
        target = Target(args)
        wordlist = ['a', 'b', 'c']

        scan_engine = ScanEngine(target, wordlist)
        assert isinstance(scan_engine, ScanEngine)
