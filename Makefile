# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
# Copyright (c) 2014 Mozilla Corporation
#
PACKAGE := dirby

.PHONY:list ## List all make targets
list:
	@echo 'Available make targets:'
	@grep '^[^#[:space:]^\.PHONY.*].*:' Makefile

.PHONY: dependencies ## install all dependencies
dependencies:
	pip3 install -e .
	pip3 install -r requirements.txt

.PHONY: tests ## run all unit tests
tests:
	python3 -m pytest ./tests

clean:
	rm -f dirby/*.pyc tests/*.pyc
	rm -rf .pytest_cache
	rm -rf Makefile_files
	rm -rf build dirby.egg-info
	rm -rf ./tests/__pycache__
