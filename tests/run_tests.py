import os
import subprocess
import sys

TEST_DIR = "tests"


def run_test(file_path):
    base = file_path.replace(".tk", "")
    expected_file = base + ".expected"
    error_file = base + ".error"
    stdin_file = base + ".stdin"
    stdin_data = None

    if os.path.exists(stdin_file):
        with open(stdin_file, encoding="utf-8") as f:
            stdin_data = f.read()

    result = subprocess.run(
        [sys.executable, "-m", "cli.tk", file_path],
        input=stdin_data,
        capture_output=True,
        text=True,
    )

    output = result.stdout.strip()
    error = result.stderr.strip()

    expects_error = os.path.exists(error_file)
    if expects_error:
        with open(error_file, encoding="utf-8") as f:
            expected_error = f.read().strip()
    else:
        with open(expected_file, encoding="utf-8") as f:
            expected = f.read().strip()

    if expects_error:
        if result.returncode == 0:
            print(f"FAIL: {file_path}")
            print("Expected error:", expected_error)
            print("Got:", output)
            return False
        if expected_error in error:
            print(f"PASS: {file_path}")
            return True
        print(f"FAIL: {file_path}")
        print("Expected error:", expected_error)
        print("Got error:", error or "(no stderr)")
        return False

    if result.returncode != 0:
        print(f"FAIL: {file_path}")
        print("Expected:", expected)
        print("Got error:", error or "(no stderr)")
        return False

    if output == expected:
        print(f"PASS: {file_path}")
        return True

    print(f"FAIL: {file_path}")
    print("Expected:", expected)
    print("Got:", output)
    return False


def main():
    test_files = sorted(
        os.path.join(TEST_DIR, name)
        for name in os.listdir(TEST_DIR)
        if name.endswith(".tk")
    )

    passed = 0
    total = len(test_files)
    for file_path in test_files:
        if run_test(file_path):
            passed += 1

    print(f"\nSummary: {passed}/{total} passed")
    if passed != total:
        sys.exit(1)


if __name__ == "__main__":
    main()
