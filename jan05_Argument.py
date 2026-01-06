# 1. Positional Argument
def sign_up(en,age,sal,cn):
    print(f"Employee name is {en}")
    print(f"Employee age is {age}")
    print(f"Employee Salary is {sal}")
    print(f"Employee Company is {cn}")
sign_up("sai",21,"TCS",60000)

# 2.Key word Argument
        # Position is not matters here. Data is passed in key-word
def sign_up2(en,age,sal,cn):
    print(f"Employee name is {en}")
    print(f"Employee age is {age}")
    print(f"Employee Salary is {sal}")  
    print(f"Employee Company is {cn}")
sign_up2(en="sai",age=21,cn="TCS",sal=60000)

# 3. Default Arguments
        # Default value is passed at the time of function defination
        # first position cannot pass as default
        # After passing Default value, for next there must be not a normal parameter  
        # As final the Default parameters as passed at last

def sign_up3(en,age,sal,cn ="TCS"):
    print(f"Employee name is {en}")
    print(f"Employee age is {age}")
    print(f"Employee Salary is {sal}")
    print(f"Employee Company is {cn}")
sign_up3(en="sai",age=21,sal=60000)


# 4. Arbitary Arguments 
def submit(**details):
    print(details)
    print(type(details))
    for k in details.items():
        print(k,"---")
submit(name ="sai",mobile=9371323603)