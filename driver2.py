from file1 import fun1, fun2
import file2

def start():
    fun1()
    fun2()
    file2.fun3() #Note fun3 was not explicitely called in the pre-amble

start()