'''
N length : elements should be (0 to n-1)
Find duplicate elements in array
Input= N=7  Array=[5 0 1 5 0 4]
Output=  0,5

time=> O(N) space=>O(1)

Approach: As we know that elements and index both are between 0 to n-1 only:
x=element on (element on index)
At any index, if  x is flagged, that means index of x (i.e. your current index) is founded before.


Algorithm:
for i=0 to n-1
    if Array[absoulte(Array[i])] >= 0:
            make  Array[absoulte(Array[i])] negative
    if Array[absoulte(Array[i])] <= 0:
            Array[i] is duplicate


'''
