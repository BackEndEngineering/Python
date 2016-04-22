    PEP8 is a style guide for Python code.
Consistency on having a style is very important.
The importants on having your code legiable,
to have readability, for others to maintain and for others
to upgrade and evolves, so your code can prosper.
Having your Python code consistency style within one module to
have the ability to function is the most important.

    One example should a line break before or after a binary
operator. The readability is the most importants from confusing
a programmer especially a new comer to programming. Take a look
at operators at the bottom. The first example of the operators are
scattered readability make it problem to solve if the program has
conflicts.

Example 1:
# No: operators sit far away from their operands
income = (gross_wages +
          taxable_interest +
          (dividends - qualified_dividends) -
          ira_deduction -
          student_loan_interest)

    Now take a look at the second example 2 of the operators.
The operators on the left-side are lineup makes the readability
more access in problem solving. The parenthese and underscores
are on the right-side of the operators. By reducing the conflicts
of over estimating how many operators.

Example 2:

# Yes: easy to match operators with operands
income = (gross_wages
          + taxable_interest
          + (dividends - qualified_dividends)
          - ira_deduction
          - student_loan_interest)

    Other things to keep in mind Imports should be
on separate lines and is always on top of the
file.

Yes: import os
     import sys

No:  import sys, os

Imports should be grouped together in the
following order.

1. standard library imports
2. related third party imports
3. local application/library specific imports

    This make the Import more readable to understand and
tend to be better behaved in group. For further understanding
on Imports and anything else pretaining to the Style Guide for Python
Code. And especially if you new to programming.
You can read PEP8: https://www.python.org/dev/peps/pep-0008/

    The imports of readability to coding. Tim Peters made
20 software principles that influences the design of Python
Programming Language called The Zen of Python that been
written on PEP20 https://www.python.org/dev/peps/pep-0020/

The Zen of Python
    Beautiful is better than ugly.
    Explicit is better than implicit.
    Simple is better than complex.
    Complex is better than complicated.
    Flat is better than nested.
    Sparse is better than dense.
    Readability counts.
    Special cases aren't special enough to break the rules.
    Although practicality beats purity.
    Errors should never pass silently.
    Unless explicitly silenced.
    In the face of ambiguity, refuse the temptation to guess.
    There should be one-- and preferably only one --obvious way to do it.
    Although that way may not be obvious at first unless you're Dutch.
    Now is better than never.
    Although never is often better than *right* now.
    If the implementation is hard to explain, it's a bad idea.
    If the implementation is easy to explain, it may be a good idea.
    Namespaces are one honking great idea -- let's do more of those!
