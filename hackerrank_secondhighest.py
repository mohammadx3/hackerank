if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    copy = list(arr)
    final_lst = sorted(list(set(copy)))
    print(final_lst[-2])