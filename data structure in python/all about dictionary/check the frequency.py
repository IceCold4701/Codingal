#initialize dictionary
test_dict={'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Codingal' : 1}
#printing original dictionary
print("the original dictionary : " + str(test_dict))
#initialize value
K=2
#using loop
#selective keep values in dictionary
res=0
for key in test_dict:
    if test_dict[key]==K:
        res=res+1
#printing result
print("Frequency of K is : " + str(res))