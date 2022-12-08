"""Division of Nlogonia"""
alternatives = ("A", "B", "C", "D", "E")
while True:
  K = int(input())
  if K == 0: break

  for _ in range(K):
    answers = list(map(int, input().split()))
    answers_sorted = sorted(answers)
    a = answers[answers.index(answers_sorted[0])]
    print("*" if answers_sorted[0] > 127 or answers_sorted[1] <= 127 else answers[answers.index(answers_sorted[0])]) 

