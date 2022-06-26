A, B, C = map(int, input().split())
print(":)" if A - B > B - C or (A - B == B - C and B - A > 0) else ":(")