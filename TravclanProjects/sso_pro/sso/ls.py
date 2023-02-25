
# def find_second_max(array):
#     if len(array) < 2:
#         return "-1"
#     max_first = int(array[0])
#     max_second = int(array[1])
#     if max_first < max_second and len(array) == 2:
#         return max_first
#     if max_first < max_second:
#         temp = max_first
#         max_first = max_second
#         max_second = temp
#     for item in range(2,len(array)):
#         if int(array[item]) > max_first:
#             temp = max_first
#             max_first = int(array[item])
#             max_second = temp
#         if (max_first == max_second) or (max_second < int(array[item]) < max_first):
#             max_second = int(array[item])
#     if max_first == max_second:
#         return "-1"
#     return str(max_second)

# array = ["-33", "-4", "-5"]
# print(find_second_max(array))

arr = [1,4,45,6,10,8]

def pairs_with_value_x(arr,x):

    set_arr = set(arr)
    already_taken = set()
    for i in arr:
        if i in already_taken:
            continue
        temp = x-i
        if temp in set_arr:
            print (i,temp)
            already_taken.add(temp)


pairs_with_value_x(arr,16)












