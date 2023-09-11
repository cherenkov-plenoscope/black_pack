import python_package_linter
import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        prog="black-pack",
        description="Lint the structure of your python-package.",
    )
    parser.add_argument(
        "path",
        metavar="PATH",
        type=str,
        help=("PATH to your python-package."),
    )
    args = parser.parse_args()

    python_package_linter.check_package(pkg_dir=args.path)


if __name__ == "__main__":
    main()
