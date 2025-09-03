def word_prompt():
    entries = []
    print("Enter words one at a time. Type 'stop' when finished")
    while True:
        entry = input().strip()

        if not entry.isalpha():
            print("No punctuation or other non-alphabetic characters!")
            continue

        if entry.lower() == "stop":
            if not entries:
                print("No words entered. Exiting program...")
            else:
                longest = max(entries, key=lambda x: len(x))
                print(f"Longest word entered -> {longest} | Length: {len(longest)} letters")
            break

        entries.append(entry)


if __name__ == "__main__":
    word_prompt()