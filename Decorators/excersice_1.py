# Create an @authenticated decorator that only allows the function to run is user1 has 'valid' set to True:
user1 = {
    'name': 'Sorna',
    'valid': True #changing this will either run or not run the message_friends function.
}

def authenticated(fn):
    def wrap_fun(*args,**kwargs):
        if user1.get('valid'):
            fn(*args,**kwargs)
        else:
            print(f"User is not authenticated")

    return wrap_fun


@authenticated
def message_friends(user):
    print(f"message has been sent for {user.get('name')}")

message_friends(user1)