def hello(name):
    if name:
        return f"Hello from Utils file {name}"
        print("***" * 10, "\n\n")
    else:
        raise NameError("Name is Empty please enter correctly")
if __name__ == '__main__':
    print(f'please run this {"__main__"}')
