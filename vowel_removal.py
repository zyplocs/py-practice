def alpha_prompt():
    while True:
        usr_in = input("Enter an alphabetical string: ")

        if usr_in.isalpha():
            vowels = ("a", "e", "i", "o", "u")
            stringy_list = list(usr_in)
            chars = []
            
            for z in stringy_list:
                if z.lower() not in vowels:
                    chars.append(z)
            
            vowelless = "".join(chars)
                
            print(f"Result: {vowelless}")
            break
        else:
            print("Invalid input! Try again...")


if __name__ == "__main__":
    alpha_prompt()