def line(que):
    if not que:
        message = "The line is currently empty."
    else:
        message = "The line is currently: " + " ".join([f"{i+1}. {customer}" for i, customer in enumerate(que)])

    print(message)


def take_a_number(que, name):
  position = len(que) + 1
  que.append(name)
  print(f"Welcome, {name}. You are number {position} in line.")


def now_serving(que):
  if(len(que) == 0) :
    print("There is nobody waiting to be served!")
  else:
   name = que.pop(0)
   print(f"Currently serving {name}.")
