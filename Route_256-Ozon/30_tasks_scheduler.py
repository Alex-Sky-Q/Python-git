# Сервер состоит из n процессоров. Процессоры разные и достигают одинаковой скорости при разном энергопотреблении.
# А именно, i-й процессор в нагрузке тратит ai энергии за одну секунду.
# Серверу в качестве нагрузки придет m задач. Про каждую задачу известны два значения: tj и lj — момент времени, когда
# задача j придет, и время выполнения задачи в секундах.
# Вы решили реализовать планировщик, ведущий себя так: в момент tj прихода задачи выбирается свободный процессор
# с минимальным энергопотреблением и данная задача выполняется на нем все заданное время. Если к моменту прихода задачи
# свободных процессоров нет, то задача отбрасывается. Процессор, на кот. запущена задача j, будет занят ровно lj сек.,
# т.е. освободится в момент tj+lj и в этот же момент уже может быть назначен для выполнения другой задачи.
# Определите суммарное энергопотребление сервера при обработке m заданных задач (считаем, что процессоры в простое
# не потребляют энергию)
# - Входные данные
# В первой строке заданы два целых числа n и m (1≤n,m≤3⋅105) — количество процессоров и задач соответственно.
# Во второй строке заданы n целых чисел a1,a2,…,an (1≤ai≤106) — энергопотребление соответствующих процессоров
# под нагрузкой в секунду. Все энергопотребления различны.
# В след. m строках заданы описания задач: по одному в строке. В j-й строке заданы два целых числа
# tj и lj (1≤tj≤109; 1≤lj≤106) — момент прихода j-й задачи и время ее выполнения.
# Все времена прихода tj различны, и задачи заданы в порядке времени прихода.
# - Выходные данные
# Вывести единственное число — суммарное энергопотребление сервера

import heapq


class Proc:
    def __init__(self, energy):
        self.rate = energy
        # self.total_time_load = 0
        self.current_task_remaining_time = 0
        self.task_end_time = 0

    # def __repr__(self):
    #     return str(self.rate)

    def __eq__(self, other):
        return self.rate == other.rate

    def __gt__(self, other):
        return self.rate > other.rate

    def __lt__(self, other):
        return self.rate < other.rate

    def __ge__(self, other):
        return self.rate >= other.rate

    def __le__(self, other):
        return self.rate <= other.rate

    def __bool__(self):
        return True

    # @property
    # def total_energy_used(self):
    #     return (self.total_time_load + self.current_task_remaining_time) * self.rate

    # def process_task(self, cnt=1):
    #     if self.current_task_remaining_time > cnt:
    #         # self.total_time_load += cnt
    #         self.current_task_remaining_time -= cnt
    #     else:
    #         # self.total_time_load += self.current_task_remaining_time
    #         self.current_task_remaining_time = 0
    #         return True


class ProcPool:
    def __init__(self, procs):
        heapq.heapify(procs)
        self.processors = procs
        self.busy_processors = []
        heapq.heapify(self.busy_processors)

    # def __repr__(self):
    #     return self.processors

    # def total_energy_used(self):
    #     res = 0
    #     for proc in list(self.processors + self.busy_processors):
    #         res += proc.total_energy_used
    #     return res

    def min_free_proc(self, end_time):
        # if self.processors:
        self.processors[0].task_end_time = end_time
        heapq.heappush(self.busy_processors, (end_time, self.processors[0]))
        return heapq.heappop(self.processors)

    # Works, but not efficient
    # def busy_proc_task_proc(self, cnt=1):
    #     list_to_remove = []
    #
    #     # def proc_task(pr):
    #     #     if pr.process_task(cnt):
    #     #         list_to_remove.append(pr)
    #     #
    #     # with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
    #     #     executor.map(proc_task, self.busy_processors)
    #
    #     for proc in self.busy_processors:
    #         # if proc.current_task_remaining_time > 0:
    #         if proc.process_task(cnt):
    #         # if proc.current_task_remaining_time == 0:
    #             list_to_remove.append(proc)
    #     if list_to_remove:
    #         # self.processors.extend(list_to_remove)
    #         # self.busy_processors = [proc for proc in self.busy_processors if proc not in list_to_remove]
    #         for proc in list_to_remove:
    #             heapq.heappush(self.processors, proc)
    #             self.busy_processors.remove(proc)

    def check_proc(self, curr_time):
        # self.busy_processors.sort(key=operator.attrgetter('task_end_time'))
        if curr_time >= self.busy_processors[0][0]:
            while self.busy_processors:
                if curr_time >= self.busy_processors[0][0]:
                    heapq.heappush(self.processors, heapq.heappop(self.busy_processors)[1])
                else:
                    break


proc_count, tasks_count = map(int, input().split())
processors = list(map(lambda x: Proc(int(x)), input().split()))
proc_pool = ProcPool(processors)
energy_sum = 0

for i in range(tasks_count):
    task_start, task_time = map(int, input().split())
# for period in range(tasks_start_times[0], tasks_start_times[-1]+1):
#     previous_task_start = task_start
#     proc_pool.busy_proc_task_proc(task_start - previous_task_start)
#     if period in tasks.keys():
#         free_proc = proc_pool.min_free_proc()
    if i != 0 and proc_pool.busy_processors:
        proc_pool.check_proc(task_start)
    if proc_pool.processors:
        free_proc = proc_pool.min_free_proc(task_start + task_time)
        # if free_proc:
        free_proc.current_task_remaining_time = task_time
        energy_sum += task_time * free_proc.rate

# print(proc_pool.total_energy_used())
print(energy_sum)
