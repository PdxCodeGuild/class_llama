def peaks(data):
    for i, num in enumerate(data):
        if i > 0 and i < len(data) -1:
            if num > data[i-1] and num > data[i+1]:
                print(f"peak at index {i}")
        

def valleys(data):
    for i, num in enumerate(data):
        if i > 0 and i < len(data) -1:
            if num < data[i-1] and num < data[i+1]:
                print(f"valley at index {i}")


def peaks_and_valleys(data):
    peaks(data)
    valleys(data)



def draw_xs(data):
    counter = 9
    water_counter = 0
    for i in range(9):
        valley_toggle = False
        print(" ", end = "")
        for num in data:
            if num >= counter:
                print("X  ", end = "")
                valley_toggle = True
            #this method of adding Os and counting water works for this data set... but I think there would be problems with more complex
            #data sets, and I'm not sure how to do a better method
            elif valley_toggle == True:
                print("O  ", end = "")
                water_counter += 1
            else:
                print("   ", end = "")
        print("\n")
        counter -= 1
    return water_counter

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    water_amount = draw_xs(data)
    print(data)
    print(f"there are {water_amount} units of water")
    peaks_and_valleys(data)
    


if __name__ == "__main__":
    main()