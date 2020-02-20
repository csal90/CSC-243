def computeFinalGrade(homeworkGrade, midtermGrade, finaltermGrade):
    return homeworkGrade*0.3+midtermGrade*0.35+finaltermGrade*0.35

def getCharFromStr(s):
    i=int(input('Enter an index: '))
    return s[i]


def midOfList(l):
    return l[len(l)//2]

def tripleItems(l):
    for n in l:
        print(3*n)

def printTriangle(n):
    for k in range(n,0,-1):
        print(k*'*')
        
