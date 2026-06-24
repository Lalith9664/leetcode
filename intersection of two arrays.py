class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # l1=sorted(set(nums1))
        # l2=sorted(set(nums2))

        # i=0
        # j=0

        # inter=[]

        # while i<len(l1) and j<len(l2):
        #     if l1[i]==l2[j]:
        #         inter.append(l1[i])
        #         i+=1
        #         j+=1
        #     elif l1[i]<l2[j]:
        #         i+=1
        #     else:
        #         j+=1
        # return inter
        return list(set(nums1) & set(nums2))