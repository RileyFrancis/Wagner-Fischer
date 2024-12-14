def wagner_fischer(word_1, word_2):
    current_row = range(len(word_1) + 1)

    for row in range(1, len(word_2) + 1):
        previous_row = current_row
        current_row = [row] + [0] * len(word_1)

        for col in range(1, len(word_1) + 1):
            insert = previous_row[col] + 1
            delete = current_row[col - 1] + 1
            substitute = previous_row[col - 1]
            if word_1[col - 1] != word_2[row - 1]:
                substitute += 1
            current_row[col] = min(insert, delete, substitute)

    return current_row[len(word_1)]