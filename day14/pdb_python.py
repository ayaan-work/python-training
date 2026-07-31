#in-built debugger in python
def calculate_total(items):
    total = 0
    for item in items:
        breakpoint()  # Execution pauses here
        total += item["price"] * item["quantity"]
    return total


items=[
    {"price":10,"quantity":2},
    {"price":20,"quantity":4}
]
result=calculate_total(items)
print(result)

