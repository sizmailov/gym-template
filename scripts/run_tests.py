import sys
import subprocess
import glob
import os


def run_tests(input_filenames):
    for input_filename in input_filenames:
        d, fname = os.path.split(input_filename)
        suffix = fname[len("input."):]
        output = open(f"output.{suffix}", "w")
        subprocess.call(sys.argv[1], stdin=open(input_filename), stdout=output)


if __name__ == "__main__":
    print(f"Running tests for {os.path.abspath('.')}")
    run_tests(sorted(glob.glob("input.*")))
