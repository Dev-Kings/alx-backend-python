# 0x03. Unittests and Integration Tests

## Project Overview
This project focuses on understanding and implementing **unit tests** and **integration tests** in Python. Through this project, we will explore common testing patterns such as **mocking**, **parametrizations**, and **fixtures**. By the end, you should be able to differentiate between unit and integration tests and apply these techniques in real-world applications.

## Table of Contents
- [Introduction to Unit Testing](#introduction-to-unit-testing)
- [Introduction to Integration Testing](#introduction-to-integration-testing)
- [Learning Objectives](#learning-objectives)
- [Requirements](#requirements)
- [How to Execute Tests](#how-to-execute-tests)
- [Resources](#resources)

## Introduction to Unit Testing
**Unit testing** is the process of testing individual functions to ensure they return expected results for a variety of inputs, including edge cases. Unit tests:
- Are designed to validate the logic within a single function.
- Should mock most external function calls, especially those involving network or database interactions.
- Aim to answer the question: *Does this function work as expected if everything else behaves correctly?*

## Introduction to Integration Testing
**Integration testing** tests code paths from end to end. These tests:
- Validate interactions between different parts of the application.
- Only mock low-level functions, especially those that make external calls (e.g., HTTP requests, file I/O, database operations).

## Learning Objectives
1. Differentiate between unit and integration tests.
2. Understand and apply testing patterns like mocking, parametrizations, and fixtures.

## How to Execute Tests
To run your tests, use the following command:
```bash
$ python -m unittest path/to/test_file.py
```
## Resources
For further reference and detailed information, consider reading or watching the following resources:

[unittest](https://docs.python.org/3/library/unittest.html) — Unit testing framework: An introduction to Python's built-in unit testing framework.
[unittest.mock](https://docs.python.org/3/library/unittest.mock.html) — mock object library: Details on using the mock library to replace parts of your system under test and make assertions about how they are used.
[How to mock a readonly property with mock](https://stackoverflow.com/questions/11836436/how-to-mock-a-readonly-property-with-mock): Tips for mocking read-only properties in Python.
[parameterized](https://pypi.org/project/parameterized/): A Python package for parameterized testing in unittest.
[Memoization](https://en.wikipedia.org/wiki/Memoization): A Wikipedia article explaining memoization, a technique used to optimize code by caching results.


