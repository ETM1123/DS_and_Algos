from test_cases import test_cases, evaluate_test
from find_peak_1d import find_peak

if __name__ == "__main__":
  evaluate_test(test_cases, find_peak, display=False)