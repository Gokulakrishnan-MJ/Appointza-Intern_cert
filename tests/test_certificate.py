"""Basic smoke tests for the certificate generator."""

import os
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from certificate import CertificateData, build_certificate_pdf  # noqa: E402


class CertificateTests(unittest.TestCase):
    def test_returns_pdf_bytes(self):
        data = CertificateData(
            name="Aarav Sharma",
            domain="Full-Stack Web Development",
            duration="3 Months",
            details="Built and shipped features for the Appointza booking platform.",
            completion_date="June 24, 2026",
        )
        pdf = build_certificate_pdf(data)
        self.assertIsInstance(pdf, bytes)
        self.assertTrue(pdf.startswith(b"%PDF"), "output should be a PDF")
        self.assertGreater(len(pdf), 1000)

    def test_minimal_required_fields(self):
        data = CertificateData(name="Test User", domain="QA", duration="")
        pdf = build_certificate_pdf(data)
        self.assertTrue(pdf.startswith(b"%PDF"))


if __name__ == "__main__":
    unittest.main()
