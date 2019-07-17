import difflib
import glob
import os


def check_test(input_filename):
    d, fname = os.path.split(input_filename)

    suffix = fname[len("input."):]

    try:
        expected = open(f"expected.{suffix}").readlines()
        output = open(f"output.{suffix}").readlines()

        expected = [line.strip()+"\n" for line in expected if line.strip()]
        output = [line.strip()+"\n" for line in output if line.strip()]

        if expected == output:
            return True, ""
        diff = difflib.context_diff(expected, output, fromfile=f"expected.{suffix}", tofile=f"output.{suffix}", n=0)
        with open(f"diff.{suffix}", "w") as fout:
            for line in diff:
                fout.write(line)
        return False, os.path.abspath(f"diff.{suffix}")
    except FileNotFoundError as e:
        print(e)


CSI = "\x1B["
red = CSI + "31m"
green = CSI + "32m"
blue = CSI + "34m"
reset = CSI + "0m"


def check_tests(input_filenames):
    for input_filename in input_filenames:
        passed, diffpath = check_test(input_filename)
        if passed:
            print(rf"{green}[ OK ] {input_filename}{reset}")
        else:
            print(rf"{red}[FAIL] {input_filename}{reset} (diff: file://{diffpath})")


if __name__ == "__main__":
    print(f"Comparing tests for {blue}{os.path.abspath('.')}{reset}")
    check_tests(sorted(glob.glob("input.*")))
