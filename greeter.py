def greet(name: str, greeting: str="Hello") -> str:
    return f"{greeting.capitalize()}, {name.capitalize()}!"

def main():
    print("Greeting constructor. Follow the prompts below...")

    while True:
        usr_name = input("> Enter a name: ").strip().lower()
        usr_greeting = input("> Enter a greeting (or leave blank for default): ").strip()

        if not usr_name:
            print("The name cannot be blank! Try again...")
            continue

        if usr_greeting:
            constructed_greet = greet(usr_name, usr_greeting)
            print(constructed_greet)
            break
        else:
            constructed_greet = greet(usr_name)
            print(constructed_greet)
            break


if __name__ == "__main__":
    main()