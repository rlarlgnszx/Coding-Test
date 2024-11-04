class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        return my_string.startsWith(is_prefix)==true?1:0;
    }
}