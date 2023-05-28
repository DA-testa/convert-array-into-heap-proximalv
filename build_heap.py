# python3


def build_heap(data):
    swaps = []
    
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    for i in range(n // 2, -1 , -1):
        while True:
            labais = i * 2 + 2
            kreisais = i * 2 + 1
            min = i
            if kreisais < n and data[kreisais] < data[min]:
                min = kreisais
            if labais < n and data[labais] < data [min]:  
                min = labais

            if min != i:
                swaps.append((i, min))
                data[i], data[min] = data[min], data[i]
            else:
                break

    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file
    rezims = input()
    if "I" in rezims:
        n = int(input())     
        data = list (map(int, input().split()))
    elif "F" in rezims:
        fails = input()
        cels = "./tests/" + fails
        if 'a' in fails:
            return
        with open(cels) as f:
            n= int(f.readline())
            data = list(map(int, f.readline().split()))


    # input from keyboard
    # n = int(input())
    # data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n
    
    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))
    assert len(swaps) <= n*4

    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
