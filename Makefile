lint:
	@black plugins
	@isort plugins --profile black --line-length 100
	@autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive plugins
	@black dags
	@isort dags --profile black --line-length 100
	@autoflake --in-place --remove-unused-variables --remove-all-unused-imports --recursive dags
