def useless():
    print("> Enter any text, pretty please")

    while True:
        usr_input = input().strip().lower()

        if not usr_input:
            print("> You said nothing!")
        elif usr_input == "help":
            print("> Available commands: help, quit")
        elif usr_input == "quit":
            print("> Goodbye")
            break
        else:
            print(f"> You said: {usr_input}")


if __name__ == "__main__":
    useless()
