# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]) With True, it gives the answer

# return a string that describes an error if :
# more than five, Error: Too many problems.
# Multiplication and division will return an error, Error: Operator must be '+' or '-'.
# Error: Numbers must only contain digits.
# Error: Numbers cannot be more than four digits.


def arithmetic_arranger(operations, show_results=False):
    """Create a function that receives a list of strings that are arithmetic 
    problems and returns the problems arranged vertically and side-by-side.

    Args:
        operations (list): list of addition and subtraction operations.
        show_results (bool, optional): if True, show results of operations. Defaults to False.
    """

    if len(operations) > 5:
        return "Error: Too many problems."

    first_line, second_line, thrid_line, forth_line = [], [], [], []
    for operation in operations :
        first_operand, operator, second_operand = operation.split()

        # Check for * or /
        if any(op in operator for op in ["*", "/"]):
            return "Error: Operator must be '+' or '-'."

        # Check the digits
        if not (first_operand.isdigit() and second_operand.isdigit()):
            return "Error: Numbers must only contain digits."

        # Check the length
        if len(first_operand) > 4 or len(second_operand) > 4:
            return "Error: Numbers cannot be more than four digits."

        spaces = max(len(first_operand), len(second_operand))

        first_line.append(f'{first_operand:>{spaces + 2}}')
        second_line.append(f'{operator} {second_operand:>{spaces}}')
        thrid_line.append(f'{"-"*(spaces + 2)}')

        if show_results:
            first_operand, second_operand = int(first_operand), int(second_operand)
            if operator == '+':
                forth_line.append(f'{int(first_operand) + int(second_operand):>{spaces + 2}}')
            else:
                forth_line.append(f'{int(first_operand) - int(second_operand):>{spaces + 2}}')

        results = f'{"    ".join(first_line)}\n{"    ".join(second_line)}\n{"    ".join(thrid_line)}'

        if show_results:
            results = results + f'\n{"    ".join(forth_line)}'

    return results
