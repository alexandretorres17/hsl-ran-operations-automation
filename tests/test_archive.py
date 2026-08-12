import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
HSL_FILES = sorted(SCRIPTS.rglob("*.hsl3"))


class ArchiveTests(unittest.TestCase):
    def test_expected_source_set_is_present(self):
        self.assertEqual(23, len(HSL_FILES))
        self.assertEqual(
            {
                "2g-migration",
                "automatic-vpn",
                "baseband-check",
                "clock-status",
                "device-ip-labels",
                "empty-elements",
                "energy-optimisation",
                "nb-iot-preparation",
                "pki-certificate-preparation",
                "site-acceptance",
            },
            {path.parent.name for path in HSL_FILES},
        )

    def test_sources_are_readable_utf8(self):
        for path in HSL_FILES:
            with self.subTest(path=path.relative_to(ROOT)):
                content = path.read_text(encoding="utf-8")
                self.assertTrue(content.strip())
                self.assertNotIn("\ufffd", content)
                self.assertNotRegex(content, r"(?:Ã.|Â.|â€)")

    def test_local_imports_resolve(self):
        pattern = re.compile(r"Import\([\"']([^\"']+)[\"']\)")
        for path in HSL_FILES:
            content = path.read_text(encoding="utf-8")
            for target in pattern.findall(content):
                with self.subTest(path=path.relative_to(ROOT), target=target):
                    self.assertTrue((path.parent / target).is_file())

    def test_no_packaged_or_project_metadata_is_included(self):
        forbidden_suffixes = {".hsp3", ".dsl"}
        for path in ROOT.rglob("*"):
            if path.is_file():
                self.assertNotIn(path.suffix.lower(), forbidden_suffixes)
        self.assertFalse(any("backup" in part.lower() for path in ROOT.rglob("*") for part in path.parts))

    def test_sanitised_network_and_identity_data(self):
        private_ip = re.compile(
            r"\b(?:10\.(?:\d{1,3}\.){2}\d{1,3}|192\.168\.(?:\d{1,3}\.)\d{1,3}|"
            r"172\.(?:1[6-9]|2\d|3[01])\.(?:\d{1,3}\.)\d{1,3})\b"
        )
        email = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.I)
        real_node = re.compile(r"\b(?:GSM\d+[A-Z]?|UMTS\d+[A-Z]?|V\d+H\d+)\b", re.I)
        for path in HSL_FILES:
            content = path.read_text(encoding="utf-8")
            with self.subTest(path=path.relative_to(ROOT)):
                self.assertIsNone(private_ip.search(content))
                self.assertIsNone(real_node.search(content))
                self.assertTrue(all(item.lower().endswith(".invalid") for item in email.findall(content)))

    def test_authors_are_recorded(self):
        authors = (ROOT / "AUTHORS.md").read_text(encoding="utf-8")
        self.assertIn("Alexandre Torres", authors)
        self.assertIn("Luis Reis", authors)


if __name__ == "__main__":
    unittest.main()
