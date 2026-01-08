# Filter function is a in-build function used to filer the sequence as per condition
# ====>> filter(function,sequence)

def topper(marks):
    return marks>80
test_marks =[50,66,40,85,75,90]
topper_list=list(filter(topper,test_marks))
print(topper_list)