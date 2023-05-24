class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # First declare a list to store the non repeting values
        substring = []
        temp = []
        maxi = 0
        for letter in s:
            # try remove first if, may be redundant
            if not letter in substring:
                substring.append(letter)
            else:
                temp = [i for i in substring]
                for pointer in temp:
                    if pointer != letter:
                        substring.remove(pointer)
                    else:
                        substring.remove(pointer)
                        break
                substring.append(letter)

            if len(substring) > maxi:
                maxi = len(substring)
        print(substring)
        return(maxi)