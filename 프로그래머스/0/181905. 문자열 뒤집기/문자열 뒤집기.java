class Solution {
    public String solution(String my_string, int s, int e) {
        // s부터 e까지의 부분 문자열을 추출하고 뒤집기
        String reversed = new StringBuilder(my_string.substring(s, e + 1)).reverse().toString();

        // 앞부분, 뒤집힌 부분, 뒷부분을 합쳐 최종 문자열 생성
        return my_string.substring(0, s) + reversed + my_string.substring(e + 1);
    }

}