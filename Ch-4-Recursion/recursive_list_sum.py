def recursive_list_sum(numList: list[int]) -> int:
    if len(numList) == 1:  # Base Case: There is only one integer in the list
        return numList[0]
    else:  # Add the first integer and pass the rest of the list in to the
        # next recursion call
        return numList[0] + recursive_list_sum(numList[1:])
        # Python slicing [1:] retrieve items from index 1 to end


if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5]
    print(f"The sum of the list {numbers} is {recursive_list_sum(numbers)}")
