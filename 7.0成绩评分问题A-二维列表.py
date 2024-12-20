def computerGrades(answers,keys,n):
    grades = []
    questionCount = [0]*len(keys)
    for i in range(len(answers)):
        correctCount = 0
        for j in range(len(answers[i])):#第i个学生
            if answers[i][j] == keys[j]:
                correctCount += n
                questionCount[j] += 1
        grades.append(correctCount)
    return grades,questionCount

def main():
    keys = input().split()
    n = int(input())
    records = [
        ['E', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
        ['E', 'A', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'C'],
        ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
        ['E', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
        ['D', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'D', 'A']]
    stuGrades,questionCount = computerGrades(records, keys, n)
    for i in range(len(stuGrades)):
        print(f'Student {i+1}\'s grade is {stuGrades[i]}')
    maxCount = max(questionCount)
    for i in range(len(questionCount)):
        if questionCount[i] == maxCount:
            print(f'The question {i+1}\'s has the highest scoring rate, with {maxCount} people.')

if __name__ == "__main__":
    main()
