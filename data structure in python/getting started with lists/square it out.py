def SquareValues(beg, end):
    lst=[]
    for i in range (beg, end):
        #append value to the list
        lst.append(i**2)
    lst_even=[]
    lst_odd=[]
    for i in lst:
        if i%2==0:
            lst_even.append(i)
        else:
            lst_odd.append(i)
    print("Here is a list of even squares with specified ranges",lst_even)
    print("Here is a list of odd squares with specified ranges",lst_odd)
beg=int(input("Enter starting range:"))
end=int(input("Enter end range:"))
SquareValues(beg, end)