def do_stuff(num=0):
    try:
        if num:
            return int(num) + 5
        else:
            return f"Please enter a number"
    except ValueError as err:
        return err
