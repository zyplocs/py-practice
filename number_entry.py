def num_prompt():
    entries = []
    print("Enter numbers one at a time. Type 'done' when finished")
    while True:
        entry = input().strip()

        if entry.lower() == "done":
            if not entries:
                print("No numbers entered. Exiting program...")
            else:
                average = sum(entries) / len(entries)
                print(f"Entries: {len(entries)} | Average: {average:.2f}")
            break

        try:
            num = float(entry)
            if num >= 0:
                entries.append(num)
            else:
                print("Only positive numbers are currently accepted!")
        except ValueError:
            print("Invalid entry!")


if __name__ == "__main__":
    num_prompt()