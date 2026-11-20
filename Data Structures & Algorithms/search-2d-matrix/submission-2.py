class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left, right = 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2

            if matrix[mid][0] <= target and target <= matrix[mid][-1]:
                return self.binarySearch(matrix[mid], target)
            elif matrix[mid][0] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def binarySearch(self, array, target):
        left, right = 0, len(array) - 1

        while left <= right:
            mid = (left + right) // 2

            if array[mid] == target:
                return True
            elif array[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return False

            