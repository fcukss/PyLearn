import numpy as np

pulse_data = np.array([72, 75, 80, 120, 68, 110, 70])

print(np.mean(pulse_data))  # average value
print(pulse_data.max())
print(pulse_data[pulse_data > 100])  # это булева маска (самая крутая фишка NumPy), показатели >100

print('____________________________')
heart_rate = [70, 72, 75, 150, 71, 73, 160, 72]  # 150 и 160 — это явно "шум" или артефакты движения

rate = np.array(heart_rate)

print(rate.min())
print(np.std(rate))
# найти скользящее среднее по 3 элементам без циклов, представь, что ты накладываешь массив сам на себя со сдвигом:
moving_avg = (rate[:-2] + rate[1:-1] + rate[2:]) / 3  # vectorization
print(moving_avg)
# find median это не среднее враифметическое, а как фильтр откидывает явно некорректные значения
print(np.median(rate))  # игнорирует экстремальные значения

print('____________________________')

patients = np.array([
    [36.6, 72, 120],  # patient #0
    [39.0, 110, 140],  # patient #1 he is ill
    [36.8, 80, 115]  # patien# 2
])
print(patients.T)  # Транспонирование матрицы(поворот матрицы)
print(np.mean(patients, axis=0)) #среднее значение по столбцам
print(patients[:,1])   #[ 72. 110.  80.] возращает столбец

adjustment = np.array([0.5, 0, 0])
fixed_patients = patients + adjustment #увеличил весь столбик на 0.5
print(fixed_patients)  #[[ 37.1  72.  120. ]
                        #[ 39.5 110.  140. ]
                        #[ 37.3  80.  115. ]]

print(patients*2)  #умножает все эдементы матрицы на 2

