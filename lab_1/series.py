import matplotlib.pyplot as plt
from collections import defaultdict


def nth_term(n):
    return 24 / (7 * n ** 2 + 56 * n + 105)


partial_sums = {}
errors = {}
n_digits = defaultdict(int)
true_sum = 1.0

for N in (10 ** m for m in range(5)):
    current_sum = 0.0
    for k in range(N):
        current_sum += nth_term(k)
    partial_sums[N] = current_sum
    errors[N] = true_sum - current_sum
    i = -1
    while i < 30:
        if errors[N] <= 10 ** (-i):
            n_digits[N] += 1
            i += 1
        else:
            break
    print(f'Sum, Error, Number of digits for n = {N}')
    print(partial_sums[N], errors[N], n_digits[N])

N_keys = list(map(str, partial_sums.keys()))
errors = list(errors.values())
n_digits = list(n_digits.values())

error_bars = plt.barh(N_keys, errors, label='Погрешность')
plt.bar_label(error_bars, padding=8, fontsize=9)
plt.xlim(0, 5)
plt.legend()
plt.savefig('plots/series_error.png', dpi=300)
plt.close()

digits_bars = plt.barh(N_keys, n_digits, label='Количество значащих цифр')
plt.bar_label(digits_bars, padding=8, fontsize=9)
plt.xlim(0, 6)
plt.legend()
plt.savefig('plots/series_digits.png', dpi=300)




