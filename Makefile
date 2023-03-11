install:
	poetry install 

brain-games:
	poetry run brain-games 

build:
	rm -f dist/*.whl 
	poetry build 

publish:
	poetry publish --dry-run 

package-install:
	python3 -m pip install --force-reinstall --user dist/*.whl

lint:
	poetry run flake8 brain_games 

.PHONY: install brain-games build publish package-install 
