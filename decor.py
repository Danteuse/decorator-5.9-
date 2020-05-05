import time
#определяем декоратор для работы с параметром количества циклов
def time_this(NUM_RUNS):
	#определяем функцию-обертку
	def time_this_level_one(func):
		#определяем функцию, производящую вычисление времени (функцию-таймер)
		def time_this_level_two():
			#счетчик времени
			avg_time = 0
			#расчет времени в зависимости от количества циклов
			for _ in range(NUM_RUNS):
				t0 = time.time()
				#в это место помещаем функцию, которую хотим обернуть
				func()
				t1 = time.time()
				avg_time += (t1 - t0)
			avg_time /= NUM_RUNS
			print("Выполнение заняло %.5f секунд" % avg_time)
		return time_this_level_two
	return time_this_level_one
#в переменной декоратора time-this() указываем количество циклов подсчета времени выполнения
@time_this(NUM_RUNS=30)
def f():
	for j in range(1000000):
		pass
#вызываем функцию
f()