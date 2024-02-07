class Solution:
    def isValid(self, s: str) -> bool:
        splitted_string = [*s]
        parantheses_dict = {
            "]": "[",
            "}": "{",
            ")": "("
        }
        temp_list = []
        index = 1

        
        if len(splitted_string) == 1:
            return False
        
        temp_list.append(splitted_string[0])
        while index <= len(splitted_string[1:]):
            char = splitted_string[index]
            if temp_list == [] or parantheses_dict.get(char) != temp_list[-1]:
                temp_list.append(char)
            else:
                temp_list.pop()
            index += 1

        if len(temp_list) >= 1:
            return False
        return True
                

# string = "(]"
# s = Solution()
# print(s.isValid(string))

