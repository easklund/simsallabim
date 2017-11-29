#A (k,n)theashold scheme, master secret for the scheme
#create a master secret using Lagrange
#f(z) = x + α1z + α2z^2 +. . . + αt−1z^t−1


def ceratePrivatePoly():
    pass

def revealMasterSecret(listOfKPoly):
    #interpolate
    #secret = sumOF(f(i)) * multiplicationssummaOF(j(j-i))
    sumOf = 0
    mulOf = 0
    for i in range(len(listOfKPoly)):
        #sumOf = sumOf + listOfKPoly[i]
        for j in range(len(listOfKPoly)):
            if j != i :
                j/(i-j)
