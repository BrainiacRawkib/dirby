#!/usr/bin/python

import argparse
import sys

from dirby.target import Target
from dirby.scan_engine import ScanEngine


def main(prog_args=None):
    example_text = '''example usage:

     python ./dirby.py --scheme https --host blog.rubidus.com --port 443 --wordlist ./wordlists/small.txt'''

    parser = argparse.ArgumentParser(
        description="Perform a directory/path discovery of a web server and output to JSON.",
        epilog=example_text)
    parser.add_argument("--wordlist", help="path to wordlist file")
    parser.add_argument("--host", help="host or IP to scan")
    parser.add_argument("--port", help="port to scan")
    parser.add_argument("--scheme", help="'http' or 'https' scheme")

    args = parser.parse_args()
    args_dict = vars(args)

    target = Target(args_dict)

    if target.valid() == False:
        print("Invalid target specified")
        exit(1)

    # TODO: make a wordlist loader
    # wordlist = ["foo", "bar"]
    f = open(args.wordlist, "r")
    words = list(f)

    try:
        scan_engine = ScanEngine(target, words)
        scan_engine.scan()
        scan_engine.print_report()
    except Exception as e:
        sys.exit(1)
    f.close()


if __name__ == "__main__":
    main()
