from typing import List

class Solution:
    """
    Assume the encode and decode function by default add new whitespace to seperate the word
    """
    def encode(self, strs: List[str]):
        pointer = 0
        mp_string = {}
        final_str = ""

        if not strs:
            return ""

        for word in strs:
            mp_string[pointer] = [word]
            pointer += 1

        for _,val in mp_string.items():
            final_str += str(len(val[0])) + "#" + val[0]
        return final_str

    def decode(self, s: str) -> List[str]:
        res = []
        first_pointer = 0
        while first_pointer < len(s):
            second_pointer = first_pointer
            while s[second_pointer] != '#':
                second_pointer += 1
            length = int(s[first_pointer:second_pointer]) # must be number
            first_pointer = second_pointer + 1
            second_pointer = first_pointer + length
            res.append(s[first_pointer:second_pointer])
            first_pointer = second_pointer
        
        return res

s = Solution()

inputs = ["!@#$%^&*()_+"]

encoded_string = s.encode(inputs)
decoded_string = s.decode(encoded_string)

print(encoded_string)
print(decoded_string)

