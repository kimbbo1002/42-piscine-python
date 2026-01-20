def garden_operations(error_type):
    if error_type == "Value":
        int("abc")
    elif error_type == "ZeroDivision":
        1/0
    elif error_type == "FilenotFound":
        open("missing.txt")
    elif error_type == "Key":
        tmp = {}
        print(tmp["missing_plant"])


def test_error_types():
    print("=== Garden Error Types Demo ===\n")
    for error in ["Value", "ZeroDivision", "FilenotFound", "Key"]:
        try:
            print(f"Testing {error}Error...")
            garden_operations(error)
        except ValueError:
            print("Caught ValueError: invalid literal for int()n\n")
        except ZeroDivisionError:
            print("Caught ZeroDivisionError: division by zero\n")
        except FileNotFoundError:
            print("Caught FileNotFoundError: No such file 'missing.txt'\n")
        except KeyError:
            print("Caught KeyError: 'missing_plant'\n")
    print("Testing multiple errors together...")
    try:
        garden_operations("file")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues !\n")
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
