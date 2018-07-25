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

# We need to import Python modules from the $SUMO_HOME/tools directory
if 'SUMO_HOME' in os.environ:
    tools = os.path.join(os.environ['SUMO_HOME'], 'tools')
    sys.path.append(tools)
else:
    sys.exit("Environment variable SUMO_HOME not defined")
    
import traci

class UnusedPortLock:
    lock = thread.allocate_lock()

    def __init__(self):
        self.acquired = False

    def __enter__(self):
        self.acquire()

    def __exit__(self):
        self.release()

    def acquire(self):
        if not self.acquired:
            UnusedPortLock.lock.acquire()
            self.acquired = True

    def release(self):
        if self.acquired:
            UnusedPortLock.lock.release()
            self.acquired = False


 
def main():
    # Option handling
    parser = OptionParser()
    parser.add_option("-c", "--command", dest="command", default="sumo", help="The command used to run SUMO [default: %default]", metavar="COMMAND")
    parser.add_option("-s", "--scenario", dest="scenario", default="london.sumo.cfg", help="A SUMO configuration file [default: %default]", metavar="FILE")
    parser.add_option("-n", "--network", dest="network", default="london.net.xml", help="A SUMO network definition file [default: %default]", metavar="FILE")    
    parser.add_option("-b", "--begin", dest="begin", type="int", default=800, action="store", help="The simulation time (s) at which the re-routing begins [default: %default]", metavar="BEGIN")
    parser.add_option("-e", "--end", dest="end", type="int", default=72000, action="store", help="The simulation time (s) at which the re-routing ends [default: %default]", metavar="END")
    parser.add_option("-i", "--interval", dest="interval", type="int", default=300, action="store", help="The interval (s) at which vehicles are re-routed [default: %default]", metavar="INTERVAL")
    parser.add_option("-o", "--output", dest="output", default="noori1.xml", help="The XML file at which the output must be written [default: %default]", metavar="FILE")
    #parser.add_option("-a", "--additional-files", dest="additional", default="london.add.xml", help="Generate edge-based dump instead of ""lane-based dump. This is the default.", metavar="FILE")
    parser.add_option("-l", "--logfile", dest="logfile", default=os.path.join(tempfile.gettempdir(), "sumo-noori.log"), help="log messages to logfile [default: %default]", metavar="FILE")
    (options, args) = parser.parse_args()
    
    logging.basicConfig(filename=options.logfile, level=logging.DEBUG)
    logging.debug("Logging to %s" % options.logfile)
    
    if args:
        logging.warning("Superfluous command line arguments: \"%s\"" % " ".join(args))
        
    start_simulation(options.command, options.scenario, options.network, options.begin, options.end, options.interval, options.output)
    
if __name__ == "__main__":
    main()    
    
 
