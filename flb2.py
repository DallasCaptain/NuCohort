# # Ultimate Analysis - Create a function that takes a list 
# # and returns a dictionary that has the sumTotal, 
# # average, minimum, maximum and length of the list.
# # Example: ultimate_analysis([37,2,1,-9]) should 
# # return {'sumTotal': 31, 'average': 7.75, 'minimum': -9, 
# # 'maximum': 37, 'length': 4 }


# def ultimate_analysis(lst):
#     sumTotal=0
#     average=0
#     minimum=lst[0]
#     maximum=lst[0]
#     length=0
#     for val in lst:
#         sumTotal += val
#         length += 1
#         minimum = min(minimum, val)
#         maximum = max(maximum, val)
    
#     average = sumTotal/length

#     return(
#         {'sumTotal': sumTotal,
#         'average': average,
#         'minimum': minimum,
#         'maximum': maximum,
#         'length': length
#         }
#     )

# print(ultimate_analysis([37,2,1,-9]))



# # reverse_list([37,2,1,-9]) should return [-9,1,2,37]

# def reverse_list(lst):
#     for i in range(int(len(lst)/2)):
#         temp = lst[i]
#         lst[i] = lst[len(lst)-1-i]
#         lst[len(lst)-1-i] = temp
#     print(lst)

# reverse_list([37,2,1,-9])


print([1,2,3,4])