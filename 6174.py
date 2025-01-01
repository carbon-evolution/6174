def kaprekar_iterations(num):
    iterations = 0
    while num != 6174:
        # Convert the number to a string and ensure it has 4 digits (add leading zeros if necessary)
        num_str = f"{num:04d}"
        
        # Create the largest and smallest possible numbers from the digits
        largest = int("".join(sorted(num_str, reverse=True)))
        smallest = int("".join(sorted(num_str)))
        
        # Subtract the smaller number from the larger number
        num = largest - smallest
        
        # Increment the iteration counter
        iterations += 1
        
        # Stop if it has been running too long (safety check)
        if iterations > 10:
            return iterations

    return iterations

def export_highest_iteration_numbers_to_file():
    max_iterations = 0
    numbers_with_max_iterations = []
    
    for i in range(1, 10000):
        # Skip numbers with all identical digits (e.g., 1111, 2222, etc.)
        if len(set(str(i).zfill(4))) == 1:
            continue
        
        iterations = kaprekar_iterations(i)
        
        # Track the highest number of iterations
        if iterations > max_iterations:
            max_iterations = iterations
            numbers_with_max_iterations = [(i, iterations)]
        elif iterations == max_iterations:
            numbers_with_max_iterations.append((i, iterations))
    
    # Write results to a file
    with open("highest_kaprekar_iterations.txt", "w") as file:
        file.write(f"Highest number of iterations: {max_iterations}\n")
        file.write("Numbers that took the highest iterations:\n")
        for num, iter_count in numbers_with_max_iterations:
            file.write(f"{str(num).zfill(4)}: {iter_count} iterations\n")
    
    print(f"Results exported to 'highest_kaprekar_iterations.txt'")

# Run the function to calculate and export the results
export_highest_iteration_numbers_to_file()
