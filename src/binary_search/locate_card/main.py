from solutions import locate_card_binary_search, locate_card_linear_search, locate_card 
from test_cases import test_cases, large_test
from helpers.helpers import evaluate_test

if __name__ == "__main__":
    print("regular test cases:\n")
    evaluate_test(test_cases, locate_card_linear_search, display=False)
    evaluate_test(test_cases, locate_card_binary_search, display=False)
    print("Large file")
    evaluate_test(large_test, locate_card_linear_search, display=False)
    evaluate_test(large_test, locate_card_binary_search, display=False)
