import java.util.*;
import java.util.stream.*;
class Solution {
    public String[] solution(String[] picture, int k) {
        List<String> a = new ArrayList<>();
        for(int i=0;i<picture.length;i++){
            String query = picture[i];
            String change = Arrays.stream(query.split("")).map(
                s-> s.repeat(k)
            ).collect(Collectors.joining());
            for(int f=0;f<k;f++){
                a.add(change);
            }
        }
        return a.toArray(new String[0]);
    }
}