class Solution:
    def largest_rectangle(self, heights, heights_len):
        stack = [-1]
        max_area = 0
        if heights_len==0: 
            return 0 
        elif heights_len==1:     
            return heights[0] 

        for idx in range(heights_len): 
            while stack[-1] != -1 and heights[idx]<=heights[stack[-1]]: 
                pop_idx = stack.pop()
                area = (idx-stack[-1]-1)* heights[pop_idx]
                if max_area<area:
                    max_area = area
            stack.append(idx)    

        while stack[-1] != -1:  
            pop_idx = stack.pop()
            area = (heights_len-stack[-1]-1)* heights[pop_idx]
            if max_area<area:
                max_area = area
        return max_area


    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        rows_num = len(matrix)
        if rows_num == 0: 
            return 0
        cols_num = len(matrix[0])
        maximal_rec_area = 0
        heights = [0 for _ in range(cols_num)]
        for i in range(rows_num): 
            for j in range(cols_num): 
                if matrix[i][j] == "0": 
                    heights[j] = 0
                elif matrix[i][j] == "1":     
                    heights[j] += 1 
            area = self.largest_rectangle(heights, cols_num)        
            # print(area)
            if maximal_rec_area<area:
                maximal_rec_area = area
        return maximal_rec_area