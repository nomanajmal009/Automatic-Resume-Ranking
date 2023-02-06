import csv
data = pd.read_csv("filename.csv")
UNIList = []
SkillsList = []
Bachelor = []
Master = []
PHD = []





with open(r"C:\Users\noman\projects\AutomaticResumeRanking\main\Bachelor.txt") as f:
    Bachelor = f.readlines()

with open(r"C:\Users\noman\projects\AutomaticResumeRanking\main\Ranking.csv",newline='', encoding='cp1252',errors='ignore') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            print(f'\t{row[0]}  {row[1]}')
            line_count += 1


def CalTotalTime(input):
    if input>= 0 and input<=15:
        result= (input / 15) * 30
        return result
    else:
        return 0

def CalEdu(input):
    EDUresult = 0
    flag=0
    for i in input:
        flag=0
        if flag==0:
            for x in Bachelor:
                if(input[i] == x):
                    EDUresult = EDUresult + 8
                    flag=1

        if flag==0:
            for x in Master:
                if(input[i] == x):
                    EDUresult = EDUresult + 12
                    flag=1
        if flag==0:
            for x in PHD:
                if(input[i] == x):
                    EDUresult = EDUresult + 15
                    flag=1
                
    
    return EDUresult
