def color(data,col):
    if col == "data":
        # pink
        return "\033[95m"+str(data)+"\033[0m"
    elif col == "%":
        # green
        return "\033[92m"+str(data)+"\033[0m %"
    elif col == "time":
        # light blue
        return "\033[96m"+str(data)+"\033[0m sec"
    elif col == "strong":
        # red
        return "\033[91m"+str(data)+"\033[0m"
