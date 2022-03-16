from interpolate import interpolate
from teacher import teacher
from teacherInterpolator import TINterpolate
import matplotlib.pyplot as plt
import numpy as np

def tnamecalc(teachers):
    tname = []

    for tteacher in teachers:
        tname.append(tteacher.name)

    return tname


interpolator = TINterpolate()
interpolator.M = 1

print("Adding some casual guy")


teacher1 = teacher()
teacher1.name = "Artur"
teacher1.students = 20
teacher1.subjectcnt = 2
teacher1.workload = 21

tteacher = teacher1
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))


teacher2 = teacher()
teacher2.name = "Bela"
teacher2.students = 15
teacher2.subjectcnt = 1
teacher2.workload = 18

tteacher = teacher2
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))

teacher3 = teacher()
teacher3.name = "Cintia"
teacher3.students = 24
teacher3.subjectcnt = 2
teacher3.workload = 22

tteacher = teacher3
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))

teachers = [teacher1, teacher2, teacher3]

interpolator.teacherList = teachers
print("Teachers: ")
print(tnamecalc(teachers))
print("Hits:")
print(interpolator.FindHits(3, 3))
print("")
print("##########################")
print("")


print("Adding a dude who doesnt like to work")

teacher4 = teacher()
teacher4.name = "Naplopo"
teacher4.students = 20
teacher4.subjectcnt = 2
teacher4.workload = 1

tteacher = teacher4
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))

teachers = [teacher1, teacher2, teacher3, teacher4]

interpolator.teacherList = teachers

print("Teachers: ")
print(tnamecalc(teachers))
print("Hits:")
print(interpolator.FindHits(3, 3))
print("")
print("##########################")
print("")

print("Adding an unrealistically overwhelmed worker")

teacher5 = teacher()
teacher5.name = "Sztahanov"
teacher5.subjectcnt = 1
teacher5.students = 2
teacher5.workload = 100

tteacher = teacher5
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))

teachers = [teacher1, teacher2, teacher3, teacher5]

interpolator.teacherList = teachers
print("Teachers: ")
print(tnamecalc(teachers))
print("Hits:")
print(interpolator.FindHits(3, 3))
print("")
print("##########################")
print("")


print("Having both an overloaded and an underloaded guy: ")

teachers = [teacher1, teacher2, teacher3, teacher4, teacher5]

interpolator.teacherList = teachers
print("Teachers: ")
print(tnamecalc(teachers))
print("Hits:")
print(interpolator.FindHits(3, 3))
print("")
print("##########################")
print("")

print("Adding a big guy and a small employee")

teacher6 = teacher("Denes", 23, 3, 25)
tteacher = teacher6
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))



teacher7 = teacher("Emese", 9, 1, 8)
tteacher = teacher7
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))


teachers = [teacher1, teacher2, teacher3, teacher6, teacher7]
interpolator.teacherList = teachers
interpolator.teacherList = teachers
print("Teachers: ")
print(tnamecalc(teachers))
print("Hits:")
print(interpolator.FindHits(3, 3))
print("")
print("##########################")
print("")





print("Adding some minor employee")

teacher8 = teacher("Fulop", 12, 1, 13)
tteacher = teacher8
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))


teacher9 = teacher("Gerda", 10, 1, 10)
tteacher = teacher9
print("     Name: " + tteacher.name + "\n     Students: " + str(tteacher.students) + "     No. subjects: " + str(tteacher.subjectcnt) + "     Workload: " + str(tteacher.workload))


teachers.append(teacher8)
teachers.append(teacher9)
interpolator.teacherList = teachers
print("Teachers: ")
print(tnamecalc(teachers))
print("Hits:")
print(interpolator.FindHits(3, 3))
print("")
print("##########################")
print("")


#region plotting
xs = []
ys = []
zs = []

for cteacher in teachers:
    xs.append(cteacher.students)
    ys.append(cteacher.subjectcnt)
    zs.append(cteacher.workload)

x = np.array(xs)
y = np.array(ys)
z = np.array(zs)

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(xs,ys,zs)
ax.set_xlim(0, 30)
ax.set_xlabel("students")
ax.set_ylim(0, 5)
ax.set_ylabel("subjects")
ax.set_zlim(0, 30)
ax.set_zlabel("workload")

#plt.show()
#endregion