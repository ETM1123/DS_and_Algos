from locate_cards_tests import test_cases, large_test, evaluate_test
from locate_card_brute_force import locate_card_linear_search
from locate_card_optimized import locate_card_binary_search




if __name__ == "__main__":
    print("regular test cases:\n")
    evaluate_test(test_cases, locate_card_linear_search, display=False)
    evaluate_test(test_cases, locate_card_binary_search, display=False)
    print("Large file")
    evaluate_test(large_test, locate_card_linear_search, display=False)
    evaluate_test(large_test, locate_card_binary_search, display=False)
