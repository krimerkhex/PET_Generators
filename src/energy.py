from itertools import zip_longest


def is_string(value) -> bool:
    return type(value) == str


def fix_wiring(args_1, args_2, args_3) -> list:
    return list(filter(is_string, list(
        ((f"plug {i[0]} into {i[1]} using {i[2]}" if i[2] is not None else f"weld {i[0]} to {i[1]} without plug") if
         i[0] is not None and
         i[1] is not None else None
         for i in zip_longest(filter(is_string, args_1), filter(is_string, args_2), filter(is_string, args_3))))))


if __name__ == "__main__":
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    for c in fix_wiring(cables, sockets, plugs):
        print(c)
