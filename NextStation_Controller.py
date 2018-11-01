from pyswip import Prolog
import requests
import json
import time


    
def getShortestPath(start, destination, time_list):
    
    prolog = Prolog()
    prolog.consult("TrainDB/location.pl")
    
    consult_data_file = getDataInTimeInterval(time_list)
    prolog.consult("TrainDB/" + consult_data_file + ".pl")
    print(consult_data_file)
    prolog.consult("astar_nextstation.pl")
    prolog.consult("TrainDB/station.pl")
    
    astar_query = "astar("+start+","+destination+ ",PATH,COST)." ## ASTAR
    shortest_path_result = list(prolog.query(astar_query))

    path_list = []
    for i in range(len(shortest_path_result[0]['PATH'])):
        path_list.append(str(shortest_path_result[0]['PATH'][i]))


    train_path_query = "trainPath("+str(path_list)+", ROW, COL, TRAIN)." ## TRAIN PATH
    train_path_result = list(prolog.query(train_path_query))

    train_path_list = []
    for i in range(len(train_path_result[0]['TRAIN'])):
        train_path_list.append(str(train_path_result[0]['TRAIN'][i]))

  
    station_info_query = "station("+str(path_list[len(path_list) -1])+", EXIT, PLACE)." ## station information 
    station_info_result = list(prolog.query(station_info_query))

    station_exit_list = []
    for i in range(len(station_info_result[0]['EXIT'])):
        station_exit_list.append(str(station_info_result[0]['EXIT'][i]))

    station_place_list = []
    for i in range(len(station_info_result[0]['PLACE'])):
        station_place_list.append(str(station_info_result[0]['PLACE'][i]))

        
    ans_list = []
    ans_list.append(path_list)
    ans_list.append(str(shortest_path_result[0]['COST']))
    ans_list.append(train_path_list)
    ans_list.append(str(train_path_result[0]['ROW']))
    ans_list.append(str(train_path_result[0]['COL']))
    ans_list.append(station_exit_list)
    ans_list.append(station_place_list)

   
        
    return ans_list

def getPlaceDetails(place_name):
    prolog = Prolog()
    prolog.consult("TrainDB/Station.pl")

    place_query = "place("+place_name+",NAME,PIC,DETAILS,ADDRESS)."
    place_result = list(prolog.query(place_query))

    ans_list = []
    ans_list.append(str(place_result[0]['NAME']))
    ans_list.append(str(place_result[0]['PIC']))
    ans_list.append(str(place_result[0]['DETAILS']))
    ans_list.append(str(place_result[0]['ADDRESS']))

    return ans_list
                

def getDataInTimeInterval(time_list):
    #day = time.strftime("%a") 
    #h, m = time.strftime("%H:%M").split(':')
    #h, m = int(h), int(m)
    file_name = getFilename(time_list[0], int(time_list[1]), int(time_list[2]))
             
    return file_name

def getFilename(day, h, m):
        file_name = ''
        if(day == 'sat' or day == 'sun'):
            if(day == 'sat' and h >= 11 and h < 21):
                file_name = 'sat_'
            elif(day == 'sun' and h >= 11 and h < 21):
                return 'sun_11_21'
            else:
                file_name = 'sat_sun_'
                
            if(h < 8):
                file_name += '6_8'
            elif(h < 9):
                file_name += '8_9'
            elif(h < 11):
                file_name += '9_11'
                
            elif(file_name == 'sat_' and h < 21):
                if (h < 15):
                    file_name += '11_15h'
                elif (h == 15 and m < 30):
                    file_name += '11_15h'
                elif (h < 19):
                    file_name += '15h_19'
                elif (h < 21):
                    file_name += '19_21'
                else:
                    return
            
            elif(h < 22):
                file_name += '21_22'
            elif(h < 24):
                file_name += '22_24'
            else:
                return
        else:
            file_name = 'mon_fri_'
            if (h < 7):
                file_name += '6_7'
                
            elif(h < 9):
                file_name += '7_9'
                
            elif(h == 9 and m < 30):
                file_name += '9_9h'
                
            elif(h < 16):
                file_name += '9h_16'
                
            elif(h == 16 and m < 30):
                file_name += '16_16h'
                
            elif(h < 17):
                file_name += '16h_17'
                
            elif(h < 19):
                file_name += '17_19h'

            elif(h < 19):
                file_name += '17_19h'

            elif(h == 19 and m < 30):
                file_name += '17_19h'

            elif(h < 20):
                file_name += '19h_20'

            elif(h < 21):
                file_name += '20_21'

            elif(h < 22):
                file_name += '21_22'

            elif(h < 24):
                file_name += '22_24'
                
            else:
                return
            
        return file_name  



