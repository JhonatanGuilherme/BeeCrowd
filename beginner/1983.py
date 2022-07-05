N = int(input())

student_notes = dict()
for _ in range(N):
  registration_number, note = map(float, input().split())
  student_notes[int(registration_number)] = note
best_student = [(k, v) for k, v in student_notes.items() if v == max(student_notes.values())][0]
print(best_student[0] if best_student[1] >= 8 else "Minimum note not reached")