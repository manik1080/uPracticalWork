r'''On the upcoming conference were sent M representatives of country A and N representatives of country B (M and N ≤ 1000).
The representatives were identified with 1, 2… M for country A and 1, 2… N for country B. Before the conference K pairs of
representatives were chosen. Every such pair consists of one member of delegation A and one of delegation B. If there exists
a pair in which both member #i of A and member #j of B are included then #i and #j can negotiate. Everyone attending the
conference was included in at least one pair. The CEO of the congress center wants to build direct telephone connections
between the rooms of the delegates, so that everyone is connected with at least one representative of the other side, and
every connection is made between people that can negotiate. The CEO also wants to minimize the amount of telephone connections.
Write a program which given M, N, K and K pairs of representatives, finds the minimum number of needed connections.

The first line of the input contains M, N and K. The following K lines contain the chosen pairs in the form of two integers p1 and p2,
p1 is member of A and p2 is member of B. The output should contain the minimum number of needed telephone connections.

Sample Input/Output:
input: 
3 2 4
1 1
2 1
3 1
3 2
output: 3
'''

n, m, k = map(int, input().split())
graph = [[0]*(m+1) for _ in range(n+1)]

for _ in range(k):
    s, t = map(int, input().split())
    graph[s][t] = 1

visited = []
link = [0] * (m+1)
max_matching = 0

def find_augmenting_path(node, visited):
    for neighbor in range(1, m+1):
        if not visited[neighbor] and graph[node][neighbor]:
            visited[neighbor] = True
            if link[neighbor] == 0 or find_augmenting_path(link[neighbor], visited):
                link[neighbor] = node
                return True
    return False

for node in range(1, n+1):
    visited = [False] * (m+1)
    if find_augmenting_path(node, visited):
        max_matching += 1

print(n + m - max_matching)
