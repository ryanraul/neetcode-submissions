public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        // two arrays prefix an suffix
        // [1,2,4,6] -> [1,2,8,16]
        // [1,2,4,6] -> [48,48,24,6]

        var numsQuantity = nums.Length;
        int[] prefix = new int[numsQuantity];
        int[] suffix = new int[numsQuantity];

        int lastAdded = -1;
        for(int i = 0; i < numsQuantity; i++){
            if(i==0)
                prefix[i] = nums[i];
            else 
                prefix[i] = lastAdded * nums[i];
           
            lastAdded = prefix[i];
        }

        for(int i = numsQuantity - 1; i > 0; i--){
            if(i==(numsQuantity - 1))
                suffix[i] = nums[i];
            else
                suffix[i] = lastAdded * nums[i];
            
            lastAdded = suffix[i];
        }

        var products = new int[numsQuantity];
        int prefixAux;
        int suffixAux;
        for(int i = 0; i < numsQuantity; i++){
            prefixAux = (i-1) < 0 ? 1 : prefix[i-1];
            suffixAux = (i+1) > (numsQuantity-1) ? 1 : suffix[i+1];

            var productResult = prefixAux * suffixAux;
            products[i] = productResult;
        }

        return products;
    }
}
