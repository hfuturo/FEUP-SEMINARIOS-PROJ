VENV_DIR = .venv

PYTHON = python3

$(VENV_DIR)/bin/activate: requirements.txt
	@echo "Creating virtual environment in $(VENV_DIR)..."
	$(PYTHON) -m venv $(VENV_DIR)
	@echo "Virtual environment created."
	@echo "Upgrading pip to the latest version..."
	$(VENV_DIR)/bin/$(PYTHON) -m pip install --upgrade pip
	@echo "pip upgraded."
	@echo "Installing requirements..."
	$(VENV_DIR)/bin/pip install -r requirements.txt
	@echo "Requirements installed."

clean:
	@echo "Removing virutal environment..."
	rm -rf $(VENV_DIR)

run1:
# 	@echo "Converting exp1.ipynb to exp1.py..."
# 	$(VENV_DIR)/bin/jupyter nbconvert --to script exp1.ipynb --output exp1
# 	@echo "Running exp1.py..."
	$(VENV_DIR)/bin/$(PYTHON) exp1.IPYNB

run2:
	$(VENV_DIR)/bin/$(PYTHON) exp2.IPYNB
