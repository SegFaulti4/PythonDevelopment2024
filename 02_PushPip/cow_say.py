import argparse
import cowsay
import sys
import textwrap


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("message", nargs="*", type=str)
    parser.add_argument(
        "-l", dest="list_cows", action="store_true", help="list all cows"
    )
    parser.add_argument(
        "-n",
        dest="wrap_text",
        action="store_false",
        help="do not wrap text, if specified any positional arguments are prohibited",
    )
    parser.add_argument(
        "-f",
        dest="cow",
        action="store",
        default="default",
        type=str,
        help="name of the cow",
    )
    parser.add_argument(
        "-e",
        dest="eyes",
        action="store",
        default="OO",
        type=str,
        help="custom eye string",
    )
    parser.add_argument(
        "-T",
        dest="tongue",
        action="store",
        default="  ",
        type=str,
        help="custom tongue string",
    )
    parser.add_argument(
        "-W",
        dest="width",
        action="store",
        default=40,
        type=int,
        help="with of the text bubble",
    )
    parser.add_argument(
        "-b", const="b", dest="preset", action="append_const", help="Borg preset"
    )
    parser.add_argument(
        "-d", const="d", dest="preset", action="append_const", help="dead preset"
    )
    parser.add_argument(
        "-g", const="g", dest="preset", action="append_const", help="greedy preset"
    )
    parser.add_argument(
        "-p", const="p", dest="preset", action="append_const", help="paranoia preset"
    )
    parser.add_argument(
        "-s", const="s", dest="preset", action="append_const", help="stoned preset"
    )
    parser.add_argument(
        "-t", const="t", dest="preset", action="append_const", help="tired preset"
    )
    parser.add_argument(
        "-w", const="w", dest="preset", action="append_const", help="wired preset"
    )
    parser.add_argument(
        "-y", const="y", dest="preset", action="append_const", help="youthful preset"
    )
    return parser


if __name__ == "__main__":
    parser = arg_parser()
    args = parser.parse_args()
    args.eyes = args.eyes[:2]
    args.tongue = args.tongue[:2]
    args.preset = None if args.preset is None else "".join(args.preset)

    if args.list_cows:
        cows = " ".join(sorted(cowsay.list_cows()))
        text = textwrap.wrap(cows, width=70)
        print(*text, sep="\n")
        parser.exit()

    if args.message:
        if not args.wrap_text:
            parser.print_help()
            parser.exit()
        # NOTE: emulating "cowsay" behaviour
        message = [w for arg in args.message for w in arg.split(" ") if w]
        message = " ".join(message)
    else:
        message = "".join(sys.stdin.readlines())

    print(
        cowsay.cowsay(
            message,
            cow=args.cow,
            preset=args.preset,
            eyes=args.eyes,
            tongue=args.tongue,
            width=args.width,
            wrap_text=args.wrap_text,
        )
    )
