n = int(input())
words_list = []
for _ in range(n):
    word = input()
    count = len(word)
    words_list.append((word, count))
# 중복삭제
words_list = list(set(words_list))
# 단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))
for word in words_list:
    print(word[0])