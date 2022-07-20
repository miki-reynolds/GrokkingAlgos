'''
Given a string and a list of words, find all the starting indices of substrings in the given string that are a concatenation of all the given words exactly once without any overlapping of words. It is given that all words are of the same length.

e.g.
Input: String="catfoxcat", Words=["cat", "fox"]
Output: [0, 3]
Explanation: The two substring containing both the words are "catfox" & "foxcat".

e.g.
Input: String="catcatfoxfox", Words=["cat", "fox"]
Output: [3]
Explanation: The only substring containing both the words is "catfox".

Solution
This problem follows the Sliding Window pattern and has a lot of similarities with Maximum Sum Subarray of Size K. We will keep track of all the words in a HashMap and try to match them in the given string. Here are the set of steps for our algorithm:

Keep the frequency of every word in a HashMap.
Starting from every index in the string, try to match all the words.
In each iteration, keep track of all the words that we have already seen in another HashMap.
If a word is not found or has a higher frequency than required, we can move on to the next character in the string.
Store the index if we have found all the words.

Time Complexity
The time complexity of the above algorithm will be O(N∗M∗Len) where ‘N’ is the number of characters in the given string, ‘M’ is the total number of words, and ‘Len’ is the length of a word.

Space Complexity
The space complexity of the algorithm is O(M) since at most, we will be storing all the words in the two HashMaps. In the worst case, we also need O(N) space for the resulting list. So, the overall space complexity of the algorithm will be O(M+N).

'''


def find_concat_substring(string, words):
    word_length = len(words[0])
    words_count = len(words)

    if word_length == 0 or words_count == 0:
        return []

    word_frequency = {}
    for word in words:
        if word not in word_frequency:
            word_frequency[word] = 0
        word_frequency[word] += 1

    result_indices = []
    for i in range(len(string) - words_count*word_length + 1):
        words_seen = {}
        for j in range(words_count):
            next_word_index = i + j * word_length
            # Get the next word from the string
            word = string[next_word_index:next_word_index + word_length]

            if word not in word_frequency:  # Break if we don't need this word
                break

            if word not in words_seen:  # Add the word to the 'words_seen' map
                words_seen[word] = 0
            words_seen[word] += 1

            # No need to process further if the word has higher frequency than required
            if words_seen[word] > word_frequency.get(word, 0):
                break

            # Store index if we have found the pattern (combination of words) stored in the words array
            if j + 1 == words_count:
                result_indices.append(i)

    return result_indices


def main():
    print(find_concat_substring("catfoxcat", ["cat", "fox"]))
    print(find_concat_substring("catcatfoxfox", ["cat", "fox"]))


main()
# [0, 3]
# [3]