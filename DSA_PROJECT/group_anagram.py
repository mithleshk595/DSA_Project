class solution:
    def sortString(self, s):
        s1 = list(s)
        s1.sort()
        return "".join(s1)
    
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        dict1 = {}

        for s in strs:
            key = self.sortString(s)
            if key not in dict1:
                dict1[key] = [s]
            else:
                dict1[key].append(s)

        return list(dict1.values())
    
    
