
build
	poetry build

publish
	poetry publish --dry-run

package-install 
	#python3 -m pip install --user dist/*.whl
	pip install  dist/*.whl
phony: brain-games
