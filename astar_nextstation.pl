%===================================================================
% Station
%===================================================================
stationList([phaya_thai_airlink,ratchaprarop,makkasan,ramkhamhaeng,hua_mak,ban_thap_chang,latkrabang,suvarnabhumi,mo_chit,saphan_kwai,ari,sanam_pao,victory_monument,phaya_thai,ratchathewi,siam,chit_lom,ploen_chit,nana,asok,phrom_phong,thong_lo,ekkamai,phra_khanong,on_nut,bang_chak,punnawithi,udom_suk,bang_na,bearing,samrong,national_stadium,siam_silom_line,ratchadamri,sala_daeng,chong_nonsi,surasak,saphan_taksin,krung_thon_buri,wongwian_yai,pho_nimit,talat_phlu,wutthakat,bang_wa,hua_lamphong,sam_yan,si_lom,lumphini,klong_toei,queen_sirkit_national_covention_center,sukhumvit,phetchaburi,phra_ram_9,thailand_cultural_center,huai_kwang,sutthisan,ratchadaphisek,lat_phrao,phahon_yothin,chatuchak_park,kamphaen_phet,bang_sue,tao_poon,khlong_bang_phai,talad_bang_yai,sam_yaek_bang_yai,bang_phlu,bang_rak_yai,bang_rak_noi_tha_it,sai_ma,phra_nang_klao_bridge,yaek_nonthaburi1,bang_krasor,nonthaburi_civic_center,ministry_of_public_health,yaek_tiwanon,wong_sawang,bang_son,tao_poon_purple]).				

%===================================================================





%=====================================================================================================================================
%  A STAR
%=====================================================================================================================================
distance(X,Y,Z) :- dist(X,Y,Z).
distance(X,Y,Z) :- dist(Y,X,Z).




astar(Start, Destination, Path, Cost) :- getHn(Start,Destination,Hn),
				   	 search(Destination,[[Start,[Start],Hn]],[_,Path,Cost]).

search(Station, [[Station,Path,TotalCost]|T], [Station,Path,TotalCost]) :- !.
search(Destination, [[Station,Path,TotalCost]|T], Result) :- expand([Station,Path,TotalCost],Destination,ExpandedNode),
							     append(T, ExpandedNode, NewQ),
							     minsort(NewQ, PriorityQ),
							 

							     %write("\n\nQUEUE: "),write(NewQ),
							     %write("\nMIN SORT: "),write(PriorityQ),write("\n")
			
							     search(Destination,PriorityQ, Result).



expand([Station,Path,_], Destination, Return) :- findall(X, distance(Station,X,_),NextStations),
				   		 checkPassedNode(NextStations, Path, [], NewNextStations),
				    		 createNode(NewNextStations, Destination, Path, [], Return).


checkPassedNode([],Path,NewStations, NewStations).
checkPassedNode([Station|T], Path, NewStations, Return) :- in(Station, Path) -> checkPassedNode(T, Path, NewStations, Return);
									     	 append(NewStations,[Station],NNewStation),
				   					      	 checkPassedNode(T, Path, NNewStation, Return).

in(Station, [PassedStation|Path]) :- Station == PassedStation -> !;in(Station,Path).

createNode([], Destination, Path, Nodes, Nodes).
createNode([Station|T], Destination,Path,Nodes, ExpandedNodes) :- append(Path, [Station], NewPath), 
					                          append(Nodes, [[Station, NewPath, 0]], NewNodes),
					      	 		  createNode(T, Destination, Path, NewNodes, Result),
					    			  %write("RESULT: "),write(Result),write("\n"),
					     			  getFn(Result, Destination, [], ExpandedNodes).

getFn([], Destination, Nodes, Nodes).
getFn([[Station, [FromPath|ToPath], TotalCost]|T], Destination, Nodes, Return) :- getGn(ToPath,FromPath, 0, Gn),
								    	 	  getHn(Station,Destination,Hn), Fn is Gn + Hn,
										  %write("FN: "),write(Fn),
                                                        	    		  append(Nodes, [[Station, [FromPath|ToPath], Fn]], NewNodes),
								     		  getFn(T, Destination, NewNodes, Return).

getGn([], From, Acc, Acc).
getGn([To|T], From, Acc, Gn) :-	distance(From,To,StepCost),!, NewAcc is Acc + StepCost, 
				getGn(T, To, NewAcc, Gn).


power(X,Result) :- Result is X * X.
getHn(Start, Destination, HeuristicValue) :- location(_,Start,X1,Y1), location(_,Destination,X2,Y2),
					     generateDistance(X1,Y1,X2,Y2,Distance),
					     HeuristicValue is Distance/106.666667. %max deltaV train 

generateDistance(X1, Y1, X2, Y2, ReturnV2) :- R is 6371e3, % metres
					      LatRadian1 is X1*pi/180,
    					      LatRadian2 is X2*pi/180,
    					      DifLat is (X2 - X1)*pi/180,
  					      DifLon is (Y2 - Y1)*pi/180,
    					      A1 is sin(DifLat/2) * sin(DifLat/2),
    					      A2 is cos(LatRadian1) * cos(LatRadian2),
    					      A3 is sin(DifLon/2) * sin(DifLon/2),
    				    	      A is A1 + A2 * A3,
    					      C is 2 * atan2(sqrt(A), sqrt(1-A)),
    					      D is R*C,
      					      ReturnV2 is D / 1000.


minsort(List, Return) :- setof([TotalCost,Station,Cost], member([Station,Cost,TotalCost], List), Result),
			 findall([Cost,TotalCost,Station], member([Station,Cost,TotalCost],Result),Return).

%=====================================================================================================================================


%=====================================================================================================================================
% Which Train
%=====================================================================================================================================
trainPath([Station|Path], Col, Row, Result) :- location(Train, Station, _, _),
				     whichTrain(Path, [Train], TrainList),
				     includeWalk(TrainList, Row, Col, Result). % confusion between width and row = ="
				     

whichTrain([], TrainList, TrainList).
whichTrain([Station|Path], TrainList, Result) :- location(Train, Station, _, _),
						 append(TrainList, [Train], NewTrainList),
				 		 whichTrain(Path, NewTrainList, Result).

includeWalk(Lst, Row, Col, Return) :- checkWalk(Lst,[],0, 1, Row, Col, Return).

checkWalk([], Return, AccR, AccC, AccR, AccC, Return).
checkWalk([H|T], Result, AccR, AccC, Row, Col, Return) :- isDifferent(H,T) -> append(Result, [walk], X), NewAccC is AccC + 1,checkWalk(T, X, AccR, NewAccC, Row, Col, Return)
                                                       		  ;append(Result, [H],X), NewAccR is AccR + 1, checkWalk(T, X, NewAccR, AccC, Row, Col, Return).

isDifferent(X,[Y|T]) :- X \= Y,!.



%=====================================================================================================================================


%=====================================================================================================================================
% Get Closest Train Station
%=====================================================================================================================================
findClosestStation(X1, Y1, Result) :- stationList(Stations),findMinDistance(Stations, X1, Y1, [9999,a], Result).

findMinDistance([], X1, Y1, [Distance|Station], [Station,Distance]).
findMinDistance([HStation|TStation], X1, Y1, [Distance|Station], Result) :- location(_,HStation,X2,Y2),
									    generateDistance(X1,Y1,X2,Y2, NewDistance),
									    NewDistance =< Distance -> 
									    findMinDistance(TStation, X1, Y1, [NewDistance| HStation], Result);
									    findMinDistance(TStation, X1, Y1, [Distance|Station],Result).
%=====================================================================================================================================
