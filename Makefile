.PHONY: test
test:
	python -m pytest --junitxml results.xml test/

.PHONY: lint
lint:
	python -m pylint main.py src/

.PHONY: analyze
analyze:
	python -m mypy --ignore-missing-imports main.py src/

.PHONY: clean
clean:
	python -m pyclean .
	rm -rf .mypy_cache
	rm -rf .pytest_cache
	rm -f results.xml
