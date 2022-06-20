def determineRiverSizes(matrix):
    riverSizes = []
    visitedNodes = [[False for _ in row] for row in matrix]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if visitedNodes[i][j]:
                continue

            traverseNode(i, j, matrix, visitedNodes, riverSizes)

    return riverSizes

def traverseNode(i, j, matrix, visitedNodes, riverSizes):
    currentRiverSize = 0

    nodesToVisit = [[i, j]]
    while len(nodesToVisit):
        currentNode = nodesToVisit.pop()
        
        i = currentNode[0]
        j = currentNode[1]

        if visitedNodes[i][j]:
            continue

        visitedNodes[i][j] = True

        if matrix[i][j] == 0:
            continue

        currentRiverSize += 1

        unvisitedNeighbours = getUnvisitedNeighbours(i, j, matrix, visitedNodes)

        for neighbour in unvisitedNeighbours:
            nodesToVisit.append(neighbour)

    if currentRiverSize > 0:
        riverSizes.append(currentRiverSize)
        
def getUnvisitedNeighbours(i, j, matrix, visitedNodes):
    unvisitedNeighbours = []

    # Top neighbour coordinates.
    if i > 0 and j < len(matrix[i - 1]) and not visitedNodes[i - 1][j]:
        unvisitedNeighbours.append([i - 1, j])
    # Bottom neighbour coordinates.
    if i < len(matrix) - 1 and j < len(matrix[i + 1]) and not visitedNodes[i + 1][j]:
        unvisitedNeighbours.append([i + 1, j])
    # Left neighbour coordinates.
    if j > 0 and not visitedNodes[i][j - 1]:
        unvisitedNeighbours.append([i, j - 1])
    # Right neighbour coordinates.
    if j < len(matrix[i]) - 1 and not visitedNodes[i][j + 1]:
        unvisitedNeighbours.append([i, j + 1])
    
    return unvisitedNeighbours
