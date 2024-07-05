from unittest import TestCase, main


def sum_nums(a, b):
    return a + b


class TestSumNums(TestCase):
    def test_sum_nums(self):
        result = sum_nums(5, 6)
        expected_result = 11
        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    main()
