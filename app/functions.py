import csv
import re


def get_list_from_csv() -> list[list[str]]:
    file = open("data.csv", "r")
    data = list(csv.reader(file, delimiter=","))
    return data


def get_page_numbers(strings: list, pattern: str = r"\d+") -> list[int]:
    numbers: list[int] = []
    for string in strings:
        string = string[0]
        m = re.search(pattern=pattern, string=string)
        if m is not None:
            numbers.append(int(m.group()))
    return numbers


def get_duplicates(unique_numbers: list[int], numbers: list[int]) -> dict:
    duplicates: dict = {}
    for number in unique_numbers:
        number_count = numbers.count(number)
        if number_count > 1:
            duplicates[f"Number {number}"] = f"appeared {number_count} times."
    return duplicates


def get_sorted_numbers_and_duplicates_info(numbers: list[int]) -> dict:
    sorted_and_unique_numbers = sorted(list(set(numbers)))
    duplicates = get_duplicates(sorted_and_unique_numbers, numbers)
    return {"numbers": sorted_and_unique_numbers, "duplicates": duplicates}


def get_missing_numbers(sorted_and_unique_numbers: list[int]) -> list[int]:
    missing_numbers: list[int] = []
    numbers = sorted_and_unique_numbers
    for index, number in enumerate(numbers):
        if index != len(numbers) - 1:
            next_number = numbers[index + 1]
            if number != next_number - 1:
                for missing_number in range(number + 1, next_number):
                    missing_numbers.append(missing_number)
    return missing_numbers


# def print_info_about_missing_numbers_and_duplicates() -> None:
#     print("work in progress")
