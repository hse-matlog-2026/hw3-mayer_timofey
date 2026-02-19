# This file is part of the materials accompanying the book
# "Mathematical Logic through Python" by Gonczarowski and Nisan,
# Cambridge University Press. Book site: www.LogicThruPython.org
# (c) Yannai A. Gonczarowski and Noam Nisan, 2017-2022
# File name: propositions/operators.py

"""Syntactic conversion of propositional formulas to use only specific sets of
operators."""

from propositions.syntax import *
from propositions.semantics import *

def to_not_and_or(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'``, ``'&'``, and ``'|'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'``, ``'&'``, and
        ``'|'``.
    """
    substitution_map = {
    'T': Formula.parse('(p|~p)'),
    'F': Formula.parse('(p&~p)'),
    '->': Formula.parse('(~p|q)'),
    '+': Formula.parse('((p&~q)|(~p&q))'),
    '<->': Formula.parse('((p&q)|(~p&~q))'),
    '-&': Formula.parse('~(p&q)'),
    '-|': Formula.parse('~(p|q)')
    }
    return formula.substitute_operators(substitution_map)
    # Task 3.5

def to_not_and(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'~'`` and ``'&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'~'`` and ``'&'``.
    """
    form = to_not_and_or(formula) 
    return form.substitute_operators({'|': Formula.parse('~(~p&~q)')})
    # Task 3.6a

def to_nand(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'-&'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'-&'``.
    """
    form = to_not_and_or(formula)

    substitution_map = {
        '~': Formula.parse('(p-&p)'),
        '&': Formula.parse('((p-&q)-&(p-&q))'),
        '|': Formula.parse('((p-&p)-&(q-&q))')
    }
    
    return form.substitute_operators(substitution_map)
    # Task 3.6b

def to_implies_not(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'~'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'~'``.
    """
    # Task 3.6c
    
    form = to_not_and_or(formula)
    
    p = Formula('p')
    q = Formula('q')
    
    not_q = Formula('~', q)
    implies_p_not_q = Formula('->', p, not_q)
    not_implies = Formula('~', implies_p_not_q)
    
    not_p = Formula('~', p)
    implies_not_p_q = Formula('->', not_p, q)
    
    substitution_map = {
        '&': not_implies,
        '|': implies_not_p_q
    }
    
    return form.substitute_operators(substitution_map)
    # Task 3.6c

def to_implies_false(formula: Formula) -> Formula:
    """Syntactically converts the given formula to an equivalent formula that
    contains no constants or operators beyond ``'->'`` and ``'F'``.

    Parameters:
        formula: formula to convert.

    Returns:
        A formula that has the same truth table as the given formula, but
        contains no constants or operators beyond ``'->'`` and ``'F'``.
    """
    form = to_implies_not(formula)

    p = Formula('p')
    f = Formula('F')  
    implies_p_f = Formula('->', p, f)
    
    substitution_map = {
        '~': implies_p_f
    }
    
    return form.substitute_operators(substitution_map)
    # Task 3.6d
