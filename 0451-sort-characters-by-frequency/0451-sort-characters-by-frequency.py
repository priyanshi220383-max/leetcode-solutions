class Solution(object):
    def frequencySort(self, s):
        freq = {}

        # Count frequency
        for ch in s:
            if ch in freq:
                freq[ch] += 1
            else:
                freq[ch] = 1

        # Sort by frequency
        sorted_chars = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        result = ""

        # Build answer
        for ch, count in sorted_chars:
            result += ch * count

        return result