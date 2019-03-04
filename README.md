**How people influence each other**

This is a simple beginning of a simulation that could simulate the decision finding of a group of politicans in context of a topic.

To start create a virtualenv with python 3.5.2 or higher
then do the following steps
1. pip install -r requirements.txt
2. start the main.py in BA-Analytics via python main.py
3. find the graphs in the senate-sim/graphs folder

Interpretation of the graphs
1. Person to Topic (in this case "Elbvertiefung")
- red means disagree, green agree
- the width shows the conviction of said approval / disapproval
2. Person to Person
- the blue lines show who influences who

The print out shows conviction and opinion of each politican in a connection to others.
################1###################
is the sign for a loop, in this case the second loop.
The count of loops can be changed in the main.py in the while loop.

Conviction Algorithm
1. the algorithm is written in classes/Person in the
- interact() function and
- convince() function

!Persons interact with each other every Loop if there is a connection!
