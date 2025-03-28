from typing import List
import heapq

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        rows, cols = len(grid), len(grid[0])
        sorted_queries = sorted(enumerate(queries), key=lambda x: x[1])  # Sort queries
        result = [0] * len(queries)
        
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
        min_heap = [(grid[0][0], 0, 0)]  # Min-Heap (value, row, col)
        visited = set()
        visited.add((0, 0))
        count = 0

        for idx, value in sorted_queries:
            while min_heap and min_heap[0][0] < value:
                _, r, c = heapq.heappop(min_heap)
                count += 1  # Increase point count

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        heapq.heappush(min_heap, (grid[nr][nc], nr, nc))
                        visited.add((nr, nc))
            
            result[idx] = count  # Store result

        return result
