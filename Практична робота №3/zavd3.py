def main():
    sentence = input("Введіть, будь ласка, речення: ")

    while not sentence:
        sentence = input("Ви нічого не ввели, спробуйте ще раз: ")

    words = sentence.split()
    found_words = []

    for word in words:
        clean_word = word.strip(".,!?;:")
        if clean_word.lower().endswith("ий"):
            found_words.append(clean_word)

    if found_words:
        print(f"Слова, що закінчуються на «ий»: {', '.join(found_words)}")
    else:
        print("На жаль, слів із таким закінченням не знайдено.")


if __name__ == "__main__":
    main()