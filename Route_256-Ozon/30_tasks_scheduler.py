import operator


class Proc:
    def __init__(self, energy):
        self.rate = energy
        # self.status = 'free'
        self.total_time_load = 0
        self.current_task_remaining_time = 0

    def __repr__(self):
        return str(self.rate)

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

    @property
    def total_energy_used(self):
        return (self.total_time_load + self.current_task_remaining_time) * self.rate

    # @property
    # def status(self):
    #     return 'free' if self.current_task_remaining_time == 0 else 'busy'

    def process_task(self, cnt=1):
        if self.current_task_remaining_time > cnt:
            self.total_time_load += cnt
            self.current_task_remaining_time -= cnt
        else:
            self.total_time_load += self.current_task_remaining_time
            self.current_task_remaining_time = 0


class ProcPool:
    def __init__(self, procs):
        procs.sort()  # key=operator.attrgetter('current_task_remaining_time', 'rate')
        self.processors = procs
        # self.busy_processors = []

    def __repr__(self):
        return self.processors

    def total_energy_used(self):
        res = 0
        for proc in self.processors:
            res += proc.total_energy_used
        return res

    def min_free_proc(self):
        for proc in self.processors:
            if proc.current_task_remaining_time == 0:
                # if proc not in self.busy_processors:
                #     self.busy_processors.append(proc)
                return proc
        # try:
        #     return min(proc for proc in self.processors if proc.current_task_remaining_time == 0)
        # except ValueError:
        return False

    def busy_proc_task_proc(self, cnt=1):
        for proc in self.processors:
            if proc.current_task_remaining_time > 0:
                proc.process_task(cnt)
            # if proc.current_task_remaining_time == 0:
            #     self.busy_processors.remove(proc)


proc_count, tasks_count = map(int, input().split())
processors = list(map(lambda x: Proc(int(x)), input().split()))
free_proc_pool = ProcPool(processors)
# busy_proc_pool = ProcPool()

tasks = {}
# tasks_start_times = []
for t in range(tasks_count):
    task_start, task_time = map(int, input().split())
    tasks[t] = (task_start, task_time)
    # tasks_start_times.append(task_start)

# for period in range(tasks_start_times[0], tasks_start_times[-1]+1):
#     proc_pool.busy_proc_task_proc()
#     if period in tasks.keys():
#         free_proc = proc_pool.min_free_proc()
#         if free_proc:
#             free_proc.current_task_remaining_time = tasks[period]

for i, task in tasks.items():
    if i != 0:
        free_proc_pool.busy_proc_task_proc(task[0] - tasks[i-1][0])
    free_proc = free_proc_pool.min_free_proc()
    if free_proc:
        free_proc.current_task_remaining_time = task[1]
        # if free_proc not in busy_proc_pool.processors:
        #     busy_proc_pool.processors.append(free_proc)

print(free_proc_pool.total_energy_used())
