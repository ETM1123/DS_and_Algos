from test_cases import test_cases
from helpers import evaluate_test
from solutions import find_peak

if __name__ == "__main__":
  evaluate_test(test_cases, find_peak, display=False)