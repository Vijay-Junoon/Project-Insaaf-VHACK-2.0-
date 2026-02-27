import pandas as pd
def calculateScore(offense,vul,age,BailMatter,UnderTrial):
    w_offense = 25
    w_vul = 20
    w_age = 15
    w_bail = 20
    w_trial = 20

    if offense == "Heinous":
        caseVal = 1
    elif offense == "Serious":
        caseVal = 0.8
    else:
        caseVal = 0.4

    vulVal = 1 if vul else 0

    ageVal = min(age,20,1)

    if BailMatter:
        bailValue = 1
    else:
        bailValue = 0


    if UnderTrial:
        trialVal = 1
    else:
        trialVal = 0

    score = (caseVal * w_offense + vulVal * w_vul + ageVal * w_age + bailValue * w_bail + trialVal * w_trial)

    return round(score,2)

dataset = pd.read_csv("insaafdataset.csv")
for i in dataset:
    print(i)
# print(dataset)

