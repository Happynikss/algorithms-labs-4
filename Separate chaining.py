import math

# Вхідна фраза (Варіант 6)
SENTENCE = "Скільки вовка не годуй, а він усе в ліс дивиться"

# Очищення: прибираємо коми, крапки, переводимо у верхній регістр, розбиваємо на слова
WORDS = SENTENCE.replace(',', '').replace('.', '').upper().split()

# Словник позицій
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


def hash_div(key, m=13):
    return key % m


def hash_mult(key, m=16):
    A = (math.sqrt(5) - 1) / 2  # ~0.618
    return math.floor(m * ((key * A) % 1))


def build_chained_table(words, hash_func, m):
    # Створюємо таблицю з m порожніх списків
    table = [[] for _ in range(m)]

    print(f"\n--- Будуємо таблицю (M={m}) ---")
    for word in words:
        k = get_key_value(word)
        idx = hash_func(k, m)
        # Додаємо в ланцюжок
        table[idx].append(word)
        print(f"Слово: {word:<10} | K={k:<3} | h(k)={idx} -> додано в індекс {idx}")

    return table


# 1. Метод ділення (M=13)
table_chain_div = build_chained_table(WORDS, hash_div, 13)

print("\n>>> РЕЗУЛЬТАТ (Ланцюжки, Метод ділення):")
for i, chain in enumerate(table_chain_div):
    print(f"Idx {i:02d}: {chain}")

# 2. Метод множення (M=16)
table_chain_mult = build_chained_table(WORDS, hash_mult, 16)

print("\n>>> РЕЗУЛЬТАТ (Ланцюжки, Метод множення):")
for i, chain in enumerate(table_chain_mult):
    print(f"Idx {i:02d}: {chain}")
