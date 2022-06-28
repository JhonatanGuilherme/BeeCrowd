S = sorted(list(map(int, input().split())))
print("S" if S[0] + S[1] > S[2] or S[1] + S[2] > S[3] else "N")