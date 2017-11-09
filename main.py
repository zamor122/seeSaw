import threading
import time
# A variable that contains some data
iteration = 0
fredHeight = 1
wilmaHeight = 7
fredVelocity = 1
wilmaVelocity = 1.5
# A semaphore to indicate that an item is available
increase = threading.Semaphore(1)
decrease = threading.Semaphore(0)
#going up function
def goingUp():
    global iteration
    global fredHeight
    global wilmaHeight
    global fredVelocity
    global wilmaVelocity
    for i in range(10):
        while fredHeight < 7:
            increase.acquire()
            fredHeight += fredVelocity
            print "Fred is going up, height is: ", fredHeight
            time.sleep(1)
            decrease.release()
        while wilmaHeight < 7:
            increase.acquire()
            wilmaHeight += wilmaVelocity
            print "Wilma is going up, height is: ", wilmaHeight
            time.sleep(1)
            decrease.release()
#going down function
def goingDown():
    global iteration
    global fredHeight
    global wilmaHeight
    global fredVelocity
    global wilmaVelocity
    for i in range(10):
        while wilmaHeight > 1:
            decrease.acquire()
            wilmaHeight -= fredVelocity
            print "Wilma is going down, height is: ", wilmaHeight, "\n"
            time.sleep(1)
            increase.release()
        while fredHeight > 1:
            decrease.acquire()
            fredHeight -= wilmaVelocity
            print "Fred is going down, height is: ", fredHeight, "\n"
            time.sleep(1)
            increase.release()
if __name__ == '__main__':
    t1 = threading.Thread(target=goingUp)
    t1.start()
    t2 = threading.Thread(target=goingDown)
    t2.start()
    t1.join()
    t2.join()