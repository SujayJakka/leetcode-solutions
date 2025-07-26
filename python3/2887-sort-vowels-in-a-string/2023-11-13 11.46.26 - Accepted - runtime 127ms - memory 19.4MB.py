class Solution:
    def sortVowels(self, s: str) -> str:
        arr_vowels = []
        vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

        for ch in s:
            if ch in vowels:
                arr_vowels.append(ch)

        arr_vowels = sorted(arr_vowels)

        i = 0
        arr_strings = []

        for ch in s:
            if ch in vowels:
                arr_strings.append(arr_vowels[i])
                i += 1
            else:
                arr_strings.append(ch)
        

        return "".join(arr_strings)


        