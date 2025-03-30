def get_num_words(text):
    words = text.split()
    return len(words)

def get_char_counts(text):
    char_counts = {}
    for char in text.lower():
        char_counts[char] = char_counts.get(char, 0) + 1
    return char_counts

def get_sorted_char_counts(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        if char.isalpha():
            sorted_chars.append({'char': char, 'count': count})

    def sort_on_count(item):
        return item['count']

    sorted_chars.sort(key=sort_on_count, reverse=True)
    return sorted_chars
