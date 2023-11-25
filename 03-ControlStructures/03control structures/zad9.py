total_tasks=30
correct_tasks=int(input('Enter the number of correct tasks: '))

if correct_tasks>=0.5*total_tasks:
    print('Test passed')
else:
    print('Test failed')    