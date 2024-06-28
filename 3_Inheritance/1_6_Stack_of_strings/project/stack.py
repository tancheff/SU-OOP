from typing import List


class Stack:
    def __init__(self):
        self.data: List[str] = []

    def is_empty(self) -> bool:
        if len(self.data) == 0:
            return True
        return False

    def __str__(self):
        final_stack = "[" + ", ".join(reversed([str(el) for el in self.data])) + "]"
        return final_stack

    def push(self, element) -> None:
        self.data.append(element)

    def pop(self) -> int or str:
        if self.is_empty():
            raise IndexError("Stack is empty!")
        last_element = self.data.pop()
        return last_element

    def top(self) -> int or str:
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.data[-1]


# test zero
import unittest


class StackTests(unittest.TestCase):
    def test_zero(self):
        stack = Stack()
        stack.push("apple")
        stack.push("carrot")
        self.assertEqual(str(stack), '[carrot, apple]')
        self.assertEqual(stack.pop(), 'carrot')
        self.assertEqual(stack.top(), 'apple')
        stack.push("cucumber")
        self.assertEqual(str(stack), '[cucumber, apple]')
        self.assertEqual(stack.is_empty(), False)


if __name__ == '__main__':
    unittest.main()