def concat(words):
    memoization = {}

    def check_word(word):
        if len(word) == 1:
            return False

        if word in memoization:
            return memoization[word]

        memoization[word] = False
        for i in range(1, len(word)):
            prefix, suffix = word[:i], word[i:]
            print(f"pre - {prefix} AND suffix - {suffix}")

            if prefix in words and (suffix in words or check_word(suffix)):
                memoization[word] = True
                print(f"Memo {word}: {memoization[word]}")
                break
            print()
        return memoization[word]

    return [word for word in words if check_word(word)]


print(concat(["cat", "cats", "catsdogcats", "dog", "dogcatsdog", "hippopotamuses", "rat", "ratcatdogcat"]))