# import operator
# import collections
# import concurrent
# from concurrent import futures
import heapq


class Proc:
    def __init__(self, energy):
        self.rate = energy
        # self.status = 'free'
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

    # @property
    # def status(self):
    #     return 'free' if self.current_task_remaining_time == 0 else 'busy'

    def process_task(self, cnt=1):
        if self.current_task_remaining_time > cnt:
            # self.total_time_load += cnt
            self.current_task_remaining_time -= cnt
        else:
            # self.total_time_load += self.current_task_remaining_time
            self.current_task_remaining_time = 0
            return True


class ProcPool:
    def __init__(self, procs):
        # procs.sort()  # key=operator.attrgetter('current_task_remaining_time', 'rate')
        heapq.heapify(procs)
        self.processors = procs
        # self.free_procs_num = len(self.processors)
        self.busy_processors = []
        heapq.heapify(self.busy_processors)

    # def __repr__(self):
    #     return self.processors

    # def total_energy_used(self):
    #     res = 0
    #     for proc in list(self.processors + self.busy_processors):
    #         res += proc.total_energy_used
    #     return res
        # res = 0
        # for proc in range(len(self.processors)):
        #     res += proc.total_energy_used
        # return res

    # @property
    # def busy_procs(self):
    #     return [proc for proc in self.processors if proc.current_task_remaining_time > 0]

    # @property
    # def free_procs(self):
    #     return [proc for proc in self.processors if proc.current_task_remaining_time == 0]

    def min_free_proc(self, end_time):
        # if self.processors:
        # self.processors.sort()
        # for proc in self.processors:
            # if proc.current_task_remaining_time == 0:
                # self.free_procs_num -= 1
                # if proc not in self.busy_processors:
        self.processors[0].task_end_time = end_time
        # self.busy_processors.append((end_time, self.processors[0]))
        heapq.heappush(self.busy_processors, (end_time, self.processors[0]))
        return heapq.heappop(self.processors)
        # try:
        #     return min(proc for proc in self.processors if proc.current_task_remaining_time == 0)
        # except ValueError:
        # return False

    def busy_proc_task_proc(self, cnt=1):
        list_to_remove = []

        # def proc_task(pr):
        #     if pr.process_task(cnt):
        #         list_to_remove.append(pr)
        #
        # with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        #     executor.map(proc_task, self.busy_processors)

        for proc in self.busy_processors:
            # if proc.current_task_remaining_time > 0:
            if proc.process_task(cnt):
                # self.free_procs_num += 1
        # if proc.current_task_remaining_time == 0:
                list_to_remove.append(proc)
        if list_to_remove:
            # self.processors.extend(list_to_remove)
            # self.busy_processors = [proc for proc in self.busy_processors if proc not in list_to_remove]
            for proc in list_to_remove:
                heapq.heappush(self.processors, proc)
                self.busy_processors.remove(proc)

    def check_proc(self, curr_time):
        # self.busy_processors.sort(key=operator.attrgetter('task_end_time'))  # key=operator.attrgetter('rate', 'task_end_time')
        # free_procs = [proc for proc in self.busy_processors if curr_time >= proc.task_end_time]
        # free_proc = next(free_procs)
        if curr_time >= self.busy_processors[0][0]:
            # for proc in self.busy_processors:
            # if curr_time >= min(end_times):
            # if free_procs:
                # free_procs.sort()
            while self.busy_processors:
                if curr_time >= self.busy_processors[0][0]:
                    # heapq.heappush(self.processors, self.busy_processors[0][0])
                    heapq.heappush(self.processors, heapq.heappop(self.busy_processors)[1])
                    # self.busy_processors.remove(proc)
                    # break
                else:
                    break
            # proc = min(sorted(self.busy_processors))
            # heapq.heappush(self.processors, proc)
            # self.busy_processors.remove(proc)


proc_count, tasks_count = map(int, input().split())
processors = list(map(lambda x: Proc(int(x)), input().split()))
free_proc_pool = ProcPool(processors)
# busy_proc_pool = ProcPool()

# tasks = {}
# tasks_start_times = []
previous_task_start = 0
sum = 0
for i in range(tasks_count):
    task_start, task_time = map(int, input().split())
    # tasks[i] = (task_start, task_time)
    # tasks_start_times.append(task_start)
# for period in range(tasks_start_times[0], tasks_start_times[-1]+1):
#     proc_pool.busy_proc_task_proc()
#     if period in tasks.keys():
#         free_proc = proc_pool.min_free_proc()
#         if free_proc:
#             free_proc.current_task_remaining_time = tasks[period]

# for i, task in tasks.items():
    if i != 0 and free_proc_pool.busy_processors:
        # free_proc_pool.busy_proc_task_proc(task_start - previous_task_start)
        free_proc_pool.check_proc(task_start)
    previous_task_start = task_start
    if free_proc_pool.processors:
        free_proc = free_proc_pool.min_free_proc(task_start + task_time)
        # if free_proc:
        free_proc.current_task_remaining_time = task_time
        # free_proc.task_end_time = task_start + task_time
        sum += task_time * free_proc.rate
        # if free_proc not in busy_proc_pool.processors:
        #     busy_proc_pool.processors.append(free_proc)

# print(free_proc_pool.total_energy_used())
print(sum)
