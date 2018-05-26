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




def CYCLE_DEFINING(Listj_CL, NV_p, Dis_shortest_path, graph):
 net = sumolib.net.readNet("D:\\PATH\\Your.net.xml")
 
 i= 0
 #Tpass = 4.5
 #Total_ASL = 50
 Ofset_dic ={}
 GrPh_List_j_CL = {}
 ITT_tl = 0
 tlid  = Listj_CL[i]
 tlid = c[0]
 Ofset_dic[Listj_CL[i]] = 0
 logging.debug("tlidtlidtlid::::(%s)" % (tlid))
 programID = traci.trafficlights.getProgram(tlid)
 net.removePrograms()
 programID = traci.trafficlights.getProgram(tlid)
 logging.debug("programIDprogramID::::(%s)" % (programID))
 net.addTLSProgram(tlid, '1', 0, "static") #actuated
 tree = ET.parse('D:\\PATH\\Your.add.xml')
 root = tree.getroot()
 print(root.tag)
 for tlLogic_tag in root:
 
  if tlid == tlLogic_tag.get('id'):
   tlLogic_tag.set('offset', "0")
   tlLogic_tag.set('programID', "1")
  tree.write("D:\\PATH\\Your.add.xml")
  # # tlLogic_tag.set(name, '5')
  # name = tlLogic_tag.get('id')
  # print(name)
  
 #tree.close() 
 for i in range(0,len(Listj_CL)-1):	
  CyST_List_j_CL[i] = Listj_CL[i]
  
  for tlid in c:
  logging.debug("Listj_CL[i]::::(%s)" % (c))
  Dis_shortest_pathh = []
  Dis_shortest_pathh= nx.dijkstra_path(graph, Listj_CL[i], Listj_CL[i+1],"length")
  logging.debug("Dis_shortest_pathh::::(%s)" % (Dis_shortest_pathh))
   x = Dis_shortest_pathh
   #logging.debug("x::::(%s)" % (x))
   j= 0
   for j in range(0,len(x)-1):
     logging.debug("x[j]x[j]::::(%s)" % (x[j]))
     logging.debug("x[j+1]x[j+1]::::(%s)" % (x[j+1]))
     speed = graph.edge[x[j]][x[j+1]]["speed"]
     lentgh = graph.edge[x[j]][x[j+1]]["length"]
     ITT_tl += (lentgh  / speed )
     j+=1
   logging.debug("ITT_tlITT_tlITT_tl::::(%s)" % (ITT_tl))
  for j in graph.nodes_iter():
   for successor_j in graph.successors_iter(j):
    if j in Dis_shortest_pathh and successor_j in Dis_shortest_pathh:
	  #logging.debug("Dis_shortest_path::::(%s)" % (Dis_shortest_path))
	  logging.debug("BugFoundedHere::::(%s)" % (j))
	  logging.debug("successor_j::::(%s)" % (successor_j))
	  speed = graph.edge[j][successor_j]["speed"]
	  lentgh = graph.edge[j][successor_j]["length"]
	  ITT_tl += (lentgh / speed )
	  
  logging.debug("ITT_tlITT_tlITT_tl::::(%s)" % (ITT_tl))#CyST_List_j_CL[i + 1] = CyST_List_j_CL[i] + ITT_tl 
  tlid2 = Listj_CL[i+1]
  logging.debug("tlid2tlid2tlid2tlid2::::(%s)" % (tlid2))
  ofset = Ofset_dic[Listj_CL[i]] + ITT_tl 
  Ofset_dic[Listj_CL[i+1]] = ofset
  logging.debug("ofsetofsetofset::::(%s)" % (ofset))
  #programID = traci.trafficlights.getProgram(tlid2)
  
  currentprogram = net.addTLSProgram(tlid2, '1', ofset, "static")
  tree = ET.parse('D:\\PATH\\Your.add.xml')
  root = tree.getroot()
  print(root.tag)
  for tlLogic_tag in root:
 
   if tlid2 == tlLogic_tag.get('id'):
    tlLogic_tag.set('offset', str(ofset))
    tlLogic_tag.set('programID', "1")
	
   tlLogic_tag.attrib['id']= "5"
   # tlLogic_tag.set(name, '5')
   name = tlLogic_tag.get('id')
   print(name)
  
  tree.write("D:\\PATH\\Your.add.xml") 
  
  i +=1
  #tree.close()#GrPh_List_j_CL[i] = NV_p / Tpass
