import time
def default_timer(f):
    def inner():
        start = time.time()
        f()
        end = time.time()
        ressult = end - start
        print(ressult)

    return inner

@default_timer
def some_function ():
    return sum ( range ( 100000000 ) )
    result = some_function ()
result = some_function ()

class timer(object):
    def __enter__(self):
        self.start=time.time()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end=time.time()
        time_result=self.end-self.start
        print(time_result)

with timer ():
    print ( sum ( range ( 1000 ) ) )
