from lesson7.utils.utils import get_msd

# print("insde my_app", __name__)

if __name__ == '__main__':
    num = int(input("insert num: "))
    result = get_msd(num)
    print(result)


class Solution:
    def romanToInt(self, s: str) -> int:
        ret_num = 0
        count_letters = []
        count_letters.append(s.count("I")) # 0
        count_letters.append(s.count("V")) # 1
        count_letters.append(s.count("X")) # 2
        count_letters.append(s.count("L")) # 3
        count_letters.append(s.count("C")) # 4
        count_letters.append(s.count("D")) # 5
        count_letters.append(s.count("M")) # 6

        roman_chars = ("I", "V", "X", "L", "C", "D", "M")
        for c in roman_chars:
            count_letters.append(s.count(c))


        count_iv = s.count("IV")
        count_ix = s.count("IX")
        count_xl = s.count("XL")
        count_xc = s.count("XC")
        count_cd = s.count("CD")
        count_cm = s.count("CM")

        count_letters[0] -= count_iv + count_ix
        count_letters[1] -= count_iv
        count_letters[2] -= count_ix + count_xl + count_xc
        count_letters[3] -= count_xl
        count_letters[4] -= count_xc + count_cd + count_cm
        count_letters[5] -= count_cd
        count_letters[6] -= count_cm

        ret_num += count_letters[0]*1 + count_letters[1]*5 + count_letters[2]*10 + count_letters[3]*50 + count_letters[4]*100 + count_letters[5]*500 + count_letters[6]*1000 + count_iv*4 + count_ix*9 + count_xl*40 + count_xc*90 + count_cd*400 + count_cm*900

        return ret_num

