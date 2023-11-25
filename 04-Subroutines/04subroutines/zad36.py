def f(detector):
    count=0
    max_people=0

    for event in detector:
        if event=='+':
            count=count+1
            max_people=max_people+count
        elif event=='-':
            count=count-1

    return max_people>=3

print(f("+-+++-+---")) 