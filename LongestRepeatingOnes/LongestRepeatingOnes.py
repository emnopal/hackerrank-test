def LongestRepeatingOnesFirstWay(string: str) -> int:
    num_final: int = 0
    num_final_temp: int = 0

    for char in string:
        num: int = int(char)
        if num == 1:
            num_final_temp += 1
            if num_final_temp > num_final:
                num_final = num_final_temp
        else:
            num_final_temp = 0

    return num_final

def LongestRepeatingOnesSecondWay(string: str) -> int:
    return max(map(int, map(len, [x for x in string.split("0") if x])))

if __name__ == '__main__':
    result: int = LongestRepeatingOnesFirstWay("11100101010000001111111010101010")
    print(result) # 7

    result: int = LongestRepeatingOnesSecondWay("11100101010000001111111010101010")
    print(result) # 7
