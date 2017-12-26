def multiply(self, num1, num2):
    str_lookup = {"0": 0, "1": 1, "2": 2, "3": 3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9}
    num_lookup = {0:"0", 1:"1", 2:"2", 3:"3", 4:"4", 5:"5", 6:"6", 7:"7", 8:"8", 9:"9"}
    int1, int2 = 0, 0
    num1, num2 = num1[::-1], num2[::-1]

    for i in range(len(num1)):
        int1 += str_lookup[num1[i]] * 10 ** i
    
    for j in range(len(num2)):
        int2 += str_lookup[num2[j]] * 10 ** j
    
    result, result_str = int1 * int2, ""
    print(result, int1, int2)
    while result >= 0:
        digit = result % 10
        result_str += num_lookup[digit]
        result = result // 10
        
    return result_str[::-1]
