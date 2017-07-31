class Rotate_Matrix:

    def __init__(self,M):
        self.M=M

    def setmatrix(self,M):
        self.M=M

    def __Repostion_values_all_directions_clockwise(self,i,j):

        #size of matrix (rows or cols)
        n=len(self.M)-1

        temp=self.M[i][j]

        #replace up by left:
        self.M[i][j]=self.M[n-j][i]

        #replace left by bottom:
        self.M[n-j][i]=self.M[n-i][n-j]

        #replace bottom by right:
        self.M[n-i][n-j]=self.M[j][n-i]

        #replace right by up:
        self.M[j][n-i]=temp

    def __Repostion_values_all_directions_Anitclockwise(self,i,j):

        #size of matrix (rows or cols)
        n=len(self.M)-1

        temp=self.M[i][j]

        # replace up by right:
        self.M[i][j]=self.M[j][n-i]

        # replace right by bottom:
        self.M[j][n-i]=self.M[n-i][n-j]

        # replace bottom by left:
        self.M[n-i][n-j]=self.M[n-j][i]


        # replace left by up:
        self.M[n-j][i]=temp


    def rotate_sqr_matrix_clockwise_inplace(self):
        n=len(self.M)
        for row in range(int(n/2)):
            for col in range(row,n-row-1):
                self.__Repostion_values_all_directions_clockwise(row,col)
        return self.M


    def rotate_sqr_matrix_Anticlockwise_inplace(self):
        n=len(self.M)
        for row in range(int(n/2)):
            for col in range(row,n-row-1):
                self.__Repostion_values_all_directions_Anitclockwise(row,col)
        return self.M

    def __make_new_matrix(self):
        rows=len(self.M)
        cols=len(self.M[0])
        return [[None]*rows for i in range(cols)]


    # column number of input matrix will be row number of output matrix
    # IM[i][j] => OM[j][lets compute]
    def rotate_arbitrary_matrix_clockwise(self):
        NewMatrix=self.__make_new_matrix()
        rows=len(self.M)
        cols=len(self.M[0])
        for row in range(rows):
            for col in range(cols):
                NewMatrix[col][rows-row-1]=self.M[row][col]
        return NewMatrix

    # row number of input matrix will be column number of output matrix
    # IM[i][j] => OM[lets compute][i]
    def rotate_arbitrary_matrix_Anticlockwise(self):
        NewMatrix=self.__make_new_matrix()
        rows=len(self.M)
        cols=len(self.M[0])
        for row in range(rows):
            for col in range(cols):
                NewMatrix[cols-col-1][row]=self.M[row][col]
        return NewMatrix


    def print_matrix(self,Matrix):
        if Matrix:
            print('-'*40)
            for row in Matrix:
                print(row)
            print('-'*40)



