#A (k,n)theashold scheme, master secret for the scheme
#create a master secret using Lagrange
#f(z) = x + α1z + α2z^2 +. . . + αt−1z^t−1

#f(0)= -26210

def ceratePrivatePoly():
    pass

# f1(x) = 13 + 8x + 11x^2 + 1x^3 + 5x^4
def countF1of1(poly):
    size = len(poly)
    summa = 0
    for j in range(size):
        summa += poly[j]*(1**j)

    return summa

def Fof1(poly, f1):
    size = len(poly)
    F1 = f1
    for j in range(size):
        F1 += poly[j]
    return F1

def revealMasterSecret(listOfKPoly):
    #interpolate
    #secret = sumOF(f(i)) * multiplicationssummaOF(j(j-i))
    #sumOf = 0
    secret = 0
    size = len(listOfKPoly)
    for i in range(size):
        mulOf = 1
        f =  listOfKPoly[i]
        for j in range(size):
            if j != i and listOfKPoly[j] != 0 :
                mulOf = mulOf * (j+1)/((j+1)-(i+1))
        secret += (f * mulOf)
    return round(secret)

def addF1InPoly(f1, poly):
    p = []
    p.append(f1)
    for i in range(len(poly)):
        p.append(poly[i])
    return p

# privatepoly = [ 13, 8, 11, 1, 5]
# fOf1 =  [ 75, 75, 54, 52, 77, 54, 43]
# collaberationPoly = [2782, 0, 30822, 70960, 0, 256422]

# privatepoly = [ 20, 20, 11, 6]
# fOf1 =  [ 63, 49, 49, 54, 43]
# collaberationPoly = [0,2199, 4389,0, 12585]

# privatepoly = [ 20 ,18, 13, 19, 15]
# fOf1 =  [ 34,  48,  45, 39, 24]
# collaberationPoly = [1908,  7677,0 , 50751,101700]

# privatepoly = [ 9, 19, 5]
# fOf1 =  [ 37,18,  40,  44,  28]
# collaberationPoly = [0, 0, 1385, 2028]

privatepoly = [ 4,4,7,9]
fOf1 =  [34,  52,  36, 34, 35, 39]
collaberationPoly = [0, 2080,0,0, 12469, 19052]




f1Of1 = countF1of1(privatepoly)
fOf1 = Fof1(fOf1, f1Of1)
p = addF1InPoly(fOf1, collaberationPoly)
secret = revealMasterSecret(p)


print(f1Of1)
print(fOf1)
print(p)
print(secret)
