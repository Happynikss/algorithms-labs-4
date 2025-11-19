import math

SENTENCE = "Скільки вовка не годуй, а він усе в ліс дивиться"
WORDS = SENTENCE.replace(',', '').replace('.', '').upper().split()

LETTER_POSITIONS = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Ґ': 5, 'Д': 6, 'Е': 7, 'Є': 8, 'Ж': 9, 'З': 10,
    'И': 11, 'І': 12, 'Ї': 13, 'Й': 14, 'К': 15, 'Л': 16, 'М': 17, 'Н': 18, 'О': 19,
    'П': 20, 'Р': 21, 'С': 22, 'Т': 23, 'У': 24, 'Ф': 25, 'Х': 26, 'Ц': 27, 'Ч': 28,
    'Ш': 29, 'Щ': 30, 'Ь': 31, 'Ю': 32, 'Я': 33
}


def get_key_value(word):
    s = 0
    for char in word:
        s += LETTER_POSITIONS.get(char, 0)
    return s

print(f"Список слів: {WORDS}")
print("Ключі (K) для слів:")
for w in WORDS:
    print(f"{w}: {get_key_value(w)}")

def hash_div(key, m):
    return key % m


def hash_mult(key, m):
    A = (math.sqrt(5) - 1) / 2
    return math.floor(m * ((key * A) % 1))


def build_open_addressing_table(words, hash_func, m):
    table = [None] * m
    print(f"\n--- Побудова таблиці (M={m}, Лінійне дослідження) ---")

    for word in words:
        k = get_key_value(word)
        start_idx = hash_func(k, m)
        placed = False

        for i in range(m):
            idx = (start_idx + i) % m
            if table[idx] is None:
                table[idx] = word
                shift_msg = f"(колізія! зсув +{i})" if i > 0 else ""
                print(f"Слово: {word:<10} | h(k)={start_idx:<2} -> записано в {idx} {shift_msg}")
                placed = True
                break
            else:
                continue

        if not placed:
            print(f"ПОМИЛКА: Таблиця переповнена! Немає місця для '{word}'")

    return table


def display_table_formatted(table, method_name, m):
    print(f"\nХеш-таблиця (Відкрита адресація, {method_name}, M={m}) ---")
    print("Індекс | Слово")
    print("-------|-------")

    for i, val in enumerate(table):
        val_str = val if val is not None else "(NULL)"
        print(f"{i:02d}     | {val_str}")


if __name__ == "__main__":
    table_div = build_open_addressing_table(WORDS, hash_div, 13)
    display_table_formatted(table_div, "Метод ділення", 13)

    table_mult = build_open_addressing_table(WORDS, hash_mult, 16)
    display_table_formatted(table_mult, "Метод множення", 16)