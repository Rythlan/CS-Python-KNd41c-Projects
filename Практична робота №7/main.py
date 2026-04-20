import string

def safe_open(file_name: str, mode: str):
    try:
        file = open(file_name, mode, encoding="utf-8")
    except Exception:
        print(f"Файл {file_name} не вдалося відкрити!")
        return None
    else:
        print(f"Файл {file_name} відкрито!")
        return file


file1_name = "TF20_1.txt"
file2_name = "TF20_2.txt"

text_to_write = (
    "Сучасна криптографія — це фундаментальна складова кібербезпеки. "
    "Використання децентралізація, автентифікація, конфіденційність, "
    "ідентифікація та багатофакторність забезпечує надійний захист. "
    "Чи є ці методології безальтернативність для майбутнього? конкурентоздатність"
)

f1_write = safe_open(file1_name, "w")
if f1_write:
    f1_write.write(text_to_write)
    f1_write.close()
    print("Файл TF20_1.txt було закрито!\n")

f1_read = safe_open(file1_name, "r")
f2_write = safe_open(file2_name, "w")

if f1_read and f2_write:
    raw_text = f1_read.read()
    clean_text = raw_text.translate(str.maketrans("", "", string.punctuation))
    words = clean_text.split()

    max_len = 0
    for word in words:
        if len(word) > max_len:
            max_len = len(word)

    max_words = [word for word in words if len(word) == max_len]
    f2_write.write(" ".join(max_words))
    f1_read.close()
    f2_write.close()

    print("Файли було закрито!\n")



print("--- Результат з TF20_2.txt ---")
f2_read = safe_open(file2_name, "r")

if f2_read:
    words_from_file2 = f2_read.read().split()

    for i, word in enumerate(words_from_file2, start=1):
        print(word, end=" ")

        if i % 5 == 0:
            print()

    print("\n\nФайл TF20_2.txt було закрито!")
    f2_read.close()

