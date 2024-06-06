import random
import matplotlib.pyplot as plt

random.seed(30)
N = 1000000

sum_counts = {i: 0 for i in range(2, 13)}

for _ in range(N):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice_sum = dice1 + dice2
    sum_counts[dice_sum] += 1

probabilities = {
    sum_: count / N for sum_,
    count in sum_counts.items()
}

print("Sum | Probability")
print("-------------------")
for sum_, prob in probabilities.items():
    print(f"{sum_} | {prob*100:.3f}%")