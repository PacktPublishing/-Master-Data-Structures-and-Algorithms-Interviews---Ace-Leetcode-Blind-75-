class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""

        # Store window and t characters frequency in hashmap.
        wmap, tmap = {}, {}

        for char in t:
            tmap[char] = tmap.get(char, 0) + 1

        # How many we've covered in the current window and Number of unique characters in t.
        have, need = 0, len(tmap)

        # Two pointers for the sliding window.
        start, end = 0, 0

        # Placeholder for the result.
        min_len = float("inf")
        result = ""

        while end < len(s):
            char = s[end]

            wmap[char] = wmap.get(char, 0) + 1

            # If the frequency of current char matches desired frequency, increment have.
            if char in tmap and wmap[char] == tmap[char]:
                have += 1

            # Try to shrink the window.
            while start <= end and have == need:
                char = s[start]

                # Update result if this window is smaller.
                current_window = end - start + 1
                if current_window < min_len:
                    min_len = current_window
                    result = s[start:end+1]

                # Update map and compare them.
                wmap[char] -= 1
                if char in tmap and wmap[char] < tmap[char]:
                    have -= 1

                # Move the start pointer.
                start += 1

            # Move the end pointer.
            end += 1

        return result
    

#Question: https://leetcode.com/problems/minimum-window-substring
#Blog: https://blog.unwiredlearning.com/minimum-window-substring