import java.util.*;
class Solution {
    public List<Integer> solution(int[] arr) {
        ArrayList<Integer> newarr = new ArrayList<>();
        for(int a:arr){
            for(int i=0;i<a;i++){
                newarr.add(a);            
            }
        }
        return newarr;
    }
}