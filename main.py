from stats import count_characters, sort_dictionary, count_words
import sys

def get_book_text(path: str) -> str:
    with open(path) as f:
        data = f.read()
    return data


def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python main.py <path_to_book>")
        exit(1)
    else:
        path = args[1]
        text = get_book_text(path)
        count = count_characters(text)
        sorted_count = sort_dictionary(count)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {path}...")
        print("----------- Word Count ----------")
        words_count = count_words(text)
        print(f"Found total {words_count} total words")
        print("--------- Character Count -------")
        for char in sorted_count:
            if char["char"].isalpha():
                print(f"{char['char']}: {char['num']}")
        print("============= END ===============")


if __name__ == "__main__":
    main()
