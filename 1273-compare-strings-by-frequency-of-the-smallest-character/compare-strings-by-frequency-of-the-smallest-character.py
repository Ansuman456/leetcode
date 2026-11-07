class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:

        def getFrequency(s):
            smallest = min(s)
            return s.count(smallest)

        # Calculate and sort word frequencies
        word_freq = [getFrequency(w) for w in words]
        word_freq.sort()

        ans = []
        # Process each query
        for q in queries:
            target = getFrequency(q)
            low = 0
            high = len(word_freq)

            # Find first element > target(upper bound)
            while low < high:
                mid = low + (high - low) // 2
                if word_freq[mid] <= target:
                    low = mid + 1
                else:
                    high = mid

            ans.append(len(word_freq) - low)
        return ans