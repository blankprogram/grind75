class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image;

        self.dfs(image,sr,sc,color,image[sr][sc])
        return image
    
    def dfs(self, image, sr, sc, color, pixel):
        stack = [(sr, sc)]
        while stack:
            r, c = stack.pop()
            if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == pixel:
                image[r][c] = color
                stack.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])







        