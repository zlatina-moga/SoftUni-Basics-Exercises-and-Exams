volume = int(input())
debit1 = int(input())
debit2 = int(input())
hours = float(input())

pipe_1 = debit1 * hours
pipe_2 = debit2 * hours
total_pipes = pipe_1 + pipe_2

if total_pipes <= volume:
    percent = (total_pipes / volume) * 100
    pipe1 = (pipe_1 / total_pipes) * 100
    pipe2 = (pipe_2 / total_pipes) * 100
    print(f"The pool is {percent:.2f}% full. Pipe 1: {pipe1:.2f}%. Pipe 2: {pipe2:.2f}%.")
else:
    difference = abs(volume - total_pipes)
    print(f"For {hours} hours the pool overflows with {difference:.2f} liters.")