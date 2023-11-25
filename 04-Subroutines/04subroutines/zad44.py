def f(password):
    if len(password)<6:
        return False
    else:
        return True

password='homiczek'
print(f(password))     