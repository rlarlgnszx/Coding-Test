import java.util.*;
import java.util.stream.*;
class Solution {
    public String[] solution(String[] strArr) {
        List<String> answer = new ArrayList<>();
        for(String arr:strArr){
            if(!arr.contains("ad")){
                answer.add(arr);
            }
        }
        return answer.toArray(new String[0]);
    }
}