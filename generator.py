from openpyxl import load_workbook

wb = load_workbook('in.xlsx')
wb.active = 1
sheet = wb.active


# namelist: n18-48
# primalnumbers: o18-48
# secondnumbers: p18-48

# codes: c5-32
# primary: d, e, f, g
# secondary: h, i, j

startnumber = 18
endnumber = 48

print(sheet['a1'].value)

primarylist= []
for i in range(18,49):
    name = sheet['n'+str(i)].value
    primaries = []
    primarystudents = 0

    for j in ['d', 'e', 'f', 'g']:
        for k in range(5,33):
            if(sheet[j+str(k)].value == name):
                primaries.append(sheet['b'+str(k)].value)
                primarystudents = primarystudents + sheet['k'+str(k)].value

    print(name)
    print(primaries)

    tpl = (name, primaries, primarystudents)

    primarylist.append(tpl)

secondarylist= []
for i in range(18,49):
    name = sheet['n'+str(i)].value
    secondaries = []
    secondarystudents = 0

    for j in ['h', 'i', 'j']:
        for k in range(5,33):
            if(sheet[j+str(k)].value == name):
                secondaries.append(sheet['b'+str(k)].value)
                secondarystudents = secondarystudents + sheet['k'+str(k)].value

    print(name)
    print(secondaries)

    tpl = (name, secondaries, secondarystudents)

    secondarylist.append(tpl)


wb.active = 0
sheet = wb.active

print("---------------------")

i=3
for tpl in primarylist:
    print(tpl[0])
    print(tpl[1])

    sheet['a' + str(i)] = tpl[0]

    j = 0
    letters = ['d', 'e', 'f', 'g']
    for code in tpl[1]:
        curcell = letters[j] + str(i)
        print("to " + curcell + ": " + code)

        sheet[curcell] = code
        j = j + 1
    sheet['k' + str(i)] = tpl[2]
    i = i + 1



i=3
for tpl in secondarylist:   
    j = 0
    letters = ['h', 'i', 'j']
    for code in tpl[1]:
        curcell = letters[j] + str(i)
        print("to " + curcell + ": " + code)

        sheet[curcell] = code
        j = j + 1

    sheet['l' + str(i)] = tpl[2]
    sheet['m' + str(i)] = tpl[2] + sheet['k' + str(i)].value
    i = i + 1


wb.active = 2
sheet = wb.active

wb.save('in2.xlsx')