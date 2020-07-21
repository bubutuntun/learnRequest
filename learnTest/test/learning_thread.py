import time
import threading


class MyThread(threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.counter = counter
        self.name = name
        self.threadID = threadID

    def run(self):
        print("开始线程：" + self.name)
        moyu_time(self.name, self.counter, 10)
        print("退出线程：" + self.name)

    pass


def moyu_time(name, delay, count):
    while count:
        time.sleep(delay)
        print("%s 开始摸鱼%s" % (name, time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())))
        count -= 1
    pass


thread1 = MyThread(1, "小明", 1)
thread2 = MyThread(2, "小红", 2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
