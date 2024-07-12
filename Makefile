.PHONY: docs


install:
	pip install -e .[test]

clean:
	rm -rf src/commercetools/platform/
	rm -rf src/commercetools/importapi/
	rm -rf src/commercetools/frontend/
	rm -rf src/commercetools/checkout/
	rm -rf src/commercetools/history/
	rm -rf src/commercetools/connect/
	rm -rf src/commercetools/ml/

generate: clean
	java -jar ../rmf-codegen/rmf-codegen.jar generate -v ../commercetools-api-reference/api-specs/api/api.raml -o src/commercetools/platform/ -t PYTHON_CLIENT 
	java -jar ../rmf-codegen/rmf-codegen.jar generate -v ../commercetools-api-reference/api-specs/import/api.raml -o src/commercetools/importapi/ -t PYTHON_CLIENT 
	java -jar ../rmf-codegen/rmf-codegen.jar generate -v ../commercetools-api-reference/api-specs/frontend-api/api.raml -o src/commercetools/frontend/ -t PYTHON_CLIENT 
	java -jar ../rmf-codegen/rmf-codegen.jar generate -v ../commercetools-api-reference/api-specs/checkout/api.raml -o src/commercetools/checkout/ -t PYTHON_CLIENT 
	java -jar ../rmf-codegen/rmf-codegen.jar generate -v ../commercetools-api-reference/api-specs/history/api.raml -o src/commercetools/history/ -t PYTHON_CLIENT
	java -jar ../rmf-codegen/rmf-codegen.jar generate -v ../commercetools-api-reference/api-specs/connect/api.raml -o src/commercetools/connect/ -t PYTHON_CLIENT
	find src/ -name "gen.properties" -delete
	isort src/commercetools/
	black src/commercetools/

test:
	pytest tests/

mypy:
	 mypy --config-file=mypy.ini src/commercetools

coverage:
	pytest --cov=commercetools

runserver:
	python -mcommercetools.testing.server

format:
	isort src tests
	black src/ tests/

release:
	pip install twine wheel
	rm -rf build/* dist/*
	python setup.py sdist bdist_wheel
	twine upload dist/*

docs:
	make -C docs html
