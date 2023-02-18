"""Test cases"""
from time import time
def evaluate_test(test_cases : list[int], func : callable, display=True):
  print(f"Testing {func.__name__} .... ")
  for num_test_case, test_case in enumerate(test_cases):
    print(f"Test {num_test_case + 1}")
    start_time = time()
    try:
      actual_output = func(**test_case["input"])
      print(f"actual output: {actual_output}")
      assert actual_output == test_case["output"]
      
      if display:
        print(f"Test {num_test_case}: \n Input: {test_case['input']} \n\n Expected output: {test_case['output']}")
        print(f"Actual output: {actual_output}\n")
      end_time = time()
      passed_message = f"passed! took {round(end_time - start_time, 10)} seconds \n"
      print(passed_message)
    except AssertionError as e:
      end_time = time()
      failed_message = f"failed!  took {round(end_time - start_time, 10)} seconds \n"
      print(failed_message)
      print(f"failed message: {e}")

# test cases
## 1. general case some rotation
test_general_case = {
    "input":
     {
    "nums" :[5, 6, 9, 0, 2, 3, 4],
    "target" : 0
      },
    "output" : 3
}
## 2. max rotation (N-1) times (reverse order)
test_max_rotation = {
    "input" : 
      {
    "nums" :[2, 3, 4, 5, 6, 9, 0],
    "target" : 2
       },
    "output" : 0
}

## 3. No rotation i.e sorted list
test_sorted_nums = {
    "input" : 
      {
    "nums" :[0, 2, 3, 4, 5, 6, 9],
    "target" : 3
       },
    "output" : 3
}


## 4. One element list
test_one_number = {
    "input":
     {
    "nums" :[1],
    "target" : 1
      },
    "output": 0
}

# 5. empty list
test_empty_list = {
    "input" : 
      {
    "nums" :[],
    "target" : 1
      },
    "output" : -1
}


test_cases = [
  test_general_case,
  test_max_rotation,
  test_sorted_nums,
  test_one_number,
  test_empty_list
]