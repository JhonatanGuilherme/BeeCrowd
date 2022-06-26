T = int(input())

for i in range(T):
  S = input().split()
  if S[0] == S[1]:
    R = "De novo!"
  elif ((S[0] == "tesoura" and S[1] in ["papel", "lagarto"]) or (S[0] == "papel" and S[1] in ["pedra", "Spock"])
    or (S[0] == "pedra" and S[1] in ["lagarto", "tesoura"]) or (S[0] == "lagarto" and S[1] in ["Spock", "papel"])
    or (S[0] == "Spock" and S[1] in ["tesoura", "pedra"])):
    R = "Bazinga!"
  else:
    R = "Raj trapaceou!"
  print(f"Caso #{i + 1}: {R}")