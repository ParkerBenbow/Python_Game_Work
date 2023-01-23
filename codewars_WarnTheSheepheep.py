def warn_the_sheep(queue):
    x = 0
    if queue[-1] == "wolf":
        return "Pls go away and stop eating my sheep"
    elif "wolf" in queue:
        x = queue.index("wolf")
        a = (len(queue) - x) - 1
        return "Oi! Sheep number " + str(a) + "! You are about to be eaten by a wolf!"

"""
cleaner

def warn_the_sheep(queue):    
    queue.reverse()
    wolfnum = queue.index("wolf")
    if wolfnum == 0:
        return "Pls go away and stop eating my sheep"
    else:
        return "Oi! Sheep number {0}! You are about to be eaten by a wolf!".format(wolfnum)
"""