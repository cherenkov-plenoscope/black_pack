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
        os.chdir(tmp)
        rc = subprocess.call(["black-pack"])
        assert rc == 17


def test_check_in_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        stdout = cli_stdout(["black-pack", "check"])
        assert len(stdout)


def test_init_and_check_in_empty_dir():
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        stdout_init = cli_stdout(
            ["black-pack", "init", "--name", "my_package"]
        )
        assert len(stdout_init) == 0

        pkg_dir = os.path.join(tmp, "my_package")
        assert os.path.isdir(pkg_dir)
        os.chdir(pkg_dir)

        stdout_check = cli_stdout(["black-pack", "check"])
        assert len(stdout_check) == 0

        # break .gitignore
        # ----------------
        with open(os.path.join(pkg_dir, ".gitignore"), "wt") as f:
            f.write("not a good gitignore.")

        # assert it is broken
        stdout_check = cli_stdout(["black-pack", "check"])
        assert len(stdout_check) != 0
        assert b"E-1564" in stdout_check

        # repair .gitignore
        stdout_write = cli_stdout(["black-pack", "write", ".gitignore"])
        assert len(stdout_write) == 0

        # check it is fine again
        stdout_check = cli_stdout(["black-pack", "check"])
        assert len(stdout_check) == 0
