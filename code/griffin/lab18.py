def peaks(data):
    for num in data:
        if num > data.index(num) and num > data.index(num+1)
        print(data[num])


def valleys():
    pass


def peaks_and_valleys():
    pass


def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    peaks(data)


if __name__ == "__main__":
    main()