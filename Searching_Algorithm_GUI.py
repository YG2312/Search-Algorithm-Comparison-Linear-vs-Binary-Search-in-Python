import time
import sys
import tkinter as tk
from tkinter import messagebox

# Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Function to calculate space used by variables
def get_space_used(*vars):
    return sum(sys.getsizeof(var) for var in vars)

# Function to compare linear and binary search
def compare_search(arr, target):
    target = int(target)
    
    # Linear Search
    start_time = time.time()
    linear_result = linear_search(arr, target)
    end_time = time.time()
    linear_time = end_time - start_time
    linear_space = get_space_used(arr, target)

    # Binary Search (on sorted array)
    sorted_arr = sorted(arr)
    start_time = time.time()
    binary_result = binary_search(sorted_arr, target)
    end_time = time.time()
    binary_time = end_time - start_time
    binary_space = get_space_used(sorted_arr, target)
    
    return (linear_result, linear_time, linear_space, binary_result, binary_time, binary_space)

# GUI Application
def search_comparison():
    try:
        # Retrieve user inputs
        arr = list(map(int, entry_array.get().split(',')))
        target = int(entry_target.get())

        # Perform the search comparison
        linear_result, linear_time, linear_space, binary_result, binary_time, binary_space = compare_search(arr, target)

        # Display results in message boxes
        linear_message = (
            f"Linear Search:\n"
            f"Element {'found' if linear_result != -1 else 'not found'}\n"
            f"Time taken: {linear_time:.10f} seconds\n"
            f"Space used: {linear_space} bytes"
        )
        binary_message = (
            f"Binary Search (on sorted array):\n"
            f"Element {'found' if binary_result != -1 else 'not found'}\n"
            f"Time taken: {binary_time:.10f} seconds\n"
            f"Space used: {binary_space} bytes"
        )
        messagebox.showinfo("Search Results", f"{linear_message}\n\n{binary_message}")
        
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid array of integers and target value.")

# Setting up the Tkinter GUI
root = tk.Tk()
root.title("Search Comparison Tool")

# Array input label and entry
label_array = tk.Label(root, text="Enter Array (comma-separated integers):")
label_array.pack(pady=5)
entry_array = tk.Entry(root, width=50)
entry_array.pack(pady=5)

# Target input label and entry
label_target = tk.Label(root, text="Enter Target Value:")
label_target.pack(pady=5)
entry_target = tk.Entry(root, width=20)
entry_target.pack(pady=5)

# Search button
btn_search = tk.Button(root, text="Compare Searches", command=search_comparison)
btn_search.pack(pady=10)

# Run the application
root.mainloop()
