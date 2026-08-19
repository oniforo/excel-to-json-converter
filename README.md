# Excel to JSON Converter

[![Build Status](https://img.shields.io/github/actions/workflow/status/oniforo/excel-to-json-converter/pylint.yml?style=flat-square)](https://github.com/oniforo/excel-to-json-converter/actions)
[![License](https://img.shields.io/github/license/oniforo/excel-to-json-converter?style=flat-square)](https://github.com/oniforo/excel-to-json-converter/blob/main/LICENSE)

A small Flask web app that converts an uploaded `.xlsx` spreadsheet into JSON. Upload a file through the browser and get back its rows as a JSON array of records.

## How it works

- `GET /` renders an upload form (`templates/upload.html`).
- `POST /upload` accepts a multipart file upload, reads it with `pandas.read_excel`, and returns the sheet as JSON (`orient="records"`). Files that don't end in `.xlsx` are rejected with an error response.

## Requirements

- Python 3.8, 3.9, or 3.10 (tested versions, see the [Pylint workflow](.github/workflows/pylint.yml))
- Dependencies listed in `requirements.txt` (Flask, pandas, openpyxl, python-dotenv, and their transitive dependencies)

## Setup

1. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. (Optional) Set the port via a `.env` file:
   ```
   PORT=8000
   ```

## Running

```bash
python main.py
```

The app listens on `0.0.0.0`, using the `PORT` environment variable if set (defaults to `8080`). Open `http://localhost:<port>` in a browser and upload an `.xlsx` file.

### Running with Docker

```bash
docker build -t excel-to-json-converter .
docker run -p 8080:8080 excel-to-json-converter
```

## Project structure

```
main.py              Flask app: routes and Excel-to-JSON conversion
templates/upload.html Upload form
static/upload.css     Page styling
static/upload.png     Upload icon
requirements.txt      Python dependencies
Dockerfile            Container build definition
```
