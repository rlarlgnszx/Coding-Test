import java.util.*;
import java.util.stream.*;
class Solution {
     public int solution(String[] strArr) {
            int answer = 0;
            Map<Integer, List<String>> arr = Arrays.stream(strArr)
                    .collect(Collectors.groupingBy(String::length));
            answer = arr.values().stream().mapToInt(List::size).max().orElse(0);
            return answer;
        }
}