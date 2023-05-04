f = open("high.score", "a+")
i = 0
while True:
  i += 1
  initial = input("INITIALS > ")
  f.write(f"{initial}\n")
  score = input("SCORE > ")
  f.write(f"{score}\n")
  if i >= 3:
    proceed = input("Have you finished entering the data?\n>").lower()
    if proceed[0] == "n":
      continue
    elif proceed [0] == "y":
      break
f.close()