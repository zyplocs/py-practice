import re

def word_stats(sentence: str) -> tuple[int, float]:
    if not isinstance(sentence, str):
        raise TypeError(f"Input must be str, got {type(sentence).__name__}")

    if not sentence.strip():
        raise ValueError("Empty input!")

    words = [w for w in re.split(r"[^\w'-]+", sentence) if w]
    word_count = len(words)
    if word_count == 0:
        raise ValueError("Zero words in the sentence!")

    avg_length = sum(len(word) for word in words) / word_count
    return word_count, avg_length