import cmd
import shlex
import cowsay


class CowsayCLI(cmd.Cmd):
    intro = "Welcome to python-cowsay CLI\n"
    prompt = "cowsay> "

    def do_exit(self, arg: str):
        """
        Exit command line

        Usage: exit
        """
        return True

    def do_list_cows(self, arg: str):
        """
        Lists all cow file names in the given directory

        Usage: list_cows <cow_path>
        """
        cow_path = shlex.split(arg)[0] if arg else cowsay.COW_PEN
        print(*cowsay.list_cows(cow_path))

    def do_make_bubble(self, arg: str):
        """
        Wraps text is wrap_text is true, then pads text and sets inside a bubble.

        Usage: make_bubble <text> [brackets] [width] [wrap_text]
        """
        txt, *args = shlex.split(arg)
        default_args = ["cowsay", "40", "True"]
        args = args + default_args[len(args):]
        print(cowsay.make_bubble(txt, brackets=cowsay.THOUGHT_OPTIONS[args[0]],
                                 width=int(args[1]), wrap_text=bool(args[2])))

    def do_cowsay(self, arg: str):
        """
        Similar to the cowsay command. Parameters are listed with their
        corresponding options in the cowsay command. Returns the resulting cowsay string

        Usage: cowsay <text> [cow] [eyes] [tongue]
        """
        text, *args = shlex.split(arg)
        default_args = ["default", cowsay.Option.eyes, cowsay.Option.tongue]
        args = args + default_args[len(args):]
        print(cowsay.cowsay(text, cow=args[0], eyes=args[1], tongue=args[2]))

    def do_cowthink(self, arg: str):
        """
        Similar to the cowthink command. Parameters are listed with their
        corresponding options in the cowsay command. Returns the resulting cowsay string

        Usage: cowthink <text> [cow] [eyes] [tongue]
        """
        text, *args = shlex.split(arg)
        default_args = ["default", cowsay.Option.eyes, cowsay.Option.tongue]
        args = args + default_args[len(args):]
        print(cowsay.cowthink(text, cow=args[0], eyes=args[1], tongue=args[2]))

    @staticmethod
    def _filter_completion_items(text: str, items: list[str]) -> list[str]:
        return list(filter(lambda x: x.startswith(text), items))

    @staticmethod
    def _complete_cowsay(text: str, line: str, n_opts: int,
                         opts_mapping: dict[int, list[str]]) -> list[str]:
        args = shlex.split(line)
        n_args = len(args)
        if not 1 < n_args <= n_opts:
            return []
        if not text:
            return opts_mapping.get(n_args, [])
        idx = args.index(text)
        return CowsayCLI._filter_completion_items(text, opts_mapping.get(idx, []))

    def complete_make_bubble(self, text: str, line: str, start: int, end: int) -> list[str]:
        opts_mapping = {
            2: ["cowsay", "cowthink"],
            4: ["True", "False"],
        }
        return self._complete_cowsay(text, line, 5, opts_mapping)

    def complete_cowthink(self, text: str, line: str, start: int, end: int) -> list[str]:
        opts_mapping = {
            2: cowsay.list_cows(),
            3: ["XX", "OO", ".."],
            4: ["UU", "ll", "II"],
        }
        return self._complete_cowsay(text, line, 5, opts_mapping)

    def complete_cowsay(self, text: str, line: str, start: int, end: int) -> list[str]:
        return self.complete_cowthink(text, line, start, end)



if __name__ == '__main__':
    CowsayCLI().cmdloop()
