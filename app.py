## Password generator app
import random


# This function check weather any one character from a list present in a string or not
def contains_any_character(input_string, characters):
    return any(char in input_string for char in characters)


uppercase_letters = [
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O',
    'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
]

lowercase_letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

special_characters = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+', '-', '=', '{',
    '}', '[', ']', '|', '\\', ';', ':', "'", '"', ',', '.', '/', '<', '>', '?'
]


def generate_password(nums: int) -> str:
    all_characters = uppercase_letters + lowercase_letters + numbers + special_characters

    result = ""

    for i in range(0, nums):
        if nums > 3:
            if i > nums - 3:
                if not (contains_any_character(result, lowercase_letters)):
                    result += random.choice(lowercase_letters)
                elif not (contains_any_character(result, uppercase_letters)):
                    result += random.choice(uppercase_letters)
                elif not (contains_any_character(result, special_characters)):
                    result += random.choice(special_characters)
                elif not (contains_any_character(result, numbers)):
                    result += random.choice(numbers)
                else:
                    result += random.choice(all_characters)
            else:
                result += random.choice(all_characters)
        else:
            result += random.choice(all_characters)

    return result


if __name__ == "__main__":
    print("**************************************\n")
    print("* Welcome to PASSWORD GENERATOR APP *\n")
    print("**************************************\n")

    # Taking user input
    password_length = ""
    while True:
        try:
            password_length = int(
                input("\nEnter the length of your desired Password: "))
            break
        except ValueError:
            print("\n❌❌❌ Please provide an integer value! ❌❌❌")

    # calling the generate password function to generate a random password
    result = generate_password(password_length)

    # Print password
    print("\n\n🎉🎉 The generated password is " + result + "\n")
