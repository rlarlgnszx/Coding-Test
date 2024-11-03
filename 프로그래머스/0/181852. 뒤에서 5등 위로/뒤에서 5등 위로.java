import java.util.*;
import java.util.stream.*;
 
class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        return IntStream.of(num_list).sorted().skip(5).toArray();
    }
}