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

# 1. one element array
test_one_element = {
    "input": {
      "nums" : [1]
    },
    "output": 0
}
# 2. two element array, with first element as peak
test_two_element_p1 = {
    "input": {
      "nums" : [1, 0]
    },
    "output": 0
}
# 3. two element array, with second element as peak
test_two_element_p2 = {
    "input": {
      "nums" : [1, 2]
    },
    "output": 1
}
# 4. n element array, with first element as peak
test_n_element_p1 = {
    "input": {
      "nums" : [9, 8, 7, 6, 5, 4, 3, 2, 1]
    },
    "output": 0
}
# 5. n element array, with last element as peak
test_n_element_p2 = {
    "input": {
      "nums" : [1, 2, 3, 4, 5, 6, 7, 8, 9]
    },
    "output": 8
}
# 6. n element array, with last n/2 element as peak
test_n_element_p3 = {
    "input": {
      "nums" : [1, 2, 3, 4, 100, 6, 7, 8, 6]
    },
    "output": 4
}
# 7. n element array, with peak in the first half of the array
test_n_element_p4 = {
    "input": {
      "nums" : [1, 2, 100, 6, 5, 4, 7, 8, 9]
    },
    "output": 2
}
# 8. n element array, with peak in the second half of the array 
test_n_element_p5 = {
    "input": {
      "nums" : [1, 2, 3, 4, 5, 6, 100, 8, 9]
    },
    "output": 6
}

test_cases = [
test_one_element, 
test_two_element_p1, 
test_two_element_p2, 
test_n_element_p1, 
test_n_element_p2, 
test_n_element_p3, 
test_n_element_p4, 
test_n_element_p5 
]