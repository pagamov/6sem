#!python3
# -*- coding: utf-8 -*-

# multiprocessing
from multiprocessing import Process
from multiprocessing import Value   # memory shared variable
from multiprocessing import Queue   # safe queues

# coloring
from color import color

# configuration
from data import step, B, n

from time import time
import decimal,copy
from Primes import Primes
from Matrix_solver import Matrix_solver
from lib import GCD,Q,smooth_region,eratosthenes

q = Q(n)
primes = Primes(n,B,q)

def get_region(idx):
    """
    return unique region for specified index
    if index is even: return positive
                 odd: return negative
    """
    # четные: положительный знак, нечетные: отрицательный
    sign = (idx % 2) * (-1)
    if sign == 0:
        return [idx * step, (idx + 1) * step]
    else:
        return [- (idx) * step, - (idx - 1) * step]


# максимальное количество процессов
MAX_PROCESSES = 4
# номер региона на котором нужно остановится
REGION_IDX_MAX = 20

# TODO: pass lambda condition to exit
def worker_task(current_idx, answer_queue, primes, q):
    """
    what every worker does

    current_idx:  multiprocessing.Value of type "i" (integer).
        Used to identify region
    answer_queue: multiprocessing.Queue
        Used to return answer from worker. You should read whole queue before
        calling worker.join()
    primes:       Primes class
    q:            Q class
    """
    while True:
        # process safe read and write operation
        with current_idx.get_lock():
            region_idx         = current_idx.value
            current_idx.value += 1

        # exit if we reached maximum
        if region_idx >= REGION_IDX_MAX:
            break
        region = get_region(region_idx)
        # calculate answer
        answer = smooth_region(*region, q, primes)
        # return it
        answer_queue.put(answer)



reg = [get_region(idx) for idx in range(REGION_IDX_MAX)]
print(f"{reg}")

if __name__ == '__main__':
    print("Запускаем классическим методом")
    t = time()
    for r in reg:
        smooth_region(r[0],r[1],q,primes)
    t1 = time()
    print("\ntime:", str(round(t1 - t, 2)))

    print("\n\nnow run workers")
    # инициализируем lock-safe очередь для ответов
    answer_queue = Queue()
    # создаем работающие процессы
    workers = []
    # отслеживаем кол-во гладких чисел (queue.qsize() не гарантирует точности)
    region_idx = Value('i', 0)
    for worker_id in range(MAX_PROCESSES):
        workers.append(Process(
            target=worker_task,
            args=(region_idx, answer_queue, primes, q)
        ))
    t = time()
    # запускаем их
    for worker in workers:
        worker.start()
    answers = []
    while len(answers) < REGION_IDX_MAX:
        answers.append(answer_queue.get())
    # ждем пока они закончат
    for idx, worker in enumerate(workers):
        print(f"waiting for {idx} process")
        worker.join()
        print(f"joined {idx} process")
    t1 = time()
    print("Get answer from workers in time: {}".format(str(round(t1 - t, 2))))

    for answer in answers:
        print("Get answer: {}".format(answer))
    print(f"smooth numbers qty: {region_idx.value}")
