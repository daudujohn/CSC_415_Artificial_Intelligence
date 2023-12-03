import networkx as nx
import matplotlib.pyplot as plt

"""Assume there is a special make-up exam for 300L students
from two programs (Computer Science and Mechanical
Engineering) in your school (just for a day).
▪ The following are the courses to be taken:
▪ CSC310, TMC311, EDS311, MCE318, GEC310, CSC315
▪ Convert this problem into a graph colouring problem (GCP)
and draw the constraints graph.
▪ Assume all the courses carry the same number of units (1)
▪ Which means they will have the same amount (1 hour) of required timeslots during
the exam.
▪ Assume there are four timeslots available
▪ 8 am - 9 am (Colour Red)
▪ 9 am - 10 am (Colour Green)
▪ 11 am - 12 noon (Colour Blue)
▪ 2 pm - 3 pm (Colour Black)
▪ Solve the problem using backtracking and interpret the solution in normal
timetabling format.
"""