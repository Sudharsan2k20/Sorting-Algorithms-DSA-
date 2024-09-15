word1 = 'abc'
word2 = 'pqd'
final_word = ''
i = 0
while i < len(word1) or i <len(word2):
    if i <len(word1):
        final_word += word1[i]
    if i <len(word2):
        final_word += word2[i]
    i += 1
print(final_word)