class Solution {
    public int solution(int n, String control) {
        int answer = n;
        String[] list = control.split("");
        for(String a:list){
            if(a.equals("w")){
                answer +=1;
            }else if(a.equals("s")){
                answer -=1;
            }else if(a.equals("d")){
                answer +=10;
            }else{
                answer -=10;
            }
        }
        return answer;
    }
}