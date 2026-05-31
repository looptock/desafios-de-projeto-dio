def is_palindrome_recursive(word, low, high):
    if word == "":
        return False
    new_word = list(word)
    new_word[low], new_word[high -
                            low] = new_word[high - low], new_word[low]
    if ''.join(new_word[::-1]) == word:
        return True
    else:
        if word[low] == word[high] and low < high:
            return is_palindrome_recursive(word, low + 1, high - 1)
        else:
            return False


word = "agua"
print(is_palindrome_recursive(word, 0, len(word) - 1))
