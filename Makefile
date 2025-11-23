# Makefile to ensure venv usage and prefer uv when available.

VENV=.venv
PY=python3
REQ=requirements.txt

.PHONY: venv install update run jupyter clean

venv:
	@if [ ! -d $(VENV) ]; then \
		if command -v uv >/dev/null 2>&1; then \
			echo "[make] Creating venv with uv"; \
			uv venv -p $(PY) $(VENV); \
		else \
			echo "[make] Creating venv with python -m venv"; \
			$(PY) -m venv $(VENV); \
		fi; \
	else \
		echo "[make] Using existing $(VENV)"; \
	fi

install: venv
	@if command -v uv >/dev/null 2>&1; then \
		echo "[make] Installing deps with uv"; \
		. $(VENV)/bin/activate && uv pip install -r $(REQ); \
	else \
		echo "[make] Installing deps with pip"; \
		. $(VENV)/bin/activate && pip install -r $(REQ); \
	fi

update: venv
	@if command -v uv >/dev/null 2>&1; then \
		echo "[make] Upgrading pip/setuptools/wheel with uv"; \
		. $(VENV)/bin/activate && uv pip install --upgrade pip setuptools wheel; \
	fi
	@$(MAKE) install

run: venv
	@. $(VENV)/bin/activate && python -V

jupyter: venv
	@. $(VENV)/bin/activate && jupyter lab

clean:
	rm -rf $(VENV)
