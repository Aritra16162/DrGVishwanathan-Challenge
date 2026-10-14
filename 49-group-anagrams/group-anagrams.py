class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        group = {}

        for word in strs:
            sort = ''.join(sorted(word))

            if sort not in group:
                group[sort] = []

            group[sort].append(word)

        return list(group.values())