class Solution:
    def removeDuplicates(self, s: str) -> str:
        s = list(s)
        i = self.duplicates(s)
        while i:
            del s[i:i+2]
            i = self.duplicates(s)
        return "".join(s)

    def duplicates(self, s):
        for i in range(len(s)-1):
            if s[i] == s[i+1]:
                #print(s[i], s[i+1])
                return i
        return None  