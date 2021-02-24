#!python3
# -*- coding: utf-8 -*-

# multiprocessing
from multiprocessing import Pool, Process
from multiprocessing import Value   # memory shared variable
from multiprocessing import Queue   # safe queues
from multiprocessing import Lock
from queue import Empty # for catching empty errors

# coloring
from color import color

# configuration
# from data import step as SIEVE_STEP
SIEVE_STEP = 40000

from time import time
import decimal,copy
from Primes import Primes
from Matrix_solver import Matrix_solver
from lib import GCD,Q,smooth_region,eratosthenes

n = 104729 * 103591
B = 10**5

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
        return [idx * SIEVE_STEP, (idx + 1) * SIEVE_STEP]
    else:
        return [- (idx) * SIEVE_STEP, - (idx - 1) * SIEVE_STEP]


# максимальное количество процессов
MAX_PROCESSES = 4
# номер региона на котором нужно остановится
REGION_IDX_MAX = 200

def worker_task(current_idx, lock, answer_queue, primes, q, idx):
    """what every worker does"""
    # проверить пустоту можно только ловлей ошибок
    # если проверять с помощью if, тогда в промежутке между if и выполнением
    # другого кода, другой процесс может взять элемент
    while True:
        lock.acquire()  # block lock
        region_idx         = current_idx.value
        current_idx.value += 1
        lock.release()  # unblock lock

        if region_idx >= REGION_IDX_MAX:
            break   # exit if we reached maximum
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
    # модифицирование кол-ва гладких чисел только для одного процесса
    region_idx_lock = Lock()
    # отслеживаем кол-во гладких чисел (queue.qsize() не гарантирует точности)
    smooth_numbers_qty = Value('i', 0)
    for _ in range(MAX_PROCESSES):
        workers.append(Process(
            target=worker_task,
            args=(smooth_numbers_qty, region_idx_lock, answer_queue, primes, q, _)
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

    while not answer_queue.empty():
        answer = answer_queue.get()
        print(f"Get answer: {answer}")
    print(f"smooth numbers qty: {smooth_numbers_qty.value}")
