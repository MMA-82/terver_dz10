# Провести дисперсионный анализ для определения того, есть ли различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.
# Даны значения роста в трех группах случайно выбранных спортсменов:
# Футболисты: 173, 175, 180, 178, 177, 185, 183, 182.
# Хоккеисты: 177, 179, 180, 188, 177, 172, 171, 184, 180.
# Штангисты: 172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170.

import numpy as np
import scipy.stats as stats

fb = np.array([173, 175, 180, 178, 177, 185, 183, 182])
hc = np.array([177, 179, 180, 188, 177, 172, 171, 184, 180])
wl = np.array([172, 173, 169, 177, 166, 180, 178, 177, 172, 166, 170]) 

k = 3
n = 28
# H0: M_fb = M_hc = M_wl
alpha = 0.05

# Применяем критерий Фишера

print(stats.f_oneway(fb, hc, wl))
# Вывод: p-value = 0.01 < alpha = 0.05, следовательно занятия разными видами спорта оказывает влияние на рост взрослых спортсменов.
# Нулевая гипотеза отвергается, есть различия среднего роста среди взрослых футболистов, хоккеистов и штангистов.


