import java.util.*;
import java.util.stream.*;

 class Solution {
        public int[] solution(int[] arr) {
            int i = 0;
            List<Integer> stk = new ArrayList<>();
            while (i < arr.length) {
                if (stk.isEmpty()) {
                    stk.add(arr[i]);
                    i++;
                } else if (stk.get(stk.size() - 1).equals(arr[i])) {
                    stk.remove(stk.size() - 1);
                    i++;
                } else {
                    stk.add(arr[i]);
                    i++;
                }
            }
            if (stk.isEmpty()) {
                return new int[]{-1};
            }
            return stk.stream().mapToInt(Integer::intValue).toArray();
        }
    }