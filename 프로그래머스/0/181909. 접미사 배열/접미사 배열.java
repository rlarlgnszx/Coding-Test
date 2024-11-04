import java.util.*;
class Solution {
    public String[] solution(String my_string) {
        List<String> answer = new ArrayList<>();
        StringBuilder sb = new StringBuilder();
        for(int i=my_string.length()-1;i>=0;i-=1){
            sb.insert(0,my_string.charAt(i));
            answer.add(sb.toString());
        }
        Collections.sort(answer);
        return answer.toArray(new String[0]);
    }
}