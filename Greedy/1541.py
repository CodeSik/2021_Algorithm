def main():
    input_arr = list(input().split("-"))
    result = 0

    if "+" in input_arr[0]:
        sub_arr = input_arr[0].split("+")
        sub_result = 0
        for sub_num in sub_arr:
            sub_result += int(sub_num)
        result += sub_result
    elif "+" not in input_arr[0]:
        result += int(input_arr[0])
    elif len(input_arr) == 1:
        print(int(input_arr[0]))
        return
    input_arr.pop(0)

    for num in input_arr:
        if "+" in num:
            sub_arr = num.split("+")
            sub_result = 0
            for sub_num in sub_arr:
                sub_result+=int(sub_num)
            result -= sub_result
        else:
            result -= int(num)

    print(result)

if __name__ == "__main__":
    main()
    while not None:
        print(1)