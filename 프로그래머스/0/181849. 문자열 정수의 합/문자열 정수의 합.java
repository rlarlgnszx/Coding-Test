class Solution {
    public int solution(String num_str) {
        int answer = 0;
        String[] a = num_str.split("");
        for(String c:a){
            answer += Integer.parseInt(c);
        }
        return answer;
    }
}