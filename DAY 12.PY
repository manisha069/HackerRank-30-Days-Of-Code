

class Student(Person):
    def __init__(self, firstName, lastName, idn, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idn
        self.scores=scores
    
    def calculate(self):
        avg=sum(scores)//len(scores)
        if avg >=90 and avg <= 100:
            return "O"
        elif avg >=80 and avg < 90:
            return "E"
        elif avg >=70 and avg < 90:
            return "A"
        elif avg >=55 and avg < 70:
            return "P"
        elif avg >=40 and avg < 55:
            return "D"
        elif avg < 40:
            return "T"


