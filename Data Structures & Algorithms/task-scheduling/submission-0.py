class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # num cycles * idle + remaining
        # (maxfreq - 1)*(n+1)+num_of_max_freq_elements
        maxfreq = 0
        num_of_max_freq_elements = 0
        freq = defaultdict(int)
        for i in tasks:
            freq[i] += 1
        for j in freq:
            maxfreq = max(freq[j], maxfreq)
        for k in freq:
            if freq[k] == maxfreq:
                num_of_max_freq_elements += 1
        return max(len(tasks), (maxfreq-1)*(n+1)+num_of_max_freq_elements)
        