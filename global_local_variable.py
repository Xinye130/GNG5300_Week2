# Global variable
global_var = 10

def my_function():
    # Local variable
    local_var = 5
    print("Inside the function:")
    print("Local variable:", local_var)
    print("Global variable:", global_var)

# Accessing global variable outside the function
print("Outside the function:")
print("Global variable:", global_var)

# Calling the function
my_function()