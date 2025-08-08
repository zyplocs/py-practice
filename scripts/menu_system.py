def menu_prompt():
    num_buffer = []

    def _append_to_list():
        usr_in = input("Enter the number you'd like to add: ").strip()
        try:
            new_num = float(usr_in)
            num_buffer.append(new_num)
        except ValueError:
            print("That's not a number!")

    def _view_nums():
        if num_buffer:
            print(", ".join(map(str, num_buffer)))
        else:
            print("You haven't entered any numbers yet!")

    def _exit():
        return False

    commands = {
        1: _append_to_list,
        2: _view_nums,
        3: _exit
    }

    while True:
        print("""
        ----------------
        [1] Add a number
        [2] View numbers
        [3] Quit
        ----------------
        """)
        entry = input(">> ").strip()

        try:
            selection = int(entry)
            if selection not in commands:
                raise ValueError
            action = commands[selection]()
            if action is False:
                break
        except ValueError:
            print("Invalid entry!")


if __name__ == "__main__":
    menu_prompt()