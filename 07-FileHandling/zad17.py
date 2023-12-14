def display_lines(file_path, lines_per_iteration):
    with open(file_path, 'r') as file:
        all_lines = file.readlines()

    total_lines = len(all_lines)
    start = 0

    while start < total_lines:
        end = start + lines_per_iteration
        print(''.join(all_lines[start:end]))

        if end%5==0:
            input('Press enter to continue...')
        start = end

file_path = 'dzialaj.txt'
lines_per_iteration = 5

# No need to print the result as the function doesn't return anything meaningful
display_lines(file_path, lines_per_iteration)

