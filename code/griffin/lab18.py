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
    for i in range(9):
        for num in data:
            if num >= counter:
                print("X  ", end = "")
            else:
                print("   ", end = "")
        print("\n")
        counter -= 1

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    draw_xs(data)
    print(data)
    peaks_and_valleys(data)
    


if __name__ == "__main__":
    main()