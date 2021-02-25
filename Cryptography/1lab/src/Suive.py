# -*- coding: utf-8 -*-
from data import Smooth_search, Smooth_file, Smooth_save
from data import n, B, step
from data import Smooth_search_parallel
from color import color
from lib import smooth_region

# for multiprocessing
import multiprocessing as mp
from lib import get_region
# indicate workers to stop
from ctypes import c_bool
# settings for multiprocessing
from data import Parallel_max_processes as MAX_PROCESSES

def worker_task(region_idx, stop_working, answer_queue, primes, q):
    while True:
        # process safe read and write operation
        with region_idx.get_lock():
            local_region_idx  = region_idx.value
            region_idx.value += 1

        # exit if we reached maximum
        if stop_working.value:
            break
        region = get_region(local_region_idx, step)
        # calculate answer
        answer = smooth_region(*region, q, primes)
        # return it
        answer_queue.put(answer)

def suive(q, primes):
    if Smooth_search_parallel:
        mp.set_start_method('spawn')
        # mp.set_start_method("spawn", force=True)
        MAX_SMOOTH_QTY = len(primes)
        print("MAX_SMOOTH_QTY:", MAX_SMOOTH_QTY)
        # инициализируем lock-safe очередь для ответов
        answer_queue = mp.Queue()
        # создаем работающие процессы
        workers = []
        # индекс региона
        region_idx = mp.Value('i', 0)
        # нужно ли останавливаться воркерам
        stop_workers = mp.Value(c_bool, False)
        # инициализируем процессы
        for worker_id in range(MAX_PROCESSES):
            workers.append(mp.Process(
                target=worker_task,
                args=(region_idx, stop_workers, answer_queue, primes, q)
            ))
        for worker in workers:
            worker.start()
        # читаем из очереди ответов в нашу локальную переменную
        smooth_numbers = []
        while len(smooth_numbers) < MAX_SMOOTH_QTY:
            smooth_numbers.extend(answer_queue.get())
            print("\nfound:",color(len(smooth_numbers),'data')+"/"+color(len(primes),'data'),color(round(float(len(smooth_numbers))/float(len(primes))*100,2),"%")+"\n")
        # говорим воркерам закончить
        stop_workers.value = True
        # ждем пока они закончат
        for idx, worker in enumerate(workers):
            worker.kill()
        return smooth_numbers
    elif Smooth_search:
        # Smooth_search == True so we need to find our smooth numbers
        print("step:",color(step,"data"))
        k = 1
        # found_smooth = 0
        smooth_numbers = []
        while q((k-1)*step) < n:
            ans = smooth_region((k-1)*step,k*step,q,primes)
            for i in range(len(ans)):
                smooth_numbers.append(ans[i])
            ans = smooth_region(-k*step,-(k-1)*step,q,primes)
            for i in range(len(ans)):
                smooth_numbers.append(ans[i])
            k+=1
            print("Total number of smooth numbers:",color(len(smooth_numbers),'data'))
            if len(smooth_numbers) > len(primes):
                # Выброс из функции
                if Smooth_save:
                    # we need to save our smooth numbers in file Smooth_file
                    t = time()
                    data = [B, n, smooth_numbers]
                    with open(Smooth_file, 'wb') as f:
                        pickle.dump(data, f)
                    print("\nsmooth numbers saved in time: "+color(round(time() - t,4),"time"),"in file: "+str(Smooth_file))
                return smooth_numbers
    else:
        # Smooth_search == False so we need to upload factor base from Smooth_file
        t = time()
        data = []
        smooth_numbers = []
        with open(Smooth_file, 'rb') as f:
            data = pickle.load(f)
        if data[0] != B:
            print(color("Suive::Error: wrong B!","strong"))
            exit()
        if data[1] != n:
            print(color("Suive::Error: wrong n!","strong"))
            exit()
        smooth_numbers = data[2]
        print(color("smooth upload in time:","strong")+color(round(time() - t,4),"time"),"from file: "+str(Smooth_file))
        print("smooth len",color(len(smooth_numbers),"data"))
        return smooth_numbers
