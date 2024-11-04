import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int n) {
        List<Integer> array = new ArrayList<>();
        while(n!=1){
            array.add(n);
            if(n%2==0){
                n /= 2;
            }else{
                n = n*3+1;
            }
        }
        array.add(1);
        return array.stream()
            .mapToInt(i->i)
            .toArray();
    }
}