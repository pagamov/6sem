class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def color(data,col):
    """
    data: object which will be colored
    col:  string representing color. possible values are:
        ['data', '%', 'time', 'strong']
    """
    if col == "data":
        # pink
        return bcolors.HEADER+str(data)+bcolors.ENDC
    elif col == "%":
        # green
        return bcolors.OKGREEN+str(data)+bcolors.ENDC+" %"
    elif col == "time":
        # light blue
        return bcolors.OKCYAN+str(data)+bcolors.ENDC+" sec"
    elif col == "strong":
        # red
        return bcolors.FAIL+str(data)+bcolors.ENDC
