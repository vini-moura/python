import time
C = 400
G = 150
I = 150
X = 50
M = 60

def eco_aberta(function):
    def wrapper():
        return function()+ X-M
    print(wrapper())

@eco_aberta
def pib():
    y = C + G + I
    return y

# -----------------------------

def delay_decorator(function):
    def wrapper():
        time.sleep(2)
        function()
    print(wrapper)

@delay_decorator
def say_hello():
    return "hello"

@delay_decorator
def say_bye():
    return "bye"