"""
two pointers
w1_ptr
w2_ptr
final_size = len(w1) + len(w2)

ab + abbxxc = 8
      ^  
aabbbxxc

while wf_ptr < final_size:
    if(w1_ptr < w1_size):
        wf[wf_ptr] = w1[w1_ptr]
        w1_ptr+=1
        wf_ptr+=1
    
    if(w2_ptr < w2_size):
        wf[wf_ptr] = w2[w2_ptr]
        w2_ptr+=1
        wf_ptr+=1
"""

class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        w1_ptr = 0
        w2_ptr = 0
        wf_ptr = 0
        w1_size = len(word1)
        w2_size = len(word2)
        final_size = w1_size + w2_size
        w1 = list(word1)
        w2 = list(word2)
        wf = []

        while wf_ptr < final_size:
            if(w1_ptr < w1_size):
                wf.append(w1[w1_ptr])
                w1_ptr+=1
                wf_ptr+=1

            if(w2_ptr < w2_size):
                wf.append(w2[w2_ptr])
                w2_ptr+=1
                wf_ptr+=1

        return "".join(wf)


