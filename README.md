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

![Uploading unnamed.jpg…]()
