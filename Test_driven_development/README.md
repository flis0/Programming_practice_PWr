### Collaborative TDD Exercise

This project demonstrates a unique take on **Test-Driven Development (TDD)**. Two people write tests for the same problem, then swap and write the code to pass each other's tests.

### Given Problem
Based on the **String Calculator Kata**, the task involves:
* **Basic Addition**: Support up to two numbers (e.g., `""`, `"1"`, `"1,2"`).
* **Empty Strings**: Return `0` for an empty input.
* **Scalability**: Extend the function to handle an unknown amount of numbers.
* **Error Handling**: Throw a `ValueError` for invalid inputs (e.g., letters).
* **Newlines**: Support `\n` as a valid separator in addition to commas.

### Project Structure
* **Test Suite 1 (`tests_1.py`):** Developed by **Szymon Flis @flis0**. Defines the initial test requirements.
* **Test Suite 2 (`tests_2.py`):** Developed by **Iwo Chwiszczuk @iwonieevo**. Defines independent test cases.
* **Implementation 1 (`solution_1.py`):** Developed by **Iwo Chwiszczuk @iwonieevo**. Code written to pass `tests_1.py`.
* **Implementation 2 (`solution_2.py`):** Developed by **Szymon Flis @flis0**. Code written to pass `tests_2.py`.

### The Process
1. **Write Tests**: Each person writes unit tests for the String Calculator.
2. **Swap**: Partners exchange files/computers.
3. **Implement**: Each person writes the code required to make the swapped tests pass.