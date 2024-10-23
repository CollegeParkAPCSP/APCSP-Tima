def func(s1: str, sub: str) -> None:
    if sub in s1:
        print(f"Is alphanumeric? {s1.isalnum()}")
        print(f"Is alphabetic? {s1.isalpha()}")
        print(f"Is digit? {s1.isdigit()}")
        print(f"Is lowercase? {s1.islower()}")
        print(f"Is uppercase? {s1.isupper()}")

func("HelloWorld", "World")