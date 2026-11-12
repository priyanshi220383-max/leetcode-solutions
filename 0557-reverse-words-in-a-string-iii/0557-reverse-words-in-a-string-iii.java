class Solution {
    public String reverseWords(String s) {
        char[] arr = s.toCharArray();
        int left = 0;

        for(int i = 0; i < s.length(); i++){
            if (arr[i] == ' ' || i == arr.length - 1){
                int right = (arr[i] == ' ') ? i - 1 : i;
                while (left < right) {
                    char temp = arr[left];
                    arr[left] = arr[right];
                    arr[right] = temp;
                    left++;
                    right--;
                }
                left = i + 1;
            }
        }
        return new String(arr);


        
    }
}