class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        return Integer.max(Integer.parseInt(String.valueOf(a)+String.valueOf(b)),Integer.parseInt(String.valueOf(b)+String.valueOf(a)));
    }
}