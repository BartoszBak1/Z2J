def bobble_sort(numbers:list):

    if numbers:
        flag = 1
        for i in range(len(numbers)):
            flag = 0
            for j in range(len(numbers)-i-1):

                if numbers[j] > numbers[j+1]:
                    number = numbers.pop(j)
                    numbers.insert(j+1, number)
                    flag = 1
            if flag == 0:
                return numbers
    else:
        return numbers
        
examples = [
        [],
        [1,2,5,3,1,7,9,1,12,83,1,5,3,2],
        [1,1,1,1,1,1,1,2,1,1,1],
        [2,2,2,2],
        [1,2],
        [2,1]
]

for example in examples:
    print(f"{bobble_sort(example)}")