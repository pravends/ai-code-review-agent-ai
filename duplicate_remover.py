#!/usr/bin/env python3
"""
Program to identify and remove repeated numbers/characters from a list.
This program works with both integers and characters, removing duplicates
and showing only unique elements.
"""

def remove_duplicates(input_list):
    """
    Remove duplicate elements from a list and return unique elements.

    Args:
        input_list: List containing numbers and/or characters

    Returns:
        List with only unique elements (duplicates removed)
    """
    # Use a set to track seen elements and preserve order
    seen = set()
    unique_elements = []

    for item in input_list:
        if item not in seen:
            seen.add(item)
            unique_elements.append(item)

    return unique_elements

def find_duplicates(input_list):
    """
    Find and return elements that appear more than once.

    Args:
        input_list: List containing numbers and/or characters

    Returns:
        List of elements that are repeated (duplicates)
    """
    element_count = {}
    duplicates = []

    # Count frequency of each element
    for item in input_list:
        element_count[item] = element_count.get(item, 0) + 1

    # Find elements that appear more than once
    for item, count in element_count.items():
        if count > 1:
            duplicates.append(item)

    return duplicates

def analyze_list(input_list):
    """
    Analyze a list to show original content, duplicates found, and unique elements.

    Args:
        input_list: List to analyze
    """
    print("🔍 LIST ANALYSIS")
    print("=" * 50)
    print(f"📋 Original List: {input_list}")
    print(f"📊 List Length: {len(input_list)}")

    # Find duplicates
    duplicates = find_duplicates(input_list)
    print(f"🔄 Repeated Elements: {duplicates}")
    print(f"📈 Number of Duplicates: {len(duplicates)}")

    # Get unique elements
    unique_elements = remove_duplicates(input_list)
    print(f"✅ Unique Elements: {unique_elements}")
    print(f"📊 Unique Count: {len(unique_elements)}")

    # Show frequency of each element
    print("\n📈 ELEMENT FREQUENCY:")
    element_count = {}
    for item in input_list:
        element_count[item] = element_count.get(item, 0) + 1

    for item, count in sorted(element_count.items(), key=lambda x: x[1], reverse=True):
        status = "🔄 REPEATED" if count > 1 else "✅ UNIQUE"
        print(f"  {item}: {count} times - {status}")

    print("=" * 50)

def main():
    """Main function with example usage"""
    print("🎯 DUPLICATE REMOVER PROGRAM")
    print("This program identifies repeated numbers/characters and removes duplicates\n")

    # Example 1: Mixed numbers and characters
    print("Example 1: Mixed Numbers and Characters")
    example1 = [1, 2, 3, 2, 4, 1, 5, 'a', 'b', 'a', 'c', 3]
    analyze_list(example1)

    # Example 2: Only numbers
    print("\nExample 2: Numbers Only")
    example2 = [10, 20, 30, 20, 10, 40, 50, 30, 60]
    analyze_list(example2)

    # Example 3: Only characters
    print("\nExample 3: Characters Only")
    example3 = ['x', 'y', 'z', 'x', 'a', 'y', 'b', 'x']
    analyze_list(example3)

    # Example 4: Single repeated element
    print("\nExample 4: Single Element Repeated")
    example4 = [7, 7, 7, 7, 7]
    analyze_list(example4)

    # Example 5: No duplicates
    print("\nExample 5: No Duplicates")
    example5 = [1, 2, 3, 4, 5, 'a', 'b', 'c']
    analyze_list(example5)

    # Interactive example
    print("\n🎮 INTERACTIVE MODE")
    print("Enter numbers/characters separated by spaces (or 'quit' to exit):")

    while True:
        try:
            user_input = input("Enter list: ").strip()

            if user_input.lower() == 'quit':
                print("👋 Goodbye!")
                break

            if not user_input:
                print("❌ Please enter some values!")
                continue

            # Parse input - try to convert to numbers, keep as strings if not
            elements = []
            for item in user_input.split():
                try:
                    # Try to convert to int
                    elements.append(int(item))
                except ValueError:
                    # If not a number, keep as string
                    elements.append(item)

            analyze_list(elements)

        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")
            print("Please try again with proper input format.")

if __name__ == "__main__":
    main()