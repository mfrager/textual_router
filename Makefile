checks:
	@poetry run ruff check
	@poetry run ruff format
	@poetry run isort .
	@poetry run mypy .
	@poetry run interrogate -v
	@poetry run pytest