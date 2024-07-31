class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        rows = len(image)
        col = len(image[0])
        for row in image:
            row.reverse()
        for r in range(rows):
            for c in range(col):
                if image[r][c] == 1:
                    image[r][c] = 0
                else:
                    image[r][c] = 1
        return image

