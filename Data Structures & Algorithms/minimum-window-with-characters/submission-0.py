class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        need = {}

        for ch in t:
            need[ch] = need.get(ch, 0) + 1

        h = {}

        left = 0
        right = 0

        c = len(t)

        mini = float('inf')
        start = 0

        while right < len(s):

            h[s[right]] = h.get(s[right], 0) + 1

            # Character is needed and we haven't exceeded
            # the required frequency
            if s[right] in need and h[s[right]] <= need[s[right]]:
                c -= 1

            # Window contains all characters of t
            while c == 0:

                if right - left + 1 < mini:
                    mini = right - left + 1
                    start = left

                # Remove left character
                h[s[left]] -= 1

                if s[left] in need and h[s[left]] < need[s[left]]:
                    c += 1

                if h[s[left]] == 0:
                    del h[s[left]]

                left += 1

            right += 1

        if mini == float('inf'):
            return ""

        return s[start:start + mini]