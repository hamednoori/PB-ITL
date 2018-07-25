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
def run(network, begin, end, interval): 
    
    logging.debug("Start run") 
    graph = build_road_graph()
    step = 1
    travel_time_cycle_begin = interval
    net = sumolib.net.readNet("D:\\PATH\\Your.net.xml")
    f = open("D:\\PATH\\Your.net.xml", 'r')
    data = f.read()
    f.close()
    soup = BeautifulSoup(data)
    L_CL = 2500 # 2500 m is equal to 2.5 km for cluster length
    NV_p = 16 #Desired No. of Vehicles in each Platoon   #simpla.load("simpla.cfg")
    
    for junction_tag in soup.findAll("junction"): #All TLs and locations (from SUMO)
	 junction_type = junction_tag["type"]
	 if junction_type == "traffic_light":
	   junction_id.append(junction_tag["id"])
	   logging.debug("junction_id::::(%s)" % (junction_id))
	   junction_x = junction_tag["x"]
	   junction_y = junction_tag["y"]
	   junction_dictionary[junction_tag["id"]] = (junction_x, junction_y)
	   
	   TLS_List_xy[junction_tag["id"]]=( junction_x, junction_y )
	   
	   
    TLS_List_sort = sorted(TLS_List_xy.iteritems(), key=lambda (k,v): (v,k))
    
    logging.debug("sorted::::(%s)" % (TLS_List_sort))
	
    CLUSTER_DEFINING(L_CL , TLS_List_sort, NV_p, graph) #CLUSTERDEFINING(TLSList)
    lane_id.append(traci.lane.getIDList())
     for edg_tag in soup.findAll("edge"):
	   edge_id = edg_tag["id"]
	   if edge_id.startswith(":"): continue
	   edge = net.getEdge(edge_id)
	   lane_id.append(edge.getLanes())

    while  step == 1 or traci.simulation.getMinExpectedNumber() > 0:     
        traci.simulationStep()	 
        if step >= travel_time_cycle_begin and travel_time_cycle_begin <= end and step%interval == 0:
            #net.removePrograms()
            for l  in traci.lane.getIDList():
             Related_TLs_Lane_list = []
             vmax = traci.lane.getMaxSpeed(l)
             lenght_lane = traci.lane.getLength(l)
             vmean = traci.lane.getLastStepMeanSpeed(l)
             lane_ITT[l] = lenght_lane / vmax # londonculate ideal traveling time (ITT)
             if vmean !=0: #londonculate current traveling time (CTT)
			  lane_CTT[l] = lenght_lane / vmean 
             else:
			  lane_CTT[l]= lenght_lane / vmax  
             
             if lane_CTT[l] >= (1.3 * lane_ITT[l]):
			 
			  for j in graph.nodes_iter():
			   for successor_j in graph.successors_iter(j):
			     if l == graph.edge[j][successor_j]["Lane"]:
				  if j in junction_id: #finding an item in a list
				    Related_TLs_Lane_list.append((j, junction_dictionary[j]) )
				  if successor_j in junction_id:
				    Related_TLs_Lane_list.append((successor_j, junction_dictionary[successor_j]))
				   #logging.debug("edge.getTLS().getID()::::(%s)" % (edge.getTLS().getID()))
			  logging.debug("Related_TLs_Lane_list::::(%s)" % (Related_TLs_Lane_list))
			  
			  if len(Related_TLs_Lane_list) > 1:
			   CLUSTER_DEFINING(L_CL , Related_TLs_Lane_list, NV_p, graph)
			  #print(lane_id)
			  
				   
                
		     
            #rerouting_step += interval
            travel_time_cycle_begin = step + 1
        step += 1 
         
   
    time.sleep(10)
    logging.debug("Simulation finished")
    traci.close()
    sys.stdout.flush()
    time.sleep(10)
 
