def count_syllables(word):
    syllable_count = 0
    vowels = "aeiouy"
    if len(word) <= 3:
        syllable_count = 1
    else:
        for i in range(1, len(word)):
            if word[i] in vowels and word[i - 1] not in vowels:
                syllable_count += 1
        if word.endswith("e"):
            syllable_count -= 1
        if syllable_count == 0:
            syllable_count += 1
    return syllable_count

def calculate_flesch_index(input_text):
    word_list = input_text.split()
    sentence_list = input_text.split(". ") 

    total_syllables = sum(count_syllables(word) for word in word_list)
    avg_syllables_per_word = total_syllables / len(word_list)
    avg_words_per_sentence = len(word_list) / len(sentence_list)

    flesch_readability_index = 206.835 - (1.015 * avg_words_per_sentence) - (84.6 * avg_syllables_per_word)
    readability_grade_level = 0.39 * avg_words_per_sentence + 11.8 * avg_syllables_per_word - 15.59

    return flesch_readability_index, readability_grade_level


with open("flesch.txt", "r") as text_file:
    content = text_file.read()

readability_index, grade_level_score = calculate_flesch_index(content)

print(f"Flesch Readability Index: {readability_index}")
print(f"Readability Grade Level: {grade_level_score}")
