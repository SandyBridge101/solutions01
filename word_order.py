num_words = int(input())

word_count = {}
distinct_occurrences = 0

for _ in range(num_words):
    word = input()

    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1
        distinct_occurrences += 1

print( distinct_occurrences)
for word, count in word_count.items():
    print(count,end=" ")