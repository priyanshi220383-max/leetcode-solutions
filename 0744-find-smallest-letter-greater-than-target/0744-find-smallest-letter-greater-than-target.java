class Solution {
    public char nextGreatestLetter(char[] letters, char target) {
        int left = 0;
        int right = letters.length - 1;
        while (left <= right) {
            int mid = left + (right - left) /2;
           
            if (letters[mid] > target) {
                right = mid - 1;
            }
            else {
                left = mid  + 1;
            }
        }
           // Left points to the smallest letter greater than target
        // If left reaches the end, wrap around to the first letter
        return letters[left % letters.length];
        
    }
}