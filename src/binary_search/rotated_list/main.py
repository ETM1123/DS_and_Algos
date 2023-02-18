from test_cases import test_cases, evaluate_test
from search import search


if __name__ == "__main__":
  evaluate_test(test_cases, search, display=False)