def f(expression):
    try:
        result=eval
        return result
    except Exception as e:
        print(f"Error: {e}")
        return None


print(f("2+3"))      
print(f("3+8+1"))   
print(f("2+3-4+5-0")) 