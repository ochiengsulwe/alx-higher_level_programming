#!/usr/bin/python3

# a function to list number of arguments in a function

def no_arg(*args)
    return(len(args), argv)
        if no_arg() == 0:
	    print("{} arguments.".format(len(args)))
        elif no_arg() == 1:
            print("{} argument: {}".format(len(args), argv))
        else:
            print("{} arguments:".format(len(args))
            for argv in range(len(args)):
                print("{} : {}".format(len(args), argv))
