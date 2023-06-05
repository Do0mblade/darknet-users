#С функцией

# входные данные

#data = [9, 3, '7', '3']
#data = ['5', '0', 9, 3, 2, 1, '9', 6, 7]
data = ['3', 6, 6, 0, '5', 8, 5, '6', 2,'0']

def difference(data):
    data_int = 0
    data_str = 0
    for i in data:
        if type(i) is int:
            data_int += i
        elif type(i) is str:
            data_str += int(i)

    return data_int - data_str

print(difference(data))

if __name__ == '__main__':
    pass