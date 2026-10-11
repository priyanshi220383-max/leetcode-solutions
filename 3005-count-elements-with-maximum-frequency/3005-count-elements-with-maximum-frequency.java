class Solution {
    public int maxFrequencyElements(int[] nums) {
        int[] freq = new int[101];
        for (int num: nums){
            freq[num]++;
        }
        int maxfreq = 0;
        for(int count : freq){
            maxfreq = Math.max(maxfreq, count);
        }
        int total = 0;

        for (int count : freq){
            if (count == maxfreq){
                total += count;
            }
        }
        return total;
        
    }
}