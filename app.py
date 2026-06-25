"""Local web app for generating Appointza internship certificates.

Run it with:

    py app.py

then open http://127.0.0.1:5000 in your browser, fill in the form,
preview the certificate, and download it as a PDF.
"""

from __future__ import annotations

import re
from datetime import date

from flask import Flask, render_template, request, send_file, abort
import io

from certificate import CertificateData, build_certificate_pdf

app = Flask(__name__)


def _safe_filename(name: str) -> str:
    cleaned = re.sub(r"[^A-Za-z0-9_-]+", "_", (name or "certificate").strip())
    cleaned = cleaned.strip("_")
    return cleaned or "certificate"


@app.route("/")
def index():
    today = date.today().strftime("%B %d, %Y")
    return render_template("index.html", today=today)


@app.route("/generate", methods=["POST"])
def generate():
    name = (request.form.get("name") or "").strip()
    domain = (request.form.get("domain") or "").strip()
    duration = (request.form.get("duration") or "").strip()
    details = (request.form.get("details") or "").strip()
    completion_date = (request.form.get("completion_date") or "").strip()
    company = (request.form.get("company") or "Appointza").strip() or "Appointza"

    if not name or not domain:
        abort(400, "Name and domain are required.")

    if not completion_date:
        completion_date = date.today().strftime("%B %d, %Y")

    data = CertificateData(
        name=name,
        domain=domain,
        duration=duration,
        details=details,
        completion_date=completion_date,
        company=company,
    )

    pdf_bytes = build_certificate_pdf(data)

    download = request.form.get("download") == "1"
    return send_file(
        io.BytesIO(pdf_bytes),
        mimetype="application/pdf",
        as_attachment=download,
        download_name=f"{_safe_filename(name)}_certificate.pdf",
    )


if __name__ == "__main__":
    app.run(debug=True, port=5000)
