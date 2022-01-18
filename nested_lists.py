

if __name__ == '__main__':
    scores = []
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     scores.append([name,score])
    scores = [['Harry',-50],['Berry',-50],['Tina',-50],['Akriti',4]]
    sorted_list = sorted(scores,key=lambda x: x[1])
    sec_low = sorted(list(set([x[1] for x in sorted_list])))
    print(sec_low)
    sec_low = sec_low[1]
    output = []
    for i in sorted_list:
        if i[1] == sec_low:
            output.append(i)
    final = sorted(output,key=lambda x:x[0])
    for name in final:
        print(name[0])
    