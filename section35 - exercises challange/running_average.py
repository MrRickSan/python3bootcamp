'''
rAvg = running_average();
rAvg(10) // 10.0;
rAvg(11) // 10.5;
rAvg(12) // 11;

rAvg2 = running_average()
rAvg2(1) // 1
rAvg2(3) // 2
'''


def running_average():
    data = []

    def data_average(n):
        data.append(n)
        return sum(data) / len(data)
    return data_average


rAvg = running_average()
print(rAvg(10))  # 10.0
print(rAvg(11))  # 10.5
print(rAvg(12))  # 11
