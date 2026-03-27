# Duplicate Remover Program

A Python program that identifies repeated numbers and characters, then removes duplicates to show only unique elements.

## Features

- ✅ Identifies repeated elements (numbers and characters)
- ✅ Removes duplicates while preserving order
- ✅ Works with mixed data types (integers and strings)
- ✅ Shows detailed analysis including frequencies
- ✅ Interactive mode for user input
- ✅ Multiple example demonstrations

## How It Works

The program uses two main approaches:

1. **Set-based deduplication**: Uses a set to track seen elements and maintain order
2. **Frequency counting**: Counts occurrences of each element to identify duplicates

## Usage

### Running the Program

```bash
python duplicate_remover.py
# or
python3 duplicate_remover.py
```

### Program Output

The program will show:
- Original list contents
- Elements that are repeated
- Unique elements (duplicates removed)
- Frequency count for each element
- Analysis summary

### Examples

#### Example 1: Mixed Data
```python
Input: [1, 2, 3, 2, 4, 1, 5, 'a', 'b', 'a', 'c', 3]
Repeated Elements: [1, 2, 3, 'a']
Unique Elements: [1, 2, 3, 4, 5, 'a', 'b', 'c']
```

#### Example 2: Numbers Only
```python
Input: [10, 20, 30, 20, 10, 40, 50, 30, 60]
Repeated Elements: [10, 20, 30]
Unique Elements: [10, 20, 30, 40, 50, 60]
```

#### Example 3: Characters Only
```python
Input: ['x', 'y', 'z', 'x', 'a', 'y', 'b', 'x']
Repeated Elements: ['x', 'y']
Unique Elements: ['x', 'y', 'z', 'a', 'b']
```

## Interactive Mode

After showing examples, the program enters interactive mode:

```
🎮 INTERACTIVE MODE
Enter numbers/characters separated by spaces (or 'quit' to exit):
Enter list: 1 2 3 2 4 a b a
```

The program will analyze your input and show the results.

## Functions

### `remove_duplicates(input_list)`
Removes duplicate elements while preserving order.

### `find_duplicates(input_list)`
Returns a list of elements that appear more than once.

### `analyze_list(input_list)`
Provides complete analysis of a list including duplicates and unique elements.

## Requirements

- Python 3.x
- No external dependencies required

## Algorithm Details

1. **Duplicate Removal**: Uses a set to track seen elements, ensuring O(n) time complexity while preserving insertion order.

2. **Duplicate Detection**: Uses a dictionary to count element frequencies, then filters for elements with count > 1.

3. **Mixed Type Support**: Handles both integers and strings seamlessly.

## Error Handling

- Handles empty input gracefully
- Supports mixed data types
- Provides clear error messages for invalid input
- Allows graceful exit with 'quit' command

## Use Cases

- Data cleaning and preprocessing
- Finding duplicate entries in datasets
- Educational examples for set operations
- Interactive data analysis tools