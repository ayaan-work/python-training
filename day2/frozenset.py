#A frozenset is an immutable set.
fs = frozenset([1,2,3])

print(fs)

# fs.add(4)

d = {
    frozenset({1,2}): "numbers"  # only immutable objects can be used as keys in a dictionary, so we can use frozenset as a key in a dictionary
}

print(d)


# When to use
# Immutable collections of unique items
# Dictionary keys that represent a set
# Nested sets
# Read-only permissions