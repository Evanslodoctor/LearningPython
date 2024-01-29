import turtle

TeamApic = ["Evans Chaun", "John Wambua", "Ashley Apondi", "Simon Ngaruiya", "Dina Anyango"]

for names in TeamApic:
    print(names)

for steps in range(4):
    turtle.forward(100)
    turtle.right(120)
    for steps in range(4):
        turtle.forward(100)
        turtle.right(360/3)


turtle.done()
