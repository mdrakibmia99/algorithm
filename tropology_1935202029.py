# Name : Md Rakib Mia
# id : 1935202029


from collections import defaultdict

graph = defaultdict(list)
print("Name:Md Rakib Mia\nId:1935202029")
vertex = int(input("Enter vertex size="))
e = int(input("Enter edge size="))
print("Enter value")
for i in range(e):
    # input value
    u, v = map(str, input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    graph[u].append(v)


def topologySort(graph, vertex):
    degree = [0] * vertex
    for node in graph:
        for adj_node in graph[node]:
            degree[adj_node] += 1

    BFS = [i for i in range(vertex) if degree[i] == 0]
    for node in BFS:
        for adj_node in graph[node]:
            degree[adj_node] -= 1
            if degree[adj_node] == 0:
                BFS.append(adj_node)
    return BFS


print("Tropology Sort=", end=" ")
topologySort = topologySort(graph, vertex)
topologySort = [chr(i + 65) for i in topologySort]
print(topologySort)

