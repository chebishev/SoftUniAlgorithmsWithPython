from collections import Counter

words = input().split(", ")
text = input()

words_dictionary = Counter(words)
words_by_index = {}

for word in words_dictionary:

    try:
        index = 0
        while True:
            index = text.index(word, index)
            if index not in words_by_index:
                words_by_index[index] = []
            words_by_index[index].append(word)
            index += len(word)
    except ValueError:
        pass


def find_all_solutions(index, text, words_by_index, words_dictionary, used_words):
    if index >= len(text):
        print(" ".join(used_words))
        return
    if index not in words_by_index:
        return
    for word in words_by_index[index]:
        if words_dictionary[word] == 0:
            continue
        used_words.append(word)
        words_dictionary[word] -= 1
        find_all_solutions(index + len(word), text, words_by_index, words_dictionary, used_words)

        used_words.pop()
        words_dictionary[word] += 1


find_all_solutions(0, text, words_by_index, words_dictionary, [])

# test inputs:

# text, me, so, do, m, ran
# somerandomtext

# Word, cruncher, cr, h, unch, c, r, un, ch, er
# Wordcruncher

# tu, stu, p, i, d, pi, pid, s, pi
# stupid
