# Name:MD Rakib Mia
#id:1935202029

print("Name:Md Rakib Mia \nId:1935202029")
Graph_Value = {
   '1':['2','4'],
    '2':['1','3','4'],
    '3':['4','4'],
    '4':['1','2','3','5'],
    '5':['4']
}
visited_node= set()

def DFS_funcion(visited_node, Graph_Value, node):
    if node not in visited_node:
        print(node,end="  ")
        visited_node.add(node)
        for child in Graph_Value[node]:
            DFS_funcion(visited_node,Graph_Value,child)

DFS_funcion(visited_node,Graph_Value,'4')
