# 
#
#
# ------------------------------------------------------------------------------------------------------------------------------
#
# This program have been developed by Hamed Noori and with citiation of the related publicaitons
# can be used without permission.
# This program is for a novel architecture for traffic light control system which can form and manipulate 
# vehicular platoons using clusters of traffic lights. This method, called Platoon-Based Intelligent Traffic Lights (PB-ITL) 
# is based on coordinated traffic lights that are connected and are also able to communicate with vehicles wirelessly. PB-ITL 
# groups traffic lights in clusters and each cluster tries to provide proper green status for the platoon of vehicles, using the
# Platooning concept which is seeking to utilize close to full capacity of roads. 
# This lib is a Python-based program which can simulate a city with dynamic intelligent traffic lights. 
# The author can be reach at noori@ece.ubc.ca
#
# ------------------------------------------------------------------------------------------------------------------------------
#
#





from __future__ import division

import os
import ast
import sys
import subprocess
import signal
import socket
import logging
import thread
import time
import tempfile
import math
import random
import networkx as nx
from collections import defaultdict, deque
from math import log
import sumolib
from k_shortest_paths import k_shortest_paths
from optparse import OptionParser
from bs4 import BeautifulSoup
from collections import defaultdict
#import simpla
from decimal import Decimal
from collections import deque
from heapq import heappush, heappop
from itertools import count
import networkx as nx
import xml.etree.ElementTree as ET
from networkx.utils import generate_unique_node
junction_dictionary ={}
TLS_List_xy={} 
TLS_List = []
junction_id =[]
lane_length = {}
lane_ITT = {}
lane_CTT = {}
lane_id=[]
avgLengthall=0
avgSpeedall=0
dict_edgeRSUs={}
dict_lane={}
laneallgraph=[]
edgeallgraph=[]
edgeallsgraph=[]
visit_bfs=[]
dict_fc={}
list_source={}
list_present_network=[]
list_vehicle_set_route=[]
number_of_lane={}
TMax=0
footprintList =[]
dict_footprint ={}


def build_road_graph():                
    logging.debug("build_road_graph0")   
    f = open("D:\\E\\d\\sumo-0.32.0\\bin\\london.net.xml", 'r')
    net = sumolib.net.readNet("D:\\E\\d\\sumo-0.32.0\\bin\\london.net.xml")
    data = f.read()
    soup = BeautifulSoup(data)
    f.close()
    sys.stdout = open('RSU.txt','wt')
    edges_length={}
    edges_speed = {}
    edge_from ={}
    edge_to ={} 
    graphlane = nx.DiGraph() 
    
    for edge_tag in soup.findAll("edge"):
	 edge_id = edge_tag["id"]
	 lane_tag = edge_tag.find("lane")
	 edges_length[edge_id] = int(float(lane_tag["length"]))
	 edges_speed[edge_id] = int(float(lane_tag["speed"]))
	 edge_from[edge_id] =  net.getEdge(edge_id).getFromNode().getID()
	 edge_to[edge_id] =  net.getEdge(edge_id).getToNode().getID()
	 lane_tag = edge_tag.findAll("lane")
	 for lane_t in lane_tag:
	   lane_id = lane_t["id"]
	   graphlane.add_edge(edge_from[edge_id].encode("ascii"), edge_to[edge_id].encode("ascii"), length= edges_length[edge_id], Edge = edge_id.encode("ascii"), speed = edges_speed[edge_id], Lane = lane_id.encode("ascii"), weight=0)
	   print("edge_from= {0}    edge_to= {1}   speed= {2} length= {3}  Edge={4}   Lane={5} weight= 0 " .format(edge_from[edge_id].encode("ascii"), edge_to[edge_id].encode("ascii"), edges_speed[edge_id], edges_length[edge_id] , edge_id.encode("ascii"), lane_id.encode("ascii")))

    return graphlane
