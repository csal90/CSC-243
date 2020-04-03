def pig(s):
    front = ""
    i = 0
    if s[0] in "AaEeIiOoUu":
        return s + 'way'

    for c in s:
        if c in ('a', 'e', 'i', 'o', 'u'):
            end = str(s[i:])
            break
        else:
            front += c
        i = i + 1
    return str(end) + front + "ay"


def findOppositeDigits(str):
    if len(str) < 2:
        return ''
    else:
        if int(str[0]) + int(str[1]) == 10:
            return str[:2]
        else:
            return findOppositeDigits(str[1:])


class Car:
    def __init__(self, engineOn=False, speed=0):
        self.engineOn = engineOn
        self.speed = speed

    def start(self):
        self.engineOn = True

    def stop(self):
        self.engineOn = False

    def accelerate(self):
        if self.engineOn is True:
            self.speed += 20
        if self.speed >= 100:
            pass

    def brake(self):
        if self.engineOn is True:
            self.speed -= 20
        if self.speed <= 0:
            pass

    def __repr__(self):
        return 'Engine: {} Speed: {}'.format(self.engineOn, self.speed)

def checkEmtpy(html):
    def handle_starttag(self, startTag, attrs):
        if str(startTag) == "ul":
            self.counter = self.counter + 1
        if self.counter not in self.dict.keys():
            self.dict[self.counter] = []
        if startTag == "li":
            self.flag = True

    def handle_data(self, data):
        if self.flag:
            self.dict[self.counter].append(data)