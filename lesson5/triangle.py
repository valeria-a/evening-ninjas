# get input from a user
# check valid input (numeric + correct trianlge)
# calculate perimeter and area
# print the result

def is_valid_triangle(sides: list[int]) -> bool:
    return sides[0] + sides[1] > sides[2] and \
           sides[0] + sides[2] > sides[1] and \
           sides[1] + sides[2] > sides[0]

def parse_input(user_inp: str) -> list[int] | None:
    split_list = user_inp.split(",")
    if len(split_list) != 3:
        return
    sides = []
    for side in split_list:
        if not side.isdigit() or side == '0':
            return
        sides.append(int(side))
    if is_valid_triangle(sides):
        return sides


        # for side in split_list:
        #     if side.isdigit()
def calc_perimeter(sides:list[int]) -> int:
    return sum(sides)


def calc_area(sides:list[int]) -> float:
    s = calc_perimeter(sides)/2
    area = s * (s-sides[0]) * (s-sides[1]) * (s-sides[2])
    area = area ** 0.5
    return area

while True:
    user_input: str = input("Insert 3 sides of triangle separated by ,: ")
    sides: list[int] = parse_input(user_input)
    if sides:
        break
print(f"The perimeter of the triangle is: "
      f"{calc_perimeter(sides)}")
print(f"The area of the triangle is: "
      f"{calc_area(sides)}")
