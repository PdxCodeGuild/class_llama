# Contact List


with open('contacts.csv', 'r') as file:
    # split twice
    # split each line into a list of strings
    lines = file.read().split('\n')
    # make each line a list
    split_lines = []
    # split at each comma
    for line in lines:
        split_lines.append(line.split(','))
    # print(split_lines)

    # keys are from the first line/list
    keys = split_lines[0]

    contacts = []
    # iterate through all other lines (after key line, 0)
    for k in range(1, len(split_lines)):
        # match keys to each value, new dictionary for each new line
        contacts.append(dict(zip(keys, split_lines[k])))
    print(contacts)
