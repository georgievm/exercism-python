def value(colors):
    encoding = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']

    return int(str(encoding.index(colors[0])) + str(encoding.index(colors[1])))
