# Kaprekar Constant (6174) Calculator

This project explores the Kaprekar constant (6174) and the number of iterations required to reach it using Kaprekar's routine.

## What is the Kaprekar Constant?

The Kaprekar constant is a number that arises when performing the following algorithm (Kaprekar's routine):

1. Take any four-digit number where not all digits are identical.
2. Arrange the digits in descending and ascending order to form two new numbers.
3. Subtract the smaller number from the larger number.
4. Repeat the process with the result.

After at most 7 iterations, the process will reach 6174, and then it will cycle, since 7641 - 1467 = 6174.

## Features

- `kaprekar_iterations(num)`: Calculates how many iterations it takes for a given number to reach 6174
- `export_highest_iteration_numbers_to_file()`: Finds all 4-digit numbers that take the maximum number of iterations to reach 6174 and exports them to a file

## Usage

```python
# Calculate iterations for a specific number
iterations = kaprekar_iterations(1234)
print(f"It takes {iterations} iterations for 1234 to reach 6174")

# Find all numbers that take the maximum iterations to reach 6174
export_highest_iteration_numbers_to_file()
```

## Results

The script generates a file called `highest_kaprekar_iterations.txt` which contains:
- The maximum number of iterations found
- All 4-digit numbers that take the maximum iterations to reach 6174

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. 