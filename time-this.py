#Задание со звездочкой


import time
class Timer:
    # Определяем класс
    # Пишем конструктор класса
    def __init__(self, num_runs = 1):
        self.num_runs = num_runs
        # Конструктор принимает аргумент num_runs - количество запусков функции при замере
        # Конструктор  
    def __call__(self, func):
        # декоратор
        def wrapper(*args, **kwargs):
            total = 0
            for i in range(self.num_runs):
                start = time.time()
                return_value = func(*args, **kwargs)
                end = time.time()
                total = total + (end-start)
            print('Программа запущена ', num_runs, 'раз')
            print('Среднее время выполнения: {} секунд.'.format(total/self.num_runs))
            return return_value
        return wrapper 

num_runs = int(input('Сколько раз запустить программу? Выберите что-то до миллиона, а то состаритесь пока ждёте;) '))        
# Создаём объект класса
timer_10 = Timer(num_runs)



# Используем объект, как декоратор
@timer_10
def f():
    for i in range(10000):
        pass
# Вызываем функцию
f()