# CYB-2013 Project — Stable Matching Algorithm Variants

> This project is part of the University of Tulsa’s **CYB-2013: Secure Software Development 2** course.  

---

## Objective

The goal of this project was to implement two variants of the Gale–Shapley stable matching algorithm in Python, building on concepts of the Stable Marriage Problem in algorithm design.

Both variants extend the standard stable matching procedure to handle additional real-world complexities:
- Forbidden Matches: Certain pairs are not allowed to be matched.
- Tied Preferences: Participants may be indifferent between multiple options, creating preference ties.

The implementation was verified using GitHub Classroom autograding and unit testing.

---

## Project Overview

### Implemented Functions

| Function | Description |
| -------- | ------------ |
| `gs()` | Standard Gale–Shapley algorithm implementation. |
| `gs_block()` | Modified algorithm that excludes forbidden match pairs from being considered. |
| `gs_tie()` | Modified algorithm that supports indifference/ties in preference orderings. |

Each function returns a **dictionary of stable matches** mapping women to their matched partners.

---

## Example Usage

```python
themen = ['xavier','yancey','zeus']
thewomen = ['amy','bertha','clare']

thepref = {
    'xavier': ['amy','bertha','clare'],
    'yancey': ['bertha','amy','clare'],
    'zeus': ['amy','bertha','clare'],
    'amy': ['yancey','xavier','zeus'],
    'bertha': ['xavier','yancey','zeus'],
    'clare': ['xavier','yancey','zeus']
}

blocked = {('xavier','clare'),('zeus','clare'),('zeus','amy')}
match_block = gs_block(themen, thewomen, thepref, blocked)
print(match_block)
# Output: {'amy': 'xavier', 'bertha': 'yancey'}
