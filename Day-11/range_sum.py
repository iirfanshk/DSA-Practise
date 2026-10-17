def answer_range_sum_queries(numbers, queries):
    prefix = [0]

    # Build the padded prefix-sum array.
    for num in numbers:
        prefix.append(prefix[-1] + num)

    answers = []

    for left, right in queries:
        answers.append(prefix[right+1] - prefix[left])
    return answers

numbers = list(map(int, input().split()))

q = int(input())
queries = []

for _ in range(q):
    left, right = map(int, input().split())
    queries.append((left, right))

answers = answer_range_sum_queries(numbers, queries)

for answer in answers:
    print(answer)