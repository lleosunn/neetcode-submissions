class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # dict with keys as numbers and values as counts of that number o(n)
        # keep track of largest values
        # list indices (count) to the number with that count o(n)
        # walk backwards
        bucket = dict()
        counts = [[]] * (len(nums) + 1)
        output = []

        for num in nums:
            if num in bucket:
                bucket[num] += 1
            else:
                bucket[num] = 1
        
        for key, value in bucket.items(): # key is number, value is count
            print(counts)
            counts[value] += [key]
        
        counts.reverse()
        print(counts)
        # counter = 0
        # for i in counts:
        #     if i != []:
        #         for j in i:
        #             output.append(j)
        #             counter += 1
        #             if counter == k:
        #                 return output

