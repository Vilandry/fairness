#from _typeshed import Self
import openpyxl
import matplotlib


class interpolate:

    xk = []
    yk = []
    M = 1


    # x is an array, which is literally an n dimension point
    def calculateSlackVariable(self, x):
        summa = sum(x)
        slackvariable = 1 - summa
        return slackvariable


    # simplical distance, where every vi is treated as 1
    def distance(self, x, y):
        maxx = abs( self.calculateSlackVariable(x) - self.calculateSlackVariable(y) )
        for elem in range(len(x)):
            maxx = max(maxx, abs(x[elem] - y[elem]))
        return maxx


    def UpperH(self, x):
        minn = 9999999
        for point in range(len(self.xk)):
            minn = min(minn,  ( self.yk[point] + self.M*self.distance(self.xk[point], x) ) )
            #print("distance: " + str(self.distance(self.xk[point], x)))
        #print("upper: "+ str(minn))
        return minn

    def LowerH(self, x):
        maxx = -9999999
        for point in range(len(self.xk)):
            maxx = max(maxx,  ( self.yk[point] - self.M*self.distance(self.xk[point], x) ) )
            #print("templower: " + str( self.yk[point] - self.M*self.distance(self.xk[point], x) ))
        #print("lower: " + str(maxx))
        return maxx

    def interpolate(self, x):
        return 0.5 * (self.LowerH(x) + self.UpperH(x) )

    def setXK(self, xk):
        self.xk = xk
    
    def setYK(self, yk):
        self.yk = yk

    def setM(self, M):
        self.M = M



#interpolater = interpolate()


#xk = [ [1, 1.5], [0, 0.6], [2, 2.2] ]
#yk = [1, 1, 2]

#interpolater.setM(1)
#interpolater.setXK(xk)
#interpolater.setYK(yk)

#x = [1.5,2]

#y = interpolater.interpolate(x)

#print(y)

