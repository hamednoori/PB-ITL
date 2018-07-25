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
def CLUSTER_DEFINING(L_CL , TLS_List, NV_p, graph): # ClusterDefining Function
 net = sumolib.net.readNet("D:\\PATH\\Your.add.xml")
 i= 0
 j= 1
 k= 1
 
 Listj_CL = []
 value1,y = TLS_List[0]
 logging.debug("BugFoundHereErrorHappened1::::(%s)" % (value1))
# logging.debug("yyyyyyyy::::(%s)" % (y))
 TLk_CLj = value1 
 Listj_CL.append(TLk_CLj)
 last_TLS_in_list = TLS_List[-1]
 remain_TLS_List = TLS_List[TLS_List.index(TLS_List[0])+1:TLS_List.index(last_TLS_in_list)+1]
 print(len(remain_TLS_List))
 logging.debug("remain_TLS_List::::(%s)" % (remain_TLS_List))
 x,y = TLS_List_xy[value1]
 print(x)
 logging.debug("BugFoundHereErrorHappened2::::(%s)" % (x))
 logging.debug("BugFoundHereErrorHappened3::::(%s)" % (y))
 for i in range(0,len(remain_TLS_List)):
  value2,h = remain_TLS_List[i]
  logging.debug("BugFoundHereErrorHappened4::::(%s)" % (value2))
  x1,y1 = TLS_List_xy[value2]
  logging.debug("BugFoundHereErrorHappened5::::(%s)" % (x1))
  logging.debug("BugFoundHereErrorHappened6::::(%s)" % (y1))
  Dis_shortest_path = nx.dijkstra_path(graph, value1, value2,"length")
  #logging.debug("Dis_shortest_path::::(%s)" % (Dis_shortest_path))
  Distance_TLSs = dijkstra_path_length(graph, value1, value2, "length" )
  logging.debug("Distance_TLSs::::(%s)" % (Distance_TLSs))
  #Distance_TLSs = math.sqrt( ((ast.literal_eval(x)- ast.literal_eval(x1))**2)+((ast.literal_eval(y)-ast.literal_eval(y1))**2) )
  print(Distance_TLSs)
  if Distance_TLSs <= L_CL:
   logging.debug("<<<<<::::")#x,y = remain_TLS_List[i]
   TLk_CLj= value2 
   k+= 1
   i+= 1 
   
   Listj_CL.append(TLk_CLj)
  else:
   logging.debug(">>>>>>::::")
   CYCLE_DEFINING(Listj_CL, NV_p, Dis_shortest_path, graph)
   j += 1
   k= 0
   TLk_CLj= value2
   value1 = value2
   
   i+= 1
 CYCLE_DEFINING(Listj_CL, NV_p, Dis_shortest_path, graph)
    
