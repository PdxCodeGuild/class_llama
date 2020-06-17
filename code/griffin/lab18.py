def peaks(data):
    for i, num in enumerate(data):
        if i > 0 and i < len(data) -1:
            if num > data[i-1] and num > data[i+1]:
                print(f"peak at index {i}")
        

def valleys():
    pass


def peaks_and_valleys():
    pass


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    
    peaks(data)


if __name__ == "__main__":
    main()