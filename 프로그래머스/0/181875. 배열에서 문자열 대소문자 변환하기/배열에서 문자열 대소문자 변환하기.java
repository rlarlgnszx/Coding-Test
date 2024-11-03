class Solution {
    public String[] solution(String[] strArr) {
        String[] answer = {};
        int i=0;
        for(String arr: strArr){
            if(i%2==0){
                strArr[i]=arr.toLowerCase();
            }else{
                strArr[i]=arr.toUpperCase();
            }
            i++;
        }
        return strArr;
    }
}