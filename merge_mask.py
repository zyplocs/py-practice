from itertools import zip_longest

def mergemask_samelength_prompt():
    print("Enter two words of the same length, one at a time...")

    while True:
        merged_and_masked = []
        word_one = input("1st Word --> ").strip().lower()
        word_two = input("2nd Word --> ").strip().lower()

        if not word_one or not word_two:
            print("At least one input was empty! Try again...")
            continue

        if not word_one.isalpha() or not word_two.isalpha():
            print("At least one input contained a non-alpha char! Try again...")
            continue

        if len(word_one) != len(word_two):
            print("The word lengths do not match! Try again...")
            continue

        for one, two in zip(word_one, word_two):
            if one == two:
                merged_and_masked.append(one)
            else:
                merged_and_masked.append("*")

        masked_word = "".join(merged_and_masked)
        print(f"Result: {masked_word}")
        break

def mergemask_prompt():
    print("Enter two words, one at a time...")

    while True:
        merged_and_masked = []
        word_one = input("1st Word --> ").strip().lower()
        word_two = input("2nd Word --> ").strip().lower()

        if not word_one or not word_two:
            print("At least one input was empty! Try again...")
            continue

        if not word_one.isalpha() or not word_two.isalpha():
            print("At least one input contained a non-alpha char! Try again")
            continue

        for one, two in zip_longest(word_one, word_two, fillvalue="_"):
            if one == two:
                merged_and_masked.append(one)
            else:
                merged_and_masked.append("*")

        masked_word = "".join(merged_and_masked)
        print(f"Result: {masked_word}")
        break


if __name__ == "__main__":
    mergemask_prompt()