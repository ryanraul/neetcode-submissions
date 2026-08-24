"""
nums1 = [10,20,20,40,0,0], m = 4, 
         n1   nf    
nums2 = [1,2], n = 2
           n2
"""


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        n1_ptr = m - 1
        n2_ptr = n - 1
        nf_ptr = (m+n)-1

        while n1_ptr >= 0 and n2_ptr >= 0:
            if(nums1[n1_ptr] > nums2[n2_ptr]):
                nums1[nf_ptr] = nums1[n1_ptr]
                n1_ptr-=1
            else:
                nums1[nf_ptr] = nums2[n2_ptr]
                n2_ptr-=1
            nf_ptr-=1

        while n2_ptr >= 0:
            nums1[nf_ptr] = nums2[n2_ptr]
            nf_ptr, n2_ptr = nf_ptr-1, n2_ptr-1


