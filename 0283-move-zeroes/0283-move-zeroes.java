// class Solution {
//     public void moveZeroes(int[] nums) {
//         int i = 0;
//         for (int j = 0; j < nums.length ;j++){

//         if (nums[j] != 0){
//             int temp = nums[i];
//             nums[i] = nums[j];
//             nums[j] = temp;
//             i++;
//         }
//         }
        
//     }
// }
// brute force approach
class Solution {
     public void moveZeroes(int[] nums) {

            int index = 0;

            for (int j = 0; j < nums.length; j++){
                if (nums[j] != 0) {
                    nums[index] = nums[j];
                    index++;
                }
            }
            while (index < nums.length){
                nums[index] = 0;
                index++;
            }

        }
     }
     //2 phase