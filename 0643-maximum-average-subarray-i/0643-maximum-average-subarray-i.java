class Solution {
    public double findMaxAverage(int[] nums, int k) {
        int currentsum = 0;
        for (int i = 0; i < k;i++){
            currentsum += nums[i];
        }
        int maxsum = currentsum;
        for (int i = k; i< nums.length; i++){
            currentsum = currentsum - nums[i-k] + nums[i];
            maxsum = Math.max(maxsum, currentsum);
        }
        return(double) maxsum /k;
        
    }
}