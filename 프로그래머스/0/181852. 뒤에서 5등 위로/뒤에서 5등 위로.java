import java.util.*;

class Solution {
    public int[] solution(int[] num_list) {
        int[] answer = {};
        return Arrays.stream(num_list).sorted().skip(5).toArray();
    }
}