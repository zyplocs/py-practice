def countdown():
    while True:
        usr_in = input("Enter a starting number: ").strip()
        
        try:
            starting_from = int(usr_in)
            if starting_from > 0:
                for i in range(starting_from, -1, -1):
                    print(i)
                print("Blast off!")
                break
            else:
                raise ValueError
        except ValueError:
            print("Invalid input!")
            break


if __name__ == "__main__":
    countdown()