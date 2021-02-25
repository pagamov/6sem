if __name__ == "__main__":
    from Factor import Factor
    from time import time
    import numpy as np
    from data import n, B
    from color import color

    print("B "+color(B,"data"))
    t = time()

    res = Factor(n,B)

    print("\nans:",color(int(res[0]),"strong")+" "+color(int(res[1]),"strong"))
    print("time:",color(round(time() - t,4),"time"))
