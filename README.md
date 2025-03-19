# Mean Time Failure API

API to compute mean time failures on equipments.

To install the necessary libraries (fastapi and uvicorn):
```bash
pip install uv
uv pip install -r requirements.txt
```

To launch the API (in the local host and port, localhost is 127.0.0.1 and default port is 8000):
```bash
uvicorn main:app --reload --port 5050
```

After installing the libraries and launching the API, you can request the predict endpoint using the requests package.
