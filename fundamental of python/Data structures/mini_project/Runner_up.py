def find_runner_up(scores):
   
    unique_scores = set(scores)

    unique_scores.remove(max(unique_scores))
    
    return max(unique_scores)

input= [2, 3, 6, 6, 5]
runner_up = find_runner_up(input)
print(f"Runner-up score: {runner_up}")