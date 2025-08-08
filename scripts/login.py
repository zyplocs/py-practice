def main():
    while True:
        passw_input: str = input("Enter your password:\n").strip()

        if passw_input == "opensesame":
            print("Access granted.")
            break
        else:
            print("Incorrect password. Try again")
            continue

if __name__ == "__main__":
    main()