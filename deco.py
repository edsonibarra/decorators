def sum_two_integers(x: int, y: int) -> int:
    if isinstance(x, int) and isinstance(y, int):
        return x + y
    else:
        raise ValueError('Only int values are accepted')


def main():
    x: int = 100
    y: int = 300

    result: int = sum_two_integers(x, y)

    print(result)


main()
