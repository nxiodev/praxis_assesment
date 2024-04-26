ambiente:
	@echo "Creando ambiente virtual"
	python3 -m venv venv
	@echo "Activando ambiente virtual"
	source venv/bin/activate
	@echo "Instalando requerimientos"
	pip install -r requirements.txt

formateo:
	@echo "Starting autoflake format"
	autoflake --recursive motor adaptadores
	@echo "Starting isort format..."
	isort motor adaptadores
	@echo "Starting black format..."
	black motor adaptadores
	@echo "Starting pylint"
	pylint motor adaptadores