import random


def main():
    while True:
        try:
            level: int = int(input("Level: "))
        except ValueError:
            print("Level should be a positive integer between 1 and 3 both inclusive")
        else:
            if 1 <= level <= 3:
                break
            print("Level should be a positive integer between 1 and 3 both inclusive")
    i = 0
    count = 0
    while i < 10:
        x = generate_integer(level)
        y = generate_integer(level)
        operator = get_operator()
        if operator == "/":
            if y == 0:
                y = 1
        result = calculate_result(x, y, operator)
        tries = 0
        while tries < 3:
            try:
                match operator:
                    case "+":
                        res = int(input(f"{x} + {y} = "))
                    case "-":
                        res = int(input(f"{x} - {y} = "))
                    case "*":
                        res = int(input(f"{x} * {y} = "))
                    case "/":
                        print("\nPlease only enter the quotient")
                        res = int(input(f"{x} / {y} = "))
            except ValueError:
                print("EEE")
                tries += 1
            else:
                if tries == 2:
                    print(result)
                elif res == result:
                    count += 1
                    break
                elif res != result:
                    print("EEE")
                tries += 1
        i += 1
    print(f"Score: {count}")


def generate_integer(level: int) -> int:
    """Generate and return a random integer based on level passed
    :param level: Level passed as arguement
    :type level: int
    :return: A random integer
    :rtype: int
    """
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


def get_operator() -> str:
    """Generate and return a random operator from the available ones
    :return: A random string depicting a mathematical operator
    :rtype: str
    """
    operators = ["+", "-", "/", "*"]
    return random.choice(operators)


def calculate_result(x: int, y: int, operator: str) -> int:
    """Generate and return the calculated result based on the arguements passed
    :param x: First integer passed as arguement
    :type x: int
    :param y: Second integer passed as arguement
    :type y: int
    :param operator: Mathematical operator passed as arguement
    :type operator: str
    :return: Calculated result
    :rtype: int
    """
    match operator:
        case "+":
            return x + y
        case "-":
            return x - y
        case "*":
            return x * y
        case "/":
            return x // y


if __name__ == "__main__":
    main()
