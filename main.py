phone_number = input("enter a valid phone number: ")


def is_valid(phone_number):
    while len(phone_number) != 10:
        print("please enter a valid number")
        phone_number = input("enter a valid phone number: ")
    print(f"entered number is {phone_number}...Thankyou!!!")


is_valid(phone_number)