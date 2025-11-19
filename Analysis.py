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
    for char in word: s += LETTER_POSITIONS.get(char, 0)
    return s


def hash_div(key, m): return key % m


def hash_mult(key, m):
    A = (math.sqrt(5) - 1) / 2
    return math.floor(m * ((key * A) % 1))


def analyze_chaining(words, hash_func, m, method_name):
    table = [[] for _ in range(m)]
    for word in words:
        idx = hash_func(get_key_value(word), m)
        table[idx].append(word)

    print(f"\n>>> Аналіз: Ланцюжки ({method_name}, M={m})")
    total_comps = 0

    for word in words:
        idx = hash_func(get_key_value(word), m)
        chain = table[idx]
        comps = 0
        for w in chain:
            comps += 1
            if w == word: break
        total_comps += comps

    avg = total_comps / len(words)
    print(f"Середня к-сть порівнянь: {avg:.2f}")
    return avg


def analyze_open_addressing(words, hash_func, m, method_name):
    table = [None] * m
    for word in words:
        k = get_key_value(word)
        start_idx = hash_func(k, m)
        for i in range(m):
            idx = (start_idx + i) % m
            if table[idx] is None:
                table[idx] = word
                break

    print(f"\n>>> Аналіз: Відкрита адресація ({method_name}, M={m})")
    total_comps = 0

    for word in words:
        k = get_key_value(word)
        start_idx = hash_func(k, m)
        comps = 0
        for i in range(m):
            idx = (start_idx + i) % m
            comps += 1
            if table[idx] == word: break
            if table[idx] is None: break  # Не знайшли
        total_comps += comps

    avg = total_comps / len(words)
    print(f"Середня к-сть порівнянь: {avg:.2f}")
    return avg


if __name__ == "__main__":
    analyze_chaining(WORDS, hash_div, 13, "Ділення")
    analyze_chaining(WORDS, hash_mult, 16, "Множення")
    analyze_open_addressing(WORDS, hash_div, 13, "Ділення")
    analyze_open_addressing(WORDS, hash_mult, 16, "Множення")