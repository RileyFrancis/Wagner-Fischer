def wagner_fischer(word_1, word_2):
    current_row = range(len(word_1) + 1)

    for i in range(1, len(word_2) + 1):
        previous_row = current_row
        current_row = [i] + [0] * len(word_1)

        for j in range(1, len(word_1) + 1):
            insert = previous_row[j] + 1
            delete = current_row[j-1] + 1
            substitute = previous_row[j-1]

            if word_1[j-1] != word_2[i-1]:
                substitute += 1
            current_row[j] = min(insert, delete, substitute)

    return current_row[len(word_1)]

def spell_check(word, dictionary:list, num_suggestions:int=5):
    if word in dictionary:
        return None
    suggestions = [(correct_word, wagner_fischer(word, correct_word)) for correct_word in dictionary]
    suggestions.sort(key=lambda x: x[1])
    return suggestions[:num_suggestions]


if __name__ == "__main__":
    dictionary = []
    with open("big_words.txt", 'r') as file:
        dictionary = [line.strip() for line in file]

    misspelled_word = "plakn"
    suggestions = spell_check(misspelled_word, dictionary)

    if suggestions is None:
        print(f"{misspelled_word} is spelled correctly")
        exit()

    print(f"Best suggestions for '{misspelled_word}':")
    for word, distance in suggestions:
        print(f"{word} (Distance: {distance})")