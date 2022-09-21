def hello(name):
    if name:
        return f"Hello from Utils file {name}"
        print("***" * 10, "\n\n")
    else:
        raise NameError("Name is Empty please enter correctly")


if __name__ == "__main__":
    print(f"Hello I'm {__name__} as long as i get executed")
