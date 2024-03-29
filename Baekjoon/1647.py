'''
'도시 분할 계획'
'''
# 24.02.19 공부
# import sys
# input = sys.stdin.readline
#
#
# def find_parent(x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
#     return parent[x]
#
#
# def union(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# N, M = map(int, input().split())
#
# parent = list(range(N+1))
# edges = []
#
# for i in range(M):
#     A, B, C = map(int, input().split())
#     edges.append([A,B,C])
# edges.sort(key=lambda x: x[2])
#
# answer = 0
# last_edge = 0
# for a, b, c in edges:
#     if find_parent(a) != find_parent(b):
#         union(a, b)
#         answer += c
#         last_edge = c
#
# print(answer - last_edge)


# 24.02.21(복습~)
# import sys
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
# graph = []
# for i in range(M):
#     graph.append(list(map(int, input().split())))
#
# graph.sort(key = lambda x:x[2])
#
#
# def find_parent(x):
#     if parent[x] != x:
#         parent[x] = find_parent(parent[x])
#     return parent[x]
#
#
# def union(a, b):
#     a = find_parent(a)
#     b = find_parent(b)
#     if a < b:
#         parent[b] = a
#     else:
#         parent[a] = b
#
#
# parent = list(range(N+1))
# answer = 0
# last_edge = 0
# for i in range(M):
#     a, b, c = graph[i]
#     if find_parent(a) == find_parent(b):
#         continue
#     union(a, b)
#     answer += c
#     last_edge = c
#
# print(answer - last_edge)

# 24.03.09 복습2~
def find_parent(x):
    if parent[x] != x:
        parent[x] = find_parent(parent[x])
    return parent[x]

def union(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
graph = []
for i in range(M):
    graph.append(list(map(int, input().split())))

parent = list(range(N+1))

answer = 0
last = 0
graph.sort(key=lambda x:x[2])
for i in range(M):
    a, b, c = graph[i]
    if find_parent(a) != find_parent(b):
        answer += c
        union(a, b)
        last = c

print(answer - last)
