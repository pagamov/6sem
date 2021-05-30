
def rus(char):
    if char in "АаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфХхЦцЧчШшЩщЪъЫыЬьЭэЮюЯя":
        return True
    return False

def eng(char):
    if char in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
        return True
    return False

def other(char):
    if char in "\t\n":
        return True
    return False

def find_non_triv(word):
    for letter in word:
        if not (rus(letter) or eng(letter) or other(letter)):
            return True
    return False

def f(text):
    count = 0
    for elem in text:
        line = elem.split()
        for word in line:
            if find_non_triv(word):
                count += 1
    if count:
        return True
    return False

print(f(["Встаёт рассвет во мгле холодной", "На нивах шум работ умолк"]))
