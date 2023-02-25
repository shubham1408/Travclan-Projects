def split_num(num,n):
    import ipdb; ipdb.set_trace()
    left = num[:n//2]
    if n%2 != 0:
        mid = [num[n//2]]
    else:
        mid = []
    if n%2 != 0:
        right = num[n//2+1:n]
    else:
        right = num[n//2:n]
    left = "".join(map(str, left))
    mid =   "".join(map(str, mid))
    right = "".join(map(str, right))
    return left,mid,right

def generateNextPalindrome(num, n) :
    # code here
    
    left,mid,right = split_num(num,n)
    import ipdb; ipdb.set_trace()
    if 10*n-1 == num:
        print (num+2)
        return [num+2]
    elif n == 1:
        num_str = "".join(map(str, num))
        return [int(num_str)+1]
    elif mid == "":
        if not int(left[::-1]) > int(right):
            left = str(int(left)+1)
        right = left[::-1]
    elif mid  != "":
        if not int(left[::-1]) > int(right):
            left_mid = str(int(left+mid)+1)
            left, mid = left_mid[:-1], left_mid[-1]
        right = left[::-1]
    
    output_arr = []
    for i in left:
        output_arr.append(int(i))
    for i in mid:
        output_arr.append(int(i))
    for i in right:
        output_arr.append(int(i))
    return output_arr

num = [9]
n = 1
generateNextPalindrome(num, n)



