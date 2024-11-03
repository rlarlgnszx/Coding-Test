import java.util.*;
class Solution {
    public String[] solution(String my_string) {
        List<String> answer = new ArrayList<>();
        String[] arr = my_string.split(" ");
        for(String item:arr){
            item = item.replace(" ","");
            if(item.length()>0){
                answer.add(item);
            }
        }
        return  answer.toArray(new String[0]);
    }
}