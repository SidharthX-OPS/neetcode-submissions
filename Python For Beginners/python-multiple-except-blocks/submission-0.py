def divide_numbers(a: str, b: str) -> None:
    try:
        x = int(a)
        y = int(b)
        z = x/y
        print(z)
    except ValueError:
        print("Error: Invalid value!")
    except ZeroDivisionError:
        print("Error: Division by zero!")
    except Exception as Error:
        print("An error occurred:", Error)



# do not modify below this line
divide_numbers("10", "2")
divide_numbers("12", "0")
divide_numbers("2", "not a number")
