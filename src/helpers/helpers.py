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