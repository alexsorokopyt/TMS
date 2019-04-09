# Даны три слова. Выяснить, является ли хоть одно из них палиндромом ("перевертышем"),
# т. е. таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)

def palindrome(word: str) -> str:
    """
    This function checks if the given word a palindrome or NOT.

    Parameters
    ----------
    word: str
        Any given word.

    Returns
    -------
    str
        Return a string that says if that word a palindrome or NOT.
    """
    if word == word[::-1]:
        return True
    else:
        return False

print(palindrome('wordrow'))
print(palindrome('word'))

list_of_words = ['Teach', 'meem', 'skilliks']
counter = 0
for word in list_of_words:
    if palindrome(word) == True:
        counter += 1
print(f'There are {counter} palindromes in the given list')