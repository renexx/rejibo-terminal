#Author: Rene Bolf
#File: Makefile
#email: xbolfr00@vutbr.cz

VENV := venv

all:
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt
	make venv

venv:
	. $(VENV)/bin/activate
run:venv
	./$(VENV)/bin/python mains.py
clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv runclf clean