"""Check that a public package rejects accidentally copied trial records."""
from contextlib import redirect_stderr, redirect_stdout
import importlib.util
import io
from pathlib import Path
import shutil
import tempfile
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_release", ROOT / "scripts/check_release.py")
release = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(release)


class ReleaseBoundaryTests(unittest.TestCase):
    def test_rejects_trial_record_but_keeps_maintainer_instructions(self):
        with tempfile.TemporaryDirectory(prefix="chef-bob-package-") as temporary:
            package = Path(temporary).resolve() / "package"
            shutil.copytree(ROOT, package, ignore=shutil.ignore_patterns(
                ".git", "__pycache__", ".pytest_cache", ".venv", ".DS_Store"))
            with patch.object(release, "ROOT", package), redirect_stdout(io.StringIO()):
                self.assertTrue((package / "docs/demo.md").is_file())
                self.assertEqual(release.check(), 0)
                record = package / "docs/demo-review/session.json"
                record.parent.mkdir()
                record.write_text('{"messages": ["Synthetic private trial reply"]}\n')
                errors = io.StringIO()
                with redirect_stderr(errors):
                    self.assertEqual(release.check(), 1)
                self.assertIn("local trial data must not enter the public package", errors.getvalue())


if __name__ == "__main__":
    unittest.main()
