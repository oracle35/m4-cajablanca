# M4 Pruebas de Caja Blanca

## TC3004B

### How to execute the project

Since this project uses an external library (Pytest), you will need to create a virtual environment in order to install the required dependencies.

For this, feel free to use one of the following commands.

```bash
uv venv
python3 -m venv .
python -m venv .
```

After that, you can initialize your virtual environment using the following command:
```bash
source .venv/bin/activate
```

Once that is set, you will need to install the required dependencies.

```bash
uv pip install -r requirements.txt
pip install -r requirements.txt
```

Finally, feel free to use any of the next commands:

```bash
pytest
pytest --cov=.
```
