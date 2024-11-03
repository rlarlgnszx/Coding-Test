class Solution {
    public int solution(double flo) {
        return (int) Math.floor(flo);
    }

    public static void main(String[] args) {
        Solution sol = new Solution();
        System.out.println(sol.solution(1.42));  // 출력: 1
        System.out.println(sol.solution(69.32)); // 출력: 69
    }
}