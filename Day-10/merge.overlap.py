def merge_overlapping_intervals(intervals):
    ordered = sorted(intervals, key=lambda interval: interval[0])
    merged = []

    # Add the first interval to merged.
    merged.append([ordered[0][0], ordered[0][1]])

    # Process every remaining interval.
    # Merge when the current start is not greater than the last end.
    # Otherwise, add a new interval.
    for index in range(1, len(ordered)):
        start, end = ordered[index]
        last = merged[-1]

        if start <= last[1]:
            if end > last[1]:
                last[1] = end
        else:
            merged.append([start, end])

    return merged


n = int(input())
intervals = []

for _ in range(n):
    start, end = map(int, input().split())
    intervals.append([start, end])

answer = merge_overlapping_intervals(intervals)

for start, end in answer:
    print(start, end)