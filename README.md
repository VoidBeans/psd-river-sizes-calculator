River sizes are determined by counting all horizontally and vertically adjacent rivers (1s) in a matrix consisting of 0s and 1s. Diagonal rivers are not considered in the computation.

For example, the following matrix will yield river sizes `[2, 2, 10]`:

```python
[
    [1, 0, 1, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 1, 1]
]
```

The matrix member arrays are not necessarily uniform and may be provided with different lengths. E.g. the following matrix will yield river sizes `[3, 3, 5, 5, 6]`:

```python
[
    [1, 0, 1],
    [1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1],
    [1, 1],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1]
]
```
