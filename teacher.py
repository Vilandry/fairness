from typing import Dict


class teacher:
    name = ""
    subjects = []
    subjectcnt = 0
    students = 0
    relative_students = 0

    workload = 0

    def calculateRelativeStudents(self, aut_subjects:Dict):
        self.relative_students = 0
        for key in aut_subjects.keys():
            if key in self.subjects:
                subject = aut_subjects[key]
                self.relative_students = self.relative_students + (aut_subjects[key].students / aut_subjects[key].teachers)

    def WorkHourWorkLoad(self, worksheets, consultantrow, examineerrow, presidentrow, memberrows, secretairerow):
        
        self.workload = 0

        for worksheet in worksheets:

            rownum = 2
            consultantrownum = "2"
            examineerrownum = "2"
            presidentrownum = "2"
            secretairerownum = "2"
            member1rownum = "2"
            member2rownum = "2"

            while not worksheet['f' + str(rownum)].value == None:
                rowstr = str(rownum)

                if(not worksheet[consultantrow + rowstr].value == None ):
                    consultantrownum = rowstr

                if(not worksheet[examineerrow + rowstr].value == None ):
                    examineerrownum = rowstr

                if(not worksheet[presidentrow + rowstr].value == None ):
                    presidentrownum = rowstr

                if(not worksheet[secretairerow + rowstr].value == None ):
                    secretairerownum = rowstr


                if(not worksheet[memberrows[0] + rowstr].value == None ):
                    member1rownum = rowstr

                if(not worksheet[memberrows[0] + rowstr].value == None ):
                    member2rownum = rowstr



                member1 = worksheet[memberrows[0] + member1rownum ].value
                member2 = worksheet[memberrows[1] + member2rownum ].value
                if(member1 == None): member1 = ""
                if(member2 == None): member2 = ""



                if( worksheet[consultantrow + consultantrownum ].value == self.name or
                    worksheet[presidentrow  + presidentrownum ].value == self.name  or
                    worksheet[secretairerow + secretairerownum ].value == self.name or
                    self.name in worksheet[examineerrow  + examineerrownum ].value  or
                    self.name in member1                                            or
                    self.name in member2 ): # if the current teacher is present during the exam

                    self.workload = self.workload + 1
                    # print(str(consultantrownum) + " | " + str(examineerrownum) + " | " + str(presidentrownum) + " | " + str(secretairerownum))               

                rownum = rownum + 1

        

    def SummaWorkLoad(self, worksheets, consultantrow, examineerrow, presidentrow, memberrows, secretairerow, workloadweights = {}):

        # region

        if(not "consultant" in workloadweights.keys() ):
            workloadweights["consultant"] = 0
        
        if(not "examineer" in workloadweights.keys() ):
            workloadweights["examineer"] = 1

        if(not "president" in workloadweights.keys() ):
            workloadweights["president"] = 0

        if(not "member" in workloadweights.keys() ):
            workloadweights["member"] = 0

        if(not "secretaire" in workloadweights.keys() ):
            workloadweights["secretaire"] = 0

        # endregion

        self.workload = 0

        for worksheet in worksheets:

            rownum = 2
            consultantrownum = "2"
            examineerrownum = "2"
            presidentrownum = "2"
            secretairerownum = "2"
            member1rownum = "2"
            member2rownum = "2"

            while not worksheet['f' + str(rownum)].value == None:
                rowstr = str(rownum)

                if(not worksheet[consultantrow + rowstr].value == None ):
                    consultantrownum = rowstr

                if(not worksheet[examineerrow + rowstr].value == None ):
                    examineerrownum = rowstr

                if(not worksheet[presidentrow + rowstr].value == None ):
                    presidentrownum = rowstr

                if(not worksheet[secretairerow + rowstr].value == None ):
                    secretairerownum = rowstr

                
                if(not worksheet[memberrows[0] + rowstr].value == None ):
                    member1rownum = rowstr
                    #print("Member1row: " + rowstr)
                    #print("value: " + worksheet[memberrows[0] + rowstr].value)

                if(not worksheet[memberrows[1] + rowstr].value == None ):
                    member2rownum = rowstr
                    #print("Member2row: " + rowstr)

                member1 = worksheet[memberrows[0] + member1rownum ].value
                member2 = worksheet[memberrows[1] + member2rownum ].value
                if(member1 == None): member1 = ""
                if(member2 == None): member2 = ""



                if( worksheet[consultantrow + consultantrownum ].value == self.name):
                    self.workload = self.workload + workloadweights["consultant"]
                    pass

                if( self.name in worksheet[examineerrow  + examineerrownum ].value):
                    self.workload = self.workload + workloadweights["examineer"]
                    pass

                if( worksheet[presidentrow  + presidentrownum ].value == self.name):
                    self.workload = self.workload + workloadweights["president"]
                    pass

                if (worksheet[secretairerow + secretairerownum ].value == self.name):
                    self.workload = self.workload +  workloadweights["secretaire"]
                    pass


                if( self.name in member1 or self.name in member2 ): # if the current teacher is present during the exam
                    self.workload = self.workload + workloadweights["member"]
                    pass 

                rownum = rownum + 1



    def ProductWorkLoad(self, worksheets, consultantrow, examineerrow, presidentrow, memberrows, secretairerow, workloadweights = {}):
        if(not "consultant" in workloadweights.keys() ):
            workloadweights["consultant"] = 1
        
        if(not "examineer" in workloadweights.keys() ):
            workloadweights["examineer"] = 1

        if(not "president" in workloadweights.keys() ):
            workloadweights["president"] = 1

        if(not "member" in workloadweights.keys() ):
            workloadweights["member"] = 1

        if(not "secretaire" in workloadweights.keys() ):
            workloadweights["secretaire"] = 1

        self.workload = 0

        for worksheet in worksheets:

            rownum = 2
            while not worksheet['f' + str(rownum)].value == None:
                
                member1 = worksheet[memberrows[0] + str(rownum) ].value
                member2 = worksheet[memberrows[1] + str(rownum) ].value
                if(member1 == None): member1 = ""
                if(member2 == None): member2 = ""

                if( worksheet[consultantrow + str(rownum) ].value == self.name):
                    self.summaworkload = self.summaworkload + workloadweights["consultant"]
                    pass

                if( worksheet[examineerrow  + str(rownum) ].value == self.name):
                    self.summaworkload = self.summaworkload + workloadweights["examineer"]
                    pass

                if( worksheet[presidentrow  + str(rownum) ].value == self.name):
                    self.summaworkload = self.summaworkload + workloadweights["president"]
                    pass

                if (worksheet[secretairerow + str(rownum) ].value == self.name):
                    self.summaworkload = self.summaworkload +  workloadweights["secretaire"]
                    pass


                if( self.name in member1 or self.name in member2 ): # if the current teacher is present during the exam
                    self.summaworkload = self.summaworkload + workloadweights["member"]
                    pass 

                rownum = rownum + 1


    def __init__(self, _name = "", _students = 0, _subjectcnt = 0, _workload = 0, _subjects = [], _rel_stud = 0) -> None:
        self.name = _name
        self.students = _students
        self.subjectcnt = _subjectcnt
        self.workload = _workload
        self.subjects = _subjects

        self.relative_students = _rel_stud