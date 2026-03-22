class Solution:
    def spiralOrder(self, matrix):
        if not matrix:
            return []
        
        ans = []
        
        row_start, row_end = 0, len(matrix) - 1
        col_start, col_end = 0, len(matrix[0]) - 1
        
        while row_start <= row_end and col_start <= col_end:
            
            # 1️⃣ Left → Right
            for col in range(col_start, col_end + 1):
                ans.append(matrix[row_start][col])
            row_start += 1
            
            # 2️⃣ Top → Bottom
            for row in range(row_start, row_end + 1):
                ans.append(matrix[row][col_end])
            col_end -= 1
            
            # 3️⃣ Right → Left
            if row_start <= row_end:
                for col in range(col_end, col_start - 1, -1):
                    ans.append(matrix[row_end][col])
                row_end -= 1
            
            # 4️⃣ Bottom → Top
            if col_start <= col_end:
                for row in range(row_end, row_start - 1, -1):
                    ans.append(matrix[row][col_start])
                col_start += 1
        
        return ans