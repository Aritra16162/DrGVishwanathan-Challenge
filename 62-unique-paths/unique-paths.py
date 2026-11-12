class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}
        stack = [(0, 0)]

        while stack:
            i, j = stack[-1]         
            if (i, j) in memo:
                stack.pop()
                continue

            
            if i == m - 1 and j == n - 1:
                memo[(i, j)] = 1
                stack.pop()
                continue

            down, right = (i + 1, j), (i, j + 1)
            pending = False

            
            if i + 1 < m and down not in memo:
                stack.append(down)
                pending = True
            if j + 1 < n and right not in memo:
                stack.append(right)
                pending = True

            if pending:
                continue              

            
            total = 0
            if i + 1 < m:
                total += memo[down]
            if j + 1 < n:
                total += memo[right]
            memo[(i, j)] = total
            stack.pop()

        return memo[(0, 0)]