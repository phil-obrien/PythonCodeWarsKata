import sys
from collections import deque

"""
The aligning of the dominos to create a valid train can be done in the following way (example using n=4, so max pips=4)

Take all dominos that have a zero pip on them and line them up in a valid train (note the left digit is left pip and right is right pip!):
00 01 10 02 20 03 30 04 40

Then the 1's (taking care not to include any dominos already used): 11 12 21 13 31 14 41

Then the 2's, 3's and 4's, so overall we have:

00 01 10 02 20 03 30 04 40   ("Control Pip" is 0) (We'll call this "Train 0" later)
11 12 21 13 31 14 41         ("Control Pip" is 1)
22 23 32 24 42               ...etc...
33 34 43
44

1. Note how each train begins with the (only) "double" domino.
2. After that we take the "next-smallest-number" (eg 12 when Control Pip is 1)...
3. ...reverse it (21), then go to step 2 for the next biggest number until we place 14 (max pips=4) and its reverse, 41

Next we want to merge these trains together. "Train 0" has a "join" (where pips of different dominos touch) of "1" in between dominos 01 and 10.
In fact, every "Train N" has a join of value "N+1" between its 2nd and 3rd dominos (except the last train (44) obviously). We can use this to
visualise how all the trains can merge into one long valid train:

00 01                                                 10 02 20 03 30 04 40 
      11 12                            21 13 31 14 41
            22 23             32 24 42
                  33 34    43
                        44
                        
Giving (dashes separate the Trains):
00 01-11 12-22 23-33 34-44-43-32 24 42-21 13 31 14 41-10 02 20 03 30 04 40

The value to be returned by the function is a list of numbers representing the joins between the pips, capped at each end by the outermost values.
So we need to return:
0 0  1  1  2  2  3  3  4  4  3  2  4  2  1  3  1  4  1  0  2  0  3  0  4 0

Upon observation, we can see that these single digits (join values) are basically just the left pip from each domino, plus the right pip from the last domino!

So now we need an algorithm!

The algorithm solves the puzzle as follows:

1. We start off by calling the process_pip function for Control Pip == 0
2. Append 0 to the list of touching_pips (note that on first call to the process_pip function the left pip of the left domino isn't touching, but is appended anyway for "outer cap"!)
3. Check "if 0 == n" to see if Control Pip (0) reached max number for n. (N=4 so we have not)
4. Append the Control Pip value again (0). This represents the "join" between dominos 00 and 01
5. The process_pip function will now call itself passing "Control Pip + 1" (0+1=1) as the parameter. This will be expanded on later (see step 9).

Ignoring the function calling itself for now, the rest of the function completes the Control Pip (0) processing as follows:

6. Append "Control Pip + 1" (0+1=1) to touching_pips list. This represents the "join" between dominos 01 and 10 (note: actually represents join between 41 and 10 due to recursive function calls)
7. Loop through all values from "Control Pip + 2" to 4 (use n+1 cos of Python!)...
   7a. Append Control Pip (0) to touching_pips list. This represents the "join" between dominos 10 and 02
   7b. Append 2 to touching_pips list. This represents the "join" between dominos 20 and 0x (where x is next value in loop)
8. So (forgetting that we called the process_pip function recursively) when the loop for Control Pip (0) finishes we have: 0 0 1 0 2 0 3 0 4

9. After the second value has been added for any Control Pip, the process_pip function is recursively called to process the first two dominos of the next Control Pip.
   9a. The only exception to this is for the last Control Pip, for which the function returns as soon as it has processed the first and only domino (44 in this case)
   9b. For all Control Pips less than n (ie Train 0 to Train n-1) is added to as follows:
       9b1. Append Control Pip (1) to touching_pips list. This represents the "join" between dominos 01 and 11.
       9b2. Append Control Pip (1) to touching_pips list. This represents the "join" between dominos 11 and 12.
       9b3. Append Control Pip (2) to touching_pips list. This represents the "join" between dominos 12 and 22.
       9b4. Append Control Pip (2) to touching_pips list. This represents the "join" between dominos 22 and 23.
       ...etc...
       
10. Once all recursive calls have been completed, we return to the initial calling code in function domino_train and append a 0 to touching_pips list for rightmost pip of rightmost domino (40)

Order of execution is thus:
1) Append to touching_pips list for first part of Train 0
2) Append to touching_pips list for first part of Train 1
3) Append to touching_pips list for first part of Train 2
4) Append to touching_pips list for first part of Train 3
-
5) Append to touching_pips list for ONLY part of Train 4
-
6) Append to touching_pips list for second part of Train 3
7) Append to touching_pips list for second part of Train 2
8) Append to touching_pips list for second part of Train 1
9) Append to touching_pips list for second part of Train 0
-
10) Append a 0 for the rightmost cap
"""

sys.setrecursionlimit(2000) # default Python limit on recursion is 999. This is too small (1474 was the highest "n" seen during testing), so extend it!

###################################
def process_pip(ctrl_pip): # this function will be called recursively
###################################

    touching_pips.append(ctrl_pip)  # Append the Control Pip value to get things moving for this Control Pip

    if  ctrl_pip == n:              # Have we reached our max value of "n"? This means we are processing the domino with pip values n&n
        return                      # Return to the previous recursive function if so

    touching_pips.append(ctrl_pip)  # Append the Control Pip value again

    ###################################
    process_pip(ctrl_pip+1) # RECURSIVE Function Call here (function calls itself and when it returns "from itself" it will carry on from here)
    ###################################
    
    touching_pips.append(ctrl_pip + 1) # from here on we're dealing with the second part of each "Train" (see notes in intro for details)

    for i in range(ctrl_pip+2,n+1):

        touching_pips.append(ctrl_pip)
        touching_pips.append(i)

    return # return from the iterative func either to previous "version" of recursive func or to calling code in domino_train
    
###################################
def domino_train(n_param):
###################################

    global n
    n = n_param
    
    global touching_pips
    touching_pips = deque([])
        
    process_pip(0)
    touching_pips.append(0)     # append a zero to represent the rightmost outer cap (rightmost pip of rightmost domino)
    return(list(touching_pips)) # convert the deque to a list and return it
    
