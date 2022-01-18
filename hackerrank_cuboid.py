def cuboid(x: int,y: int,z: int,n: int) -> list:
    x_list = [i for i in range(x+1)]
    y_list = [j for j in range(y+1)]
    z_list = [k for k in range(z+1)]
    final_list = []
    for i in x_list:
        for j in y_list:
            for k in z_list:
                if i+j+k != n:
                    final_list.append([i,j,k])
    return final_list

    pass



if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    ans = cuboid(x,y,z,n)
    print(ans)
