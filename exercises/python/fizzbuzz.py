def fizzbuzz(limit: int) -> list[str]:
    """Retorna a sequência FizzBuzz de 1 até o limite informado."""
    result = []

    for number in range(1, limit + 1):
        if number % 15 == 0:
            result.append("FizzBuzz")
        elif number % 3 == 0:
            result.append("Fizz")
        elif number % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(number))

    return result


if __name__ == "__main__":
    limit = int(input("Informe o limite: "))

    for item in fizzbuzz(limit):
        print(item)
