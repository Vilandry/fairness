from numpy import floor, sqrt, vectorize
from teacher import teacher
from interpolate import interpolate
import math
class TINterpolate:
    teacherList = []
    M = 1

    furthest = []

    def vectorise(self, t:teacher):
        return [t.subjectcnt, t.students]


    # x is a vectorised teacher, which is literally an n dimension point
    def calculateSlackVariable(self, x):
        summa = sum(x)
        slackvariable = 1 - summa
        return slackvariable

    # simplical distance, where every vi is treated as 1
    # both x and y are vectorised teachers
    def distance(self, x, y):
        maxx = abs( self.calculateSlackVariable(  x  ) - self.calculateSlackVariable(y) )
        for elem in range(len(x)):
            maxx = max(maxx, abs(x[elem] - y[elem]))
        return maxx

    def distance2(self, x, y):
        dist = 0
        for elem in range(len(x)):
            dist = dist + x[elem] + y[elem]

        dist = floor(sqrt(dist))
        return dist
    
    def vUpperH(self, x, teacherList):
        minn = 9999999
        name = ""
        xvector = self.vectorise(x)
        for point in range(len(teacherList)):
            vpoint = self.vectorise(teacherList[point])
            curval = ( teacherList[point].workload + self.M*self.distance( vpoint, xvector) )

            if ( minn > curval):
                minn = curval
                name = teacherList[point].name

            #print("distance: " + str(self.distance(self.xk[point], x)))
        #print("upper: "+ str(minn))
        return (name, minn)

    def vLowerH(self, x, teacherlist):
        maxx = -9999999
        name = ""
        xvector = self.vectorise(x)
        for point in range(len(teacherlist)):
            vpoint = self.vectorise(teacherlist[point])
            wl = teacherlist[point].workload
            dist = self.distance(  vpoint, xvector)
            curval = ( wl - self.M * dist )
            if ( maxx < curval ):
                maxx = curval
                name = teacherlist[point].name

            #print("templower: " + str( self.yk[point] - self.M*self.distance(self.xk[point], x) ))
        #print("lower: " + str(maxx))
        return (name, maxx)


    def interpolate(self, x):
        return 0.5 * (self.vLowerH(x)[1] + self.vUpperH(x)[1] )


    def findOuterElements(self):
        self.furthest = []

        dimensions = len(self.vectorise(self.teacherList[0]))

        
        for i in range(dimensions):
            curmax = -10000000
            curmin = 9999999999
            curminName = ""
            curmaxName = ""

            for teacher in self.teacherList:
                vec_teacher = self.vectorise(teacher)
                if(vec_teacher[i] > curmax):
                    curmax = vec_teacher[i]
                    curmaxName = teacher.name
                
                if(vec_teacher[i] < curmin):
                    curmin = vec_teacher[i]
                    curmaxName = teacher.name

            self.furthest.append(curminName)
            self.furthest.append(curmaxName)

    def FindHits(self, upperMargin, lowerMargin):
        self.findOuterElements()

        hits = []
        for teacher in self.teacherList:
            xs = []
            if(teacher.name in self.furthest):  # we cant do anything with the outer-rim elements
                continue
                pass

            for ot in self.teacherList:
                if(ot.name == teacher.name):
                    continue

                xs.append(ot)

            nameL = self.vLowerH(teacher, xs)
            nameU = self.vUpperH(teacher, xs)
            expectedWork = (nameL[1] + nameU[1])* 0.5

            #if(teacher.name == "Emese"): print(teacher.name + ", expected work: " + str(expectedWork))

            if( ( floor(expectedWork) - lowerMargin > teacher.workload) or
                ( math.ceil(expectedWork) + upperMargin < teacher.workload)  ):
                    hit = (teacher.name, nameU[0], nameL[0])
                    hits.append(hit)

        return hits

    def __init__(self) -> None:
        pass