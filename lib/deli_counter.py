def line(que):
    if not que:
        message = "The line is currently empty."
    else:
        message = "The line is currently: " + " ".join([f"{i+1}. {customer}" for i, customer in enumerate(que)])

    print(message)


def take_a_number():
  pass

def now_serving():
  pass