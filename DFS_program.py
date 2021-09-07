'''
Graph_Value = {
    'A': ['B', 'F'],
    'B': ['H'],
    'C': [],
    'D':['E','I','C','H'],
    'E':['I'],
    'F':[],
    'G':['A','C'],
    'H':[],
    'I':['C'],
    'J':['E']

     '1':['2','4'],
    '2':['3','4'],
    '3':[],
    '4':['3','5'],
    '5':[]
}
'''
Graph_Value = {
   '1':['2','4'],
    '2':['1','3','4'],
    '3':['4','4'],
    '4':['1','2','3','5'],
    '5':['4']
}
visited_node= set()

def DFS_funcion(visited_node,Graph_Value,node):
    if node not in visited_node:
        print(node)
        visited_node.add(node)
        for child in Graph_Value[node]:
            DFS_funcion(visited_node,Graph_Value,child)

DFS_funcion(visited_node,Graph_Value,'4')

