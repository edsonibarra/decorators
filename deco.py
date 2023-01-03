def int_validation(func):
    def inner(*args):
        x: int = args[0]
        y: int = args[1]
        if isinstance(x, int) and isinstance(y, int):
            result = func(x, y)
        else:
            raise ValueError(f'Only int values are accepted. Values provided {x}, {y} are invalid')
        return result
    return inner


@int_validation
def sum_two_integers(x: int, y: int) -> int:
        return x + y


def main():
    x: int = 100
    y: int = 300

    # result: int = sum_two_integers('hello ', 'world')
    result: int = sum_two_integers(100, 500)

    print(result)


main()
