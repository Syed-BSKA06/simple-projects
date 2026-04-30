import statistics

# Sample dataset: daily steps count
steps = [5234, 6789, 4321, 9876, 1234, 8765, 6543, 3456, 7890, 5678]

def analyze_steps(data):
    total = sum(data)
    avg = total / len(data)
    median = statistics.median(data)
    max_steps = max(data)
    min_steps = min(data)

    above_avg = [x for x in data if x > avg]

    print("---- Step Analysis ----")
    print(f"Total Steps: {total}")
    print(f"Average Steps: {round(avg, 2)}")
    print(f"Median Steps: {median}")
    print(f"Max Steps: {max_steps}")
    print(f"Min Steps: {min_steps}")
    print(f"Days above average: {len(above_avg)}")

    return {
        "total": total,
        "average": avg,
        "median": median,
        "max": max_steps,
        "min": min_steps
    }

# Run analysis
result = analyze_steps(steps)

# Simple insight
if result["average"] > 6000:
    print("Good activity level!")
else:
    print("Try to walk more!")