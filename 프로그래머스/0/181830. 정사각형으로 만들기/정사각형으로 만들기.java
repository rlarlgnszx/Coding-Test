import java.util.*;
class Solution {
    public int[][] solution(int[][] arr) {
        int rows = arr.length; // 행의 수
        int cols = arr[0].length; // 열의 수

        // 행의 수가 더 많으면 열을 맞추기 위해 0 추가
        if (rows > cols) {
            for (int i = 0; i < rows; i++) {
                int[] newRow = new int[rows];
                System.arraycopy(arr[i], 0, newRow, 0, cols);
                Arrays.fill(newRow, cols, rows, 0);
                arr[i] = newRow; // 새로운 행으로 교체
            }
        }
        // 열의 수가 더 많으면 행을 맞추기 위해 0 추가
        else if (cols > rows) {
            int[][] newArr = new int[rows + (cols - rows)][cols]; // 새로운 배열 생성
            for (int i = 0; i < rows; i++) {
                System.arraycopy(arr[i], 0, newArr[i], 0, cols);
            }
            // 나머지 행은 0으로 채우기
            for (int i = rows; i < newArr.length; i++) {
                for (int j = 0; j < cols; j++) {
                    newArr[i][j] = 0;
                }
            }
            arr = newArr; // 새로운 배열로 교체
        }

        return arr; // 결과 반환
    }
}
