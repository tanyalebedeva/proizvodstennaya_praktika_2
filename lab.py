import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data_final = [
    2479, 3613, 2120, 788, 4222, 1310, 1777, 1528, 4428, 865,
    3859, 3888, 1704, 786, 2152, 2890, 2997, 1680, 1951, 2618,
    4755, 3979, 2196, 566, 544, 5107, 2922, 2984, 3371, 5158,
    4112, 876, 1673, 940, 2143, 1274, 987
]

hist_freqs, hist_bins = np.histogram(data_final, bins='auto')

for i in range(len(hist_freqs)):
    print(f"Интервал: {round(hist_bins[i], 1)} – {round(hist_bins[i+1], 1)}, Частота: {hist_freqs[i]}")


plt.hist(data_final, bins='auto', edgecolor='black')
plt.title("Гистограмма частот времени восстановления")
plt.xlabel("Время восстановления (мин)")
plt.ylabel("Частота")
plt.grid(True)
plt.show()
