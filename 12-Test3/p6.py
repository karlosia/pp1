def f(vname):
    if len(vname)>1 and len(vname)<5:
        if vname.startswith('_') or vname[0].isalpha():
            return True
        else: 
            return False
    else:
        return False

print(f("abc"))      # Output: True
print(f("Abc"))      # Output: True
print(f("aBC"))      # Output: True
print(f("_ab_c"))    # Output: True
print(f("abcdef"))   # Output: False
print(f("8abc"))     # Output: False
print(f("_aB8_"))    # Output: True
print(f("_4x"))      # Output: True       