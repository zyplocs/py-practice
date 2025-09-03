def alpha_prompt():
    while True:
        usr_in = input("Enter an alphabetical string: ")

        if usr_in.isalpha():
            vowels = {"a", "e", "i", "o", "u"}
            stringy_in = list(usr_in)
            chars = []

            for z in stringy_in:
                if z.lower() not in vowels:
                    chars.append(z)

            vowelless = "".join(chars)

            print(f"Result: {vowelless}")
            break
        else:
            print("Invalid input! Try again...")

def censor_prompt():
    while True:
        usr_in = input("Enter a sentence: ")

        if usr_in:
            vowels = {"a", "e", "i", "o", "u"}
            censored = []

            for i, val in enumerate(usr_in):
                if val.lower() in vowels:
                    print(f"Vowel found at index {i}")
                    censored.append("*")
                else:
                    censored.append(val)

            censored_in = "".join(censored)
            print(f"Result: {censored_in}")
            break
        else:
            print("That was nothing!")


if __name__ == "__main__":
    censor_prompt()
