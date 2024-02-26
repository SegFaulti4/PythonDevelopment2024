import argparse
import cowsay
import sys


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", nargs="*", type=str)
    parser.add_argument("-f", dest="cow", action="store", default="default", type=str)
    parser.add_argument("-e", dest="eyes", action="store", default="OO", type=str)
    parser.add_argument("-T", dest="tongue", action="store", default="  ", type=str)
    parser.add_argument("-W", dest="width", action="store", default=40, type=int)
    parser.add_argument("-b", const="b", dest="preset", action="append_const")
    parser.add_argument("-g", const="g", dest="preset", action="append_const")
    parser.add_argument("-p", const="p", dest="preset", action="append_const")
    parser.add_argument("-s", const="s", dest="preset", action="append_const")
    parser.add_argument("-t", const="t", dest="preset", action="append_const")
    parser.add_argument("-w", const="w", dest="preset", action="append_const")
    parser.add_argument("-y", const="y", dest="preset", action="append_const")
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
    args.eyes = args.eyes[:2]
    args.tongue = args.tongue[:2]
    args.preset = None if args.preset is None else "".join(args.preset)

    if args.message:
        # NOTE: emulating "cowsay" behaviour
        message = [w for arg in args.message for w in arg.split(" ") if w]
        message = " ".join(message)
    else:
        message = read_message()
    print(
        cowsay.cowsay(
            message,
            cow=args.cow,
            preset=args.preset,
            eyes=args.eyes,
            tongue=args.tongue,
            width=args.width,
        )
    )
