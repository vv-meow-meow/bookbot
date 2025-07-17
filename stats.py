from collections import Counter


def count_characters(text: str) -> dict[str, int]:
    lowered_text = text.lower()
    counter = Counter(lowered_text)
    return dict(counter)

def count_words(text: str) -> int:
    words = text.split()
    return len(words)


def sort_dictionary(characters: dict[str, int]) -> list[dict[str, int]]:
    # I know about Counter.most_coomon(), that's just for practice.
    characters_list: list[dict[str, int]] = []
    for char, count in characters.items():
        characters_list.append({"char": char, "num": count})

    characters_list.sort(reverse=True, key=lambda x: x["num"])
    return characters_list
