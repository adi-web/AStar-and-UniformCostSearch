## Progetto IA
# Run main.py :
**Output Astar and Uniform cost Search**:
- nodi esaminati durante il processo per trovare il path migliore
- numero di nodi esaminati
- output path trovato

 # Inserimento nuovi poligoni:
 Per inserire un nuovo poligono si deve inserire una lista di vertici in main.py  
 - esempio:  triangolo=[(5,6),(5,11),(10,8)] e fare pol.append(triangolo) per inserirlo nella lista dei poligoni

 # Inserimento start e goal diversi 
- graph_create.find_intersection(pol,( start_vertex), -1) e pol.append(sart_vertex) in main.py
- per il vertice goal fare graph_create.find_intersection(pol,goal_vertex, -1) in main.py
  
# Esempio di prova: 
![esempio](https://mail.google.com/mail/u/0?ui=2&ik=7fda07b09c&attid=0.1&permmsgid=msg-a:r7577954504465250976&th=1919a269a5aa9e16&view=fimg&fur=ip&sz=s0-l75-ft&attbid=ANGjdJ-snFUv5NxLVVBg1AtoaRYvwtqgVNyZXRP9oongbUIjUKW7b9Mk6Kv0twrTy-NMDTs8fkvBMSHvXHBuXAirS9vLh4-fRNvYuV3Di4n9olY8K9NoIdUXWqVQJ0Y&disp=emb&realattid=7A27C3F5-B387-498C-A686-FE0FC1735FAA$0)
