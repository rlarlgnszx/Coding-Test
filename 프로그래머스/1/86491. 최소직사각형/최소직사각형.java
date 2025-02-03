// import java.util.Math;
class Solution {
    public int solution(int[][] sizes) {
        int answer = 0;
        int left=sizes[0][0];
        int right=sizes[0][1];
        for(int i=1;i<sizes.length;i++){
            int l =  sizes[i][0];
            int r = sizes[i][1];
            if ((Math.abs(left-l)+Math.abs(right-r))>(Math.abs(left-r)+Math.abs(right-l))){
                left= Math.max(left,r);
                right = Math.max(right,l);
            }else{
                left = Math.max(left,l);
                right= Math.max(right,r);
            }
        }
        // 7 5    7 5
        // 8 4    4 8
        
        System.out.println(left);
        System.out.println(right);
        answer = left *right;
        return answer;
    }
}