import java.util.*;
import java.util.stream.*;
class Solution {
    public String solution(String myString) {
        return myString.chars()
                .mapToObj(i -> Character.toString(Integer.max(i, 'l')))
                .collect(Collectors.joining());
    }
}