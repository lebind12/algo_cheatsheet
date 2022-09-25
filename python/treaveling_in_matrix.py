import sys


N = 4
# 행렬에서 원소를 기준으로 전후 좌우 확인하면서
# 행렬의 모든 원소를 순회하는 코드
# 예시로 4 x 4 크기의 행렬이고 0부터 15까지 값이 들어가 있음
matrix = [[] for _ in range(N)]
n = 0
for x in range(N):
    for _ in range(N):
        matrix[x].append(n)
        n += 1

# 상하 좌우 이동 값
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for x in range(N):
    for y in range(N):
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 상하좌우 좌표 값이 행렬의 범위를 초과하지 않는다면
            if nx >= 0 and nx < N and ny >= 0 and ny < N:
                print(matrix[nx][ny])