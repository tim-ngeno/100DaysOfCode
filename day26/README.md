# List Comprehensions and Dictionary Comprehensions in Python

## What are List Comprehensions?

List comprehensions are a concise way to create lists in Python. They are similar to for loops, but they are more concise and easier to read.

The syntax for a list comprehension is:

```python
[expression for item in iterable]
```

Where `expression` is the expression that is evaluated for each item in the iterable, and `iterable` is the object that is being looped over.

For example, the following code creates a list of the squares of the numbers from 1 to 5:

```python
numbers = [1, 2, 3, 4, 5]
squares = [number ** 2 for number in numbers]

print(squares)
```

This code will print the following output:

```
[1, 4, 9, 16, 25]
```


## What are Dictionary Comprehensions?

Dictionary comprehensions are a concise way to create dictionaries in Python. They are similar to list comprehensions, but they create dictionaries instead of lists.

- The syntax for a dictionary comprehension is:

```python
{key: expression for item in iterable}
```

Where `key` is the key for the dictionary, `expression` is the expression that is evaluated for each item in the iterable, and `iterable` is the object that is being looped over.

For example, the following code creates a dictionary that maps each number from 1 to 5 to its square:

```python
numbers = [1, 2, 3, 4, 5]
squares = {number: number ** 2 for number in numbers}

print(squares)
```

This code will print the following output:

```
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
```

## Examples

Here are some more examples of list comprehensions and dictionary comprehensions:

* Create a list of the even numbers from 1 to 10:

```python
even_numbers = [number for number in range(11) if number % 2 == 0]
```

* Create a dictionary that maps each letter of the alphabet to its corresponding ASCII value:

```python
letters = {letter: ord(letter) for letter in "abcdefghijklmnopqrstuvwxyz"}
```

* Create a list of all the possible pairs of numbers from 1 to 5:

```python
pairs = [(x, y) for x in range(1, 6) for y in range(1, 6)]
```

---
