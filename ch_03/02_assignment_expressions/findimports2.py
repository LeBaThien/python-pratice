import os
import re
import sys

import_re = re.compile(r"^\s*import\s+\.{0,2}((\w+\.)*(\w+))\s*$")
import_from_re = re.compile(
    r"^\s*from\s+\.{0,2}((\w+\.)*(\w+))\s+import\s+(\w+|\*)+\s*$"
)


def main():
    if len(sys.argv) != 2:
        print(f"usage: {os.path.basename(__file__)} file-name")
        sys.exit(1)

    # with open(sys.argv[1]) as file:
    #     for line in file:
    #         match = import_re.match(line)
    #         if match:
    #             print(match.groups()[0])
    #
    #         match = import_from_re.match(line)
    #         if match:
    #             print(match.groups()[0])
    #
    # := the same logic above

    with open(sys.argv[1]) as file:
        for line in file:
            if match := import_re.match(line):
                print(match.groups()[0])

            if match := import_from_re.match(line):
                print(match.groups()[0])


if __name__ == '__main__':
    main()
