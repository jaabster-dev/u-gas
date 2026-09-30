#!/usr/bin/env python3
from __future__ import annotations
import importlib.util, pathlib, subprocess, sys, tempfile, unittest

ROOT = pathlib.Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("repository_health", ROOT / "scripts" / "check_repository_health.py")
health = importlib.util.module_from_spec(spec); assert spec.loader is not None
sys.modules["repository_health"] = health; spec.loader.exec_module(health)

def git(repo, *args):
    subprocess.run(["git","-C",str(repo),*args], check=True, capture_output=True, text=True)

class RepositoryHealthTests(unittest.TestCase):
    def repo(self):
        td=tempfile.TemporaryDirectory(); p=pathlib.Path(td.name)
        git(p,"init","-b","main"); git(p,"config","user.email","test@example.com"); git(p,"config","user.name","Test")
        (p/"x").write_text("a"); git(p,"add","x"); git(p,"commit","-m","base")
        return td,p

    def test_authority_only_is_green(self):
        td,p=self.repo(); self.addCleanup(td.cleanup)
        self.assertEqual(health.evaluate(p,"main").status,"GREEN")

    def test_authority_ahead_of_release_is_green(self):
        td,p=self.repo(); self.addCleanup(td.cleanup)
        git(p,"branch","release"); (p/"x").write_text("b"); git(p,"commit","-am","work")
        r=health.evaluate(p,"main","release")
        self.assertEqual((r.status,r.authority_ahead,r.release_ahead),("GREEN",1,0))

    def test_release_unique_commit_is_red(self):
        td,p=self.repo(); self.addCleanup(td.cleanup)
        git(p,"branch","release"); git(p,"checkout","release"); (p/"y").write_text("release"); git(p,"add","y"); git(p,"commit","-m","release unique"); git(p,"checkout","main")
        r=health.evaluate(p,"main","release")
        self.assertEqual(r.status,"RED"); self.assertEqual(r.release_ahead,1)

    def test_missing_ref_is_visible_error(self):
        td,p=self.repo(); self.addCleanup(td.cleanup)
        self.assertEqual(health.evaluate(p,"missing").status,"ERROR")

if __name__ == "__main__":
    unittest.main()
