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


def find_unused_port():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    sock.bind(('127.0.0.1', 0))
    sock.listen(socket.SOMAXCONN)
    ipaddr, port = sock.getsockname()
    sock.close()
    
    return port
#"--device.hbefa.probability", "1.0",