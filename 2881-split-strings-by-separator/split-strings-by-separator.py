class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        result = []
        for word in words:
            parts = word.split(separator)
            for w in parts:
                if w:
                    result.append(w)
        return result