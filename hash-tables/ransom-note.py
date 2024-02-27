class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ransomNoteDict = {}

        for c in ransomNote:
            ransomNoteDict[c] = ransomNoteDict.get(c, 0) + 1

        for c in magazine:
            if c in ransomNoteDict:
                ransomNoteDict[c] = ransomNoteDict.get(c) - 1


        # if value == 0 or value < 0, it means all the character in ransomNote 
        # can be constructed from magazine
        return all(values <= 0 for values in ransomNoteDict.values())
        

s = Solution()
ransomNote = "aa"
magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"

print(s.canConstruct(ransomNote, magazine))