class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Edge case: if the grid is empty, return 0 islands
        if not grid or not grid[0]:
            return 0

        # Dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        # Helper function for DFS traversal
        def dfs(r, c):
            # If out of bounds or current cell is water, return
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the current cell as water to avoid re-visiting
            grid[r][c] = 'W'
            # Visit all connected cells (up, down, left, right)
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        # Main loop to find islands
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':  # Found a new island
                    num_islands += 1
                    dfs(r, c)  # Start DFS to mark the entire island

        return num_islands
        