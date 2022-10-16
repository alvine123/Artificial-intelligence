
from matplot import pyplot as plt
import network as nx

###Number 1####

def populateGraph():
    # Add All The Nodes To The Graph In their respective postions
        
    

    # Add All The Edges
    # G.add_edge(source, target, weight)
    
    G.add_edge('SportsComplex', 'Siwaka', weight=450)
    G.add_edge('Siwaka', 'Phase1A', weight=10)
    G.add_edge('Siwaka', 'Phase1B', weight=230)
    G.add_edge('Phase1A', 'Phase1B', weight=100)
    G.add_edge('Phase1A', 'Mada', weight=850)
    G.add_edge('Phase1B', 'Phase2', weight=112)
    G.add_edge('Phase1B', 'STC', weight=50)
    G.add_edge('Phase2', 'J1', weight=600)
    G.add_edge('Phase2', 'Phase3', weight=500)
    G.add_edge('STC', 'Phase2', weight=50)
    G.add_edge('STC', 'ParkingLot', weight=250)
    G.add_edge('J1', 'Mada', weight=200)
    G.add_edge('Phase3', 'ParkingLot', weight=350)
    
    G.add_edge('Mada', 'ParkingLot', weight=700)
    
  #
  ## *****************Implemention of Greedy BREADTH FIRST SEARCH************************ ##
      
     def bfs(startNode, goal):
    explored = {}
    frontier = []
    bfs_result = []

    # Add all the nodes in the graph to the explored dictionary
    for node in G.nodes:
        explored[node] = False
    
    # Change the startNode to True in the 'explored' dictionary
    explored[startNode] = True
    frontier.append(startNode) 

    # frontier condition
    while frontier:
        curr_node = frontier.pop(0) # Pop the first element in the list (queue structure)
        bfs_result.append(curr_node)

        if curr_node == goal:
            return bfs_result

        for node in G.neighbors(curr_node):
            if not explored[node]:
                explored[node] = True
                frontier.append(node)

    return False

 def drawBFS():
    # Generate BFS Path From The Sports Complex To Parking Lot
    bfs_path = bfs('SportsComplex', 'ParkingLot')

    if bfs_path == False:
        print('Path Not Found!')
        return 0
    
    print('BFS Traversal Path: ', '->'.join(bfs_path))
    color_map = []
    # For all the nodes in the graph#
    ##assign the color green if part of the path , else assign blue##
    for node in G.nodes:
        if node in bfs_path:
            color_map.append('green')
        else:
            color_map.append('blue')
    
    # Draw the Graph
    pos = nx.get_node_attributes(G, 'pos')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, verticalalignment='bottom')
    nx.draw(G, pos, node_size=2500, node_color=color_map, with_labels=True)
    plt.title('BREADTH FIRST SEARCH TRAVERSAL PATH(GREEN)')
    plt.show() 
    

    # Create A Graph And Assign It To 'G' Variable
 G = nx.Graph()
 populateGraph()

   # Dialogue Options To Choose Which Path The User Wants To See
   isValid = False
   while not isValid:
     choice = input('Enter 1 for BFS Path or 2 for UCS Path: ')
     if choice == '1':
         isValid = True
         drawBFS()
     elif choice == '2':
         isValid = True
         drawUCS()
     else:
         print('Invalid Choice!! Try Again!')
