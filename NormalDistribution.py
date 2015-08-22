

def arithmetic_average(the_list):
    return float(sum(the_list))/len(the_list) if len(the_list) > 0 else float('nan')


def normal_distributions(length):
    from random import gauss
    result = []
    for i in range(0, length):
        result.append(gauss(0, 1))
    return result


def verify_normal_distributions(data):
    return max(data), min(data), arithmetic_average(data)


# 決定要幾筆資料，以怎樣的組合回傳
if __name__ == "__main__":
    counts = 3000
    a= normal_distributions(counts)
    # b= normal_distributions(counts)
    # c= normal_distributions(counts)
    re2 = []
    for i in range(counts):
        re2.append([i, a[i]])
    print(re2)