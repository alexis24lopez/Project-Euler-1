######################################################################################################################
# Project Euler
# Problem 15
# File name: PE_P15.py
# Compile: python PE_P15.py
# Programer: Alexis Lopez
# Description: Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
# there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?
# NOTE: This works for any size grid!
######################################################################################################################

print(r"Welcome to 'Project Euler' This is problem #15")

# Computing square of the sum of natural numbers
def grid(size):
    
    # Defining grid 1 x 1 to have only 2 routes
    if (size == 1):
        return 2
    
    # Storing all information about all possible routes
    matrix = []
    
    # initializing the grid with ones, as many as the size of the grid
    for a in range(0, size):
        matrix.append(1)
    
    # Defining and initializing variables
    index = 0
    sum = 0
    innerSize = size
    result = 0
    
    # Firts we set the size of the matrix to be (n - 2)* n. This is due because
    # I'm treating the 1-D matrix as a multidimentional matrix where certain
    # number of rows it is a column which depends on the size. i.e. if the grid 
    # is a 3 x 3 then every 3 indexes it is a new column. So the end product
    # is not an square matrix is an 3 x 2 matrix.
    for a in range(0, (size - 2) * size):
    
        # We are adding the previous column to get the next column. For the example above
        # if the first column is [1, 1, 1] to get the next index of the next column we add
        # 1 + 1 + 1 = 3, the next row of the same column is 1 + 1 = 2, and the last one is
        # 1 = 1 so we end up with the next column being [3, 2, 1]. We have a matrix 
        # [[3, 1], [2, 1], [1, 1]] by traditonal matrix which is a 3 x 2 matrix. 
        for i in range(index, innerSize):
            #print("this is index: ", i)
            sum += matrix[i]
        matrix.append(sum)
        sum = 0
        index += 1
        
        # The index catches the size of the matrix everytime we add a new column so we need to
        # set it back to the previous column so we can perform the same operation on the loop
        # again so we set it back one column. Remember the column size is the size of the grid
        # in this case is 3.
        if (index == innerSize):
            innerSize += size
        #print ("index", index)
        #print ("size", len(matrix))
    
    # To print the elements of the matrix
    # for b in range(0, len(matrix)):
        # print(matrix[b])
    
    # Now we need to add all the values of our matrix which represents all possible combinations
    # That we could take by passing tru the nodes of the matrix.
    for j in range(0, len(matrix)):
        result += matrix[j]
    
    # Since the matrix is symmetrical we double the count and take the scenario were we go
    # by the outside. Going by the upper counter of the grid and the bottom countor of the 
    # grid so we consider all possible paths it could take.
    result = 2 * result + 2
    
    return result


if __name__ == "__main__":

    size = int(input("\nPlease enter how big is the grid you want to check: "))
    routes = grid(size)

    print("\nThe {} X {} grid has {} routes!".format(size, size, routes))
    