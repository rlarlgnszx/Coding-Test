import java.util.*;
class Solution {
    public int[] solution(int brown, int yellow) {
        List<Integer> divr = soin(yellow);
        int first=0;
        int last = divr.size()-1;
        while (brown+yellow != (divr.get(first)+2)*(divr.get(last)+2)){
            first++;
            last--;
            if(first>last){
                break;
            }
        }
        int[] answer = {divr.get(last)+2,divr.get(first)+2};
        return answer;
    }
    
    public List<Integer> soin(int a){
        List<Integer> div = new ArrayList<>();
        for(int i=1;i*i <= a; i++){
            if(a%i ==0){
                div.add(i);
                if( i!= a/i){
                    div.add(a/i);
                }
            }
        }
        Collections.sort(div);
        return div;
    }
}