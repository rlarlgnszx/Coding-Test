import java.util.*;

class Solution {
    public int solution(int[][] jobs) {
        // 작업 요청 시각과 소요 시간을 저장할 큐
        PriorityQueue<int[]> jobQueue = new PriorityQueue<>(
            (a, b) -> a[0] == b[0] ? a[1] - b[1] : a[0] - b[0] // 요청 시각이 같으면 소요 시간으로 정렬
        );
        
        // 초기 작업을 큐에 추가
        for (int[] job : jobs) {
            jobQueue.add(job);
        }
        
        // 현재 시간, 총 대기 시간, 처리한 작업 수
        int currentTime = 0;
        int totalWaitTime = 0;
        int completedJobs = 0;

        // 대기 중인 작업을 처리할 우선 순위 큐
        PriorityQueue<int[]> processingQueue = new PriorityQueue<>(
            (a, b) -> a[1] - b[1] // 소요 시간을 기준으로 정렬
        );

        while (!jobQueue.isEmpty() || !processingQueue.isEmpty()) {
            // 현재 시간에 도착한 작업을 processingQueue로 이동
            while (!jobQueue.isEmpty() && jobQueue.peek()[0] <= currentTime) {
                processingQueue.add(jobQueue.poll());
            }

            // processingQueue가 비어있지 않으면 작업을 수행
            if (!processingQueue.isEmpty()) {
                int[] currentJob = processingQueue.poll();
                currentTime += currentJob[1]; // 작업 소요 시간만큼 현재 시간 증가
                totalWaitTime += currentTime - currentJob[0]; // 대기 시간 계산
                completedJobs++;
            } else {
                // processingQueue가 비어있고 jobQueue에 작업이 남아있다면
                // 다음 작업 요청 시각으로 현재 시간을 이동
                currentTime = jobQueue.peek()[0];
            }
        }

        return totalWaitTime / completedJobs; // 평균 대기 시간 반환
    }
}
