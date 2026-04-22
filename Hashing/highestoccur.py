arr_map=dict()
arr=[1,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5]

for i in range(len(arr)):
    if arr[i] in arr_map:
        arr_map[arr[i]]+=1
    else:
        arr_map[arr[i]]=1
    

sorted_dict=dict(sorted(arr_map.items(),key=lambda item: item[1]))

print(list(sorted_dict.keys())[-1])