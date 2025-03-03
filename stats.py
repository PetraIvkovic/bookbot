def get_num_words(text):
    words = text.split()
    return len(words)


def get_sorted_chars(char_count):
    result = []
    for char, count in char_count.items():
        if char.isalpha():  # abc slova
            result.append({"char": char, "count": count})
    result.sort(key=lambda x: x["count"], reverse=True)
    return result