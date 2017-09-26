init:
	pip install -r requirements.txt

test:
	nosetests tests

test-single:
	nosetests tests/${ARGS}

test-watch:
	ag -l | entr nosetests tests

test-watch-single:
	ag -l | entr nosetests tests/${ARGS}
