# Day 4 — Lists, References, and Comprehensions

## Goals
- Understand Python list mutability and reference behavior
- Learn safe ways to copy lists
- Practice slicing, stack operations, and list comprehensions

## Work Done
- Demonstrated the reference trap and avoided it using `.copy()`
- Used slicing to extract and reverse list segments
- Simulated stack behavior using `append()` and `pop()`
- Generated derived lists using list comprehensions

## Key Learnings
- Lists are mutable objects and assignment copies references, not data
- `.copy()` or slicing creates a new list in memory
- List slicing produces shallow copies without modifying the original list
- `append()` and `pop()` enable efficient LIFO stack operations
- List comprehensions are concise, readable, and optimized at the C level