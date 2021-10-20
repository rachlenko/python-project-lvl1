
build:
	poetry build

publish:
	poetry publish --dry-run

package-install: 
	#python3 -m pip install --user dist/*.whl
	pip install  dist/*.whl

brain-games: 
	poetry run brain-games

brain-even: 
	poetry run brain-even


poetry-dep:
	echo "check if pip installed"
	echo "check if virtualenv installed"
	echo "check if poetry installed "
	echo "activate virtualev with poetry"

lint:
	 poetry run flake8 --ignore=E501 brain_games
phony: brain-games
