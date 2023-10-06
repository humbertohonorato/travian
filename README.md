# travian
travian boot 

SE id="tileDetails" EXIST: VERIFICA QUAL É A CLASS

SE CLASSE FOR IGUAL A class="village": ENTÃO VERIFICA SE É UMA CAMPO VAZIA OU OCUPADA 

SE id="map_details" EXIST:
	SE table id="village_info" EXIST:
		VILA OCUPADA: 
			PEGAR VALORES E VERIFICA SE EXISTEM:
				E OBTEM OS VALORES DAS CLASSES class="titleInHeader" E class="coordinatesWrapper"
				TRIBO = <tr class="first"><th>Tribo:</th><td>Teutões</td></tr> 
				ALIANÇA= <tr><th>Aliança:</th><td class="alliance"><a href="/alliance/3">D£LTA</a></td></tr>
				PLAYER= <tr><th>Proprietário:</th><td class="player"><a href="/profile/1204">Eri-Clis</a></td></tr>
				POPULAÇÃO= <tr><th>População:</th><td>520</td></tr>
				DISTANCIA= <tr><th>Distância</th><td>7.1 Campos:</td></tr>
				
			SE TRIBO = "Natarianos":
				SAVE natars.json
			SE NAO:
				PASS
	SE NAO:
		VILA DESOCUPADA:
			PASS




--------------------------------------------------


SE id="tileDetails" EXIST, VERIFICA QUAL É A CLASS
E OBTEM OS VALORES DAS CLASSES class="titleInHeader" E class="coordinatesWrapper"

SE CLASSE FOR IGUAL A class="oasis": ENTÃO VERIFICA SE É UMA OASIS VAZIO OU OCUPADO

SE id="map_details" EXIST:
	SE table id="village_info" EXIST:
		OASIS OCUPADO:
			PASS
	SE NAO:
		OASIS LIVRE:
			PEGAR VALORES:
				SE table id="distance" EXIST:
					DISTANCIA: <tr><td class="desc">Distância</td><td class="bold">8.5 Campos:</td>
				SE table id="troop_info" EXIST:
					TROPAS: list [{<tr>
                					<td class="ico"><img class="unit u36" src="/img/x.gif" alt="Lobo"></td>
                					<td class="val">12</td>
               						<td class="desc">Lobos</td>
            						</tr>}
							]
	