import black_pack
import subprocess
import os
import tempfile


def cli_stdout(cmd):
    p = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    p.wait()
    return p.stdout.read()


def test_no_command():
    with tempfile.TemporaryDirectory() as tmp:
        rc = subprocess.call(["black-pack"])
        assert rc == 17


def test_check_in_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        stdout = cli_stdout(["black-pack", "check", tmp])
        assert len(stdout)


def test_init_and_check_in_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        pkg_dir = os.path.join(tmp, "my_package")

        stdout_init = cli_stdout(["black-pack", "init", pkg_dir])
        assert len(stdout_init) == 0
        assert os.path.isdir(pkg_dir)
        assert os.path.isfile(os.path.join(pkg_dir, "setup.py"))

        stdout_check = cli_stdout(["black-pack", "check", pkg_dir])
        assert len(stdout_check) == 0

        # break .gitignore
        # ----------------
        with open(os.path.join(pkg_dir, ".gitignore"), "wt") as f:
            f.write("not a good gitignore.")

        # assert it is broken
        stdout_check = cli_stdout(["black-pack", "check", pkg_dir])
        assert len(stdout_check) != 0
        assert b"E-1564" in stdout_check

        # repair .gitignore
        stdout_write = cli_stdout(
            ["black-pack", "write", pkg_dir, ".gitignore"]
        )
        assert len(stdout_write) == 0

        # check it is fine again
        stdout_check = cli_stdout(["black-pack", "check", pkg_dir])
        assert len(stdout_check) == 0
