#!/usr/bin/env python3
"""
Simple test cases for the duplicate remover program.
Run this to verify the functionality works correctly.
"""

from duplicate_remover import remove_duplicates, find_duplicates

def test_remove_duplicates():
    """Test the remove_duplicates function"""
    print("🧪 Testing remove_duplicates function...")

    # Test 1: Mixed numbers and characters
    test1 = [1, 2, 3, 2, 4, 1, 'a', 'b', 'a']
    result1 = remove_duplicates(test1)
    expected1 = [1, 2, 3, 4, 'a', 'b']
    assert result1 == expected1, f"Test 1 failed: expected {expected1}, got {result1}"
    print("✅ Test 1 passed: Mixed numbers and characters")

    # Test 2: Only duplicates
    test2 = [5, 5, 5, 5]
    result2 = remove_duplicates(test2)
    expected2 = [5]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("✅ Test 2 passed: Only duplicates")

    # Test 3: No duplicates
    test3 = [1, 2, 3, 4, 5]
    result3 = remove_duplicates(test3)
    expected3 = [1, 2, 3, 4, 5]
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print("✅ Test 3 passed: No duplicates")

    # Test 4: Empty list
    test4 = []
    result4 = remove_duplicates(test4)
    expected4 = []
    assert result4 == expected4, f"Test 4 failed: expected {expected4}, got {result4}"
    print("✅ Test 4 passed: Empty list")

def test_find_duplicates():
    """Test the find_duplicates function"""
    print("\n🧪 Testing find_duplicates function...")

    # Test 1: Multiple duplicates
    test1 = [1, 2, 3, 2, 4, 1, 5, 3]
    result1 = find_duplicates(test1)
    expected1 = [1, 2, 3]  # Order may vary
    assert set(result1) == set(expected1), f"Test 1 failed: expected {expected1}, got {result1}"
    print("✅ Test 1 passed: Multiple duplicates")

    # Test 2: Single duplicate
    test2 = [1, 1]
    result2 = find_duplicates(test2)
    expected2 = [1]
    assert result2 == expected2, f"Test 2 failed: expected {expected2}, got {result2}"
    print("✅ Test 2 passed: Single duplicate")

    # Test 3: No duplicates
    test3 = [1, 2, 3, 4, 5]
    result3 = find_duplicates(test3)
    expected3 = []
    assert result3 == expected3, f"Test 3 failed: expected {expected3}, got {result3}"
    print("✅ Test 3 passed: No duplicates")

    # Test 4: Characters
    test4 = ['a', 'b', 'c', 'a', 'b']
    result4 = find_duplicates(test4)
    expected4 = ['a', 'b']  # Order may vary
    assert set(result4) == set(expected4), f"Test 4 failed: expected {expected4}, got {result4}"
    print("✅ Test 4 passed: Character duplicates")

if __name__ == "__main__":
    print("🚀 Running Duplicate Remover Tests")
    print("=" * 50)

    try:
        test_remove_duplicates()
        test_find_duplicates()

        print("\n" + "=" * 50)
        print("🎉 All tests passed successfully!")
        print("✅ The duplicate remover program is working correctly.")

    except AssertionError as e:
        print(f"\n❌ Test failed: {e}")
        exit(1)
    except Exception as e:
        print(f"\n💥 Unexpected error: {e}")
        exit(1)