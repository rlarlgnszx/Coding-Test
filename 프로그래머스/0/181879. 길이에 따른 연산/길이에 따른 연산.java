import java.util.*;
import java.util.stream.*;
class Solution {
    public int solution(int[] num_list) {
        IntStream stream = IntStream.of(num_list);
        return num_list.length>10?stream.sum():stream.reduce(1, (a, b) -> a * b);
    }
}