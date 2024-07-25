import sys
input = sys.stdin.readline
a = input().strip()
b = input().strip()

def lcs(A, B):
    m = len(A)
    n = len(B)

    # (m+1) x (n+1) 크기의 2차원 배열 초기화
    L = [[0] * (n + 1) for _ in range(m + 1)]

    # L 배열 채우기
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if A[i - 1] == B[j - 1]:  # 문자가 같을 경우
                L[i][j] = L[i - 1][j - 1] + 1
            else:  # 문자가 다를 경우
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # LCS 길이
    lcs_length = L[m][n]
    return lcs_length  # LCS 길이 반환
    # LCS 길이
print(lcs(a,b))
