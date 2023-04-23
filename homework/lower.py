N, X = map(int, input().split())
A = list(map(int, input().split()))

for l in range(N):
    if A[l] < X:
        print(A[l], end=" ")
        
#10871