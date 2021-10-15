# (U.U)

SRC = main.py
PYTHON = python3
UTILS = utils/

run:
	$(PYTHON) $(SRC)

unify: 
	$(PYTHON) $(UTILS)unify.py single-header/tinyengine.py

clean:
	rm -rf __pycache__