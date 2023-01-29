
lines_to_write = [
    'line1',
    'line2',
    'line3'
]

with open("my_test.txt", mode="a") as f:
    # f.write("It is raining")
    # f.write("bye-bye"
    f.writelines(lines_to_write)