import argparse
import cowsay
import sys


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", nargs="*")
    return parser.parse_args()


def read_message():
    msg = sys.stdin.readline().rstrip()
    for line in sys.stdin.readlines():
        line = line.rstrip()
        # XXX: (for some reason) this is needed to correctly handle EOF
        if not line:
            break
        if line.startswith(" "):
            msg += "\n"
            line = line[1:]
        msg += " " + line
    return msg


if __name__ == "__main__":
    args = parse_arguments()
    if args.message:
        # NOTE: emulating "cowsay" behaviour
        message = [w for arg in args.message for w in arg.split(" ") if w]
        message = " ".join(message)
    else:
        message = read_message()
    print(cowsay.cowsay(message))
