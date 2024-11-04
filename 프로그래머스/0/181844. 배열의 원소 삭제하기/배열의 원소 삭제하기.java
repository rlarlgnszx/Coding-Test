import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int[] arr, int[] delete_list) {
        List<Integer> deleteList = Arrays.stream(delete_list)
                                          .boxed() // int를 Integer로 변환
                                          .collect(Collectors.toList());
        
        return Arrays.stream(arr) // arr을 스트림으로 변환
                     .filter(num -> !deleteList.contains(num)) // delete_list에 포함되지 않은 원소 필터링
                     .toArray(); // 결과를 int[] 배열로 변환
    }
}