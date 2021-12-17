import pexpect
import sys


def traceroute(URL):

    commandStr = 'traceroute -w 1 -q 1 -I ' + URL   #Linux / Unix traceroute command
    child = pexpect.spawn(commandStr)               #Creates a child traceroute process

    hopCount = 0
    while 1:                        #runs until process finishes
        line = child.readline()     #reads each line of stout
        if not line: break          #break if reached the end
        hopCount += 1               #increment

    return hopCount                     #total num of hops