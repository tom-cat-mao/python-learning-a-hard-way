def print_multi_argvs(*argvs):
    argv1, argv2, argv3 = argvs;
    print("argv1:", argv1)
    print("argv2:", argv2)
    print("argv3:", argv3)
    
print_multi_argvs("Hello", "world", "Python")