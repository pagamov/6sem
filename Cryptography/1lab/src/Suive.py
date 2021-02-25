# -*- coding: utf-8 -*-
from data import Smooth_search, Smooth_file, Smooth_save
from data import n, B, step
from color import color
from lib import smooth_region

def suive(q, primes):
    if Smooth_search:
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
