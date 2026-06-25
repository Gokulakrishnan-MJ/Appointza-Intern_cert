# Appointza Internship Certificate Generator

A small **local** web app for creating internship completion certificates.
A developer runs it on their own machine, opens a browser, fills in a form
(intern name, domain, duration, details, etc.), previews the certificate,
and downloads it as a PDF. Nothing is deployed anywhere — it runs entirely
on `localhost`.

## What it does

- Simple web form for the certificate details
- Live PDF preview in the browser
- One-click **Download PDF**
- Uses the Appointza logo from [logo/](logo/) on the certificate

## Requirements

- Python 3.10+ (tested with 3.13). On Windows the `py` launcher is used.

## Quick start (Windows)

Double-click [run.bat](run.bat), or from a terminal:

```bat
run.bat
```

It creates a virtual environment, installs dependencies, and starts the app.
Then open <http://127.0.0.1:5000>.

## Quick start (manual / cross-platform)

```bash
# 1. Create and activate a virtual environment
py -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate     # macOS / Linux

# 2. Install dependencies
python -m pip install -r requirements.txt

# 3. Run the app
python app.py
```

Open <http://127.0.0.1:5000>, fill in the form, click **Preview certificate**,
then **Download PDF**.

## Project layout

| Path | Purpose |
| --- | --- |
| [app.py](app.py) | Flask web server (form + PDF endpoint) |
| [certificate.py](certificate.py) | Builds the certificate PDF with reportlab |
| [templates/index.html](templates/index.html) | The form + preview UI |
| [static/style.css](static/style.css) | Styling |
| [logo/](logo/) | Appointza logo used on the certificate |

## Customizing

- **Logo** — replace the file in [logo/](logo/) (SVG/PNG/JPG). The certificate
  layout reads it automatically.
- **Layout, colors, wording** — edit [certificate.py](certificate.py); the
  brand colors are defined at the top of the file.

## Generate from the command line (optional)

You can also build a certificate without the web UI:

```python
from certificate import CertificateData, build_certificate_pdf

data = CertificateData(
    name="Aarav Sharma",
    domain="Full-Stack Web Development",
    duration="3 Months",
    details="Built and shipped features for the Appointza booking platform.",
    completion_date="June 24, 2026",
)
with open("certificate.pdf", "wb") as f:
    f.write(build_certificate_pdf(data))
```
