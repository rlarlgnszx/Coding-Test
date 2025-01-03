class Solution {
    public int[] solution(String my_string) {
            int[] count = new int[52];
            for (char c : my_string.toCharArray()) {
                if (c >= 'A' && c <= 'Z') {
                    count[c - 'A']++;
                } else if (c >= 'a' && c <= 'z') {
                    count[c - 'a' + 26]++;
                }
            }
            return count;
    }
}