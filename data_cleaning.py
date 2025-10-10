# Data Cleaning using Python Data Structures

def remove_duplicates(data_list):
    return list(set(data_list))

def filter_data(data_list, threshold):
    return [item for item in data_list if item >= threshold]

if __name__ == "__main__":
    data = [10, 20, 20, 30, 40, 10, 50, 60, 30]
    print("Original Data:", data)
    print("After Removing Duplicates:", remove_duplicates(data))
    print("Filtered Data (>=30):", filter_data(data, 30))
