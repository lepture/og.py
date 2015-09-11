coverage:
	@rm -f .coverage
	@nosetests --with-coverage --cover-package=og --cover-html
