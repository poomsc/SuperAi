import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.animation

def createG():
    g = nx.Graph()
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(3, 1)
    g.add_edge(2, 6)
    g.add_edge(2, 7)
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    return 1, g


visited = set()


def DFS(visited, graph, node):
    if node not in visited:
        dfsPath.append(node)
        visited.add(node)
        for child in graph[node]:
            DFS(visited, graph, child)

def makeStepEdge():
    tmp = []
    for i in range(1,len(dfsPath)):
        if dfsPath[i] in graph[dfsPath[i-1]]:
            tmp.append(sorted([dfsPath[i],dfsPath[i-1]]))
        else:
            print(dfsPath[i])
            for j in range(len(dfsPath)):
                tL = sorted([dfsPath[i],dfsPath[j]])
                if dfsPath[j] in graph[dfsPath[i]] and tL not in tmp:
                    tmp.append(tL)
                    break
    return tmp
def toTitle(vis):
    tmp = ""
    for i in range(len(vis)):
        tmp += str(vis[i]) + ', '
    return tmp
startG, graph = createG()
fig, ax = plt.subplots(figsize=(6, 6))

dfsPath = []
DFS(visited, graph, startG)

stepEdge = makeStepEdge()
position = nx.spring_layout(graph)
print("dfsPath : ", dfsPath)
print("stepEdge : ", stepEdge)


def update(num):
    nx.draw(graph, position, with_labels=True)
    ct = num % len(stepEdge)+1
    paths = stepEdge[:ct]
    vis = []
    for i in paths:
        for j in i:
            if i not in vis:
                vis.append(i)
    print(vis)
    nx.draw_networkx_edges(graph, position, edgelist=paths, edge_color='r')
    ax.set_title("Start DFS at node 0", fontweight="bold")
    visText = toTitle(vis)
    ax.set_title(visText, fontweight="bold")
    ax.set_xticks([])
    ax.set_yticks([])


ani = matplotlib.animation.FuncAnimation(
    fig, update, frames=6, interval=1000, repeat=True)
# ani.save('animation.gif', writer='imagemagick', fps=0.5)
plt.show()
