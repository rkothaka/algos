from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        def cycle_length(start: int):
            l = 1
            current = edges[start]
            while current != start:
                l += 1
                current = edges[current]
            return l

        visited = {}
        n = len(edges)
        longest = -1

        for i in range(n):
            if i in visited:
                continue
            current_path = set()
            current_cycle_length = -1
            current_path.add(i)

            next_node = edges[i]
            while True:
                if next_node == -1:
                    break
                elif next_node in visited:
                    current_cycle_length = visited[next_node]
                    break
                elif next_node in current_path:  # cycle detected, check cycle length
                    current_cycle_length = cycle_length(next_node)
                    break
                else:
                    current_path.add(next_node)
                    next_node = edges[next_node]

            for node in current_path:
                visited[node] = current_cycle_length
            longest = max(longest, current_cycle_length)

        return longest


import ast

# Specify the file path
file_path = 'testcase'

# Read the content of the file
with open(file_path, 'r') as file:
    file_content = file.read()

# Safely parse and load the array using ast.literal_eval
edges = []
try:
    edges = ast.literal_eval(file_content)
except (SyntaxError, ValueError) as e:
    print(f"Error loading array: {e}")


solution = Solution()
print(solution.longestCycle(edges))
