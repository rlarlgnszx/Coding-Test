import java.util.*;
import java.util.stream.*;
class Solution {
    public int[] solution(int[] arr) {
        int a = 1;
        while (arr.length > a){
            a *=2;
        }
        int[] answer = new int[a];
        
        for(int i=0;i<a;i++){
            if(i<arr.length){
                answer[i] = arr[i];
            }
            else{
                answer[i]=0;
            }
        }
        return answer;
    }
}