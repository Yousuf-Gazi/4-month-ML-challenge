# Day 5 — Dictionaries and Key-Based Data Handling

## Goals

- Learn safe dictionary access patterns
- Understand how to handle missing keys gracefully
- Practice real-world dictionary use cases

## Work Done

- Accessed dictionary values safely using `.get()` with and without default values
- Built a character frequency map using a dictionary accumulator pattern
- Merged dictionaries using the pipe (`|`) operator
- Merged dictionaries using `.copy()` and `.update()`

## Key Learnings

- `.get()` prevents runtime errors when keys are missing
- Default values provide safe fallbacks for optional data
- Dictionaries are ideal for counting and aggregation tasks
- The pipe operator (`|`) creates a new merged dictionary without mutating inputs
- `.update()` mutates the target dictionary in place
