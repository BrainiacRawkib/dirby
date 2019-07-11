#!/usr/bin/python

import argparse
import json
import os
import sys
from dirby import Target
from dirby import ScanEngine


def main(prog_args=None):
    parser = argparse.ArgumentParser(
        description="Perform a directory/path discovery of a web server and output to JSON.")
    parser.add_argument("--wordlist", help="path to wordlist file")
    parser.add_argument("--host", help="host or IP to scan")
    parser.add_argument("--port", help="port to scan")
    parser.add_argument("--scheme", help="'http' or 'https' scheme")

    args = parser.parse_args()
    args_dict = vars(args)

    target = Target(args_dict)

    # TODO: make a wordlist loader
    wordlist = ["foo", "bar"]

    scan_engine = ScanEngine(target, wordlist)
    scan_engine.scan()
    scan_engine.print_report()


if __name__ == "__main__":
    main()
