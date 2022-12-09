#TP2; and calculeouvert(tab[0])!=True;   else:
       # res=True 

#ALSO; flag thingy was kind of hardcoded; need to fix that if got time

#CHERCHER LES !!!!!!!!!!!!!!!!!!! dans le code pour les points importants

#A faire :
#1. SHIFTKEY pour les flags
#2. RECURSION
#3. NbRangees et NbColonnes >=10
#4. BETTER COMMENTS AND VARIABLE NAMES
#5. TESTS UNITAIRES


#DECLAS
#grille pour noter tous les coups

#grilleBombe pour l'emplacement des bombes (meme format que grilleBombe)

#placeBombeListeUnique; liste avec emplacement exactement uniquement (check 
#if can erase grilleBombe and use just that and check for inverse as well =
#reduce data redundancy)

#count- increment till nombre de bombes (doit etre = nbMine(constante))
global grille,bombe, count
global nbMine
global placeBombeListeUnique


nbMine=5
count=0

#commencer une nouvelle partie= nouveau code HTML avec case vides, nouvelles bombes etc
def decla(ran, col):
    global placeBombeListeUnique
    placeBombeListeUnique=[""]
    global grille, bombe
    grille=[]
    bombe=[]
    
    for i in range(1,ran+2):
        
        grille1=[]
        grille2=[]
        for j in range(1,col+2):
            grille1.append("0")
            grille2.append(False)
                
        grille.append(grille1)  
        bombe.append(grille2)
            
     

# Prend un entier représentant l'index d'une tuile et retourne
# l'identifiant HTML(id) de l'élément représentant cette case dans le DOM
def idCase(col,ran):
    return "tuile" + colRow(ran,col)

#logique de row+col pour les cases (12: 1 row, 2 columns i.e case representant cela)
def colRow(ran,col):
    return str(ran)+str(col)
    
def detecteClickShift(case):
        grille[case]="flag"
        
        pic=image(case)
        
        num=idCase(case)
        
        num=document.querySelector('#main')
        num.innerHTML=pic
        
#code qui commence la partie   
def init(ran,col):
    global grille
    
    start()
    
    main=document.querySelector('#main')
    main.innerHTML=""
    
    string=decideRangeeCol(ran,col)
    main.innerHTML = string
    
    
    
    #TEST SEULEMENT pour verifier flag; a enlever lorsque SHIFT sera fait !!!!!!!!!!!!!!!!!!!!!!! (IMPORTANT)
    #tuile11=document.querySelector('#tuile11')
    #tuile11.innerHTML='<img src="http://codeboot.org/images/minesweeper/flag.png">'
    #grille[1][1]="D"


# Prend deux entiers représentant les nombres de rangee et colonne et retourne
# le code HTML pour creer les tuiles
def decideRangeeCol(ran,col):
    string='''
  <link rel="preload" href="http://codeboot.org/images/minesweeper/0.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/1.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/2.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/3.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/4.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/5.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/6.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/7.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/8.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/blank.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/flag.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/mine.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/mine-red.png">
  <link rel="preload" href="http://codeboot.org/images/minesweeper/mine-red-x.png">'''
   
    string=string + '''<style>\n

      #main table {\n
        border: 1px solid black;\n
        margin: 10px;\n
      }\n
      #main table td {\n
        width: 30px;\n
        height: 30px;\n
        border: none;\n
      }\n
      </style>\n

      <table>\n'''
    global event
    
    #logique de ne pas considerer 0; facilité conversion string-integer et inverse ("01" to integer = chiant)
    #
    #cependant il faut changer pour considerer le cas de >=10 rangees et cols !!!!!!!!!!!!!!!!!!!!!!! (IMPORTANT)
    for i in range(1,ran+1):
        counts=0
        string=string + '<tr>\n'
        for j in range(1,col+1):
            counts=counts+1
            
            string=string + '<td id="' +idCase(counts,i) + '" onclick="clic('+str(colRow(i,counts))+', event)"><img src="http://codeboot.org/images/minesweeper/blank.png"></td>'+'\n'
        string=string + '</tr>\n'

    string=string + '</table>'
    
    return string

#_COPY PASTE; sauvegarder au cas ou; sleep(0) a l'air important_
# Met à jour le HTML pour refléter l'état des tuiles
#def mettreAJourHTML():
 #   for case in range(len(grille)):
  #      element = document.querySelector("#" + idCase(case))
        
   #     if joueur = image(grille[case])
        
        #element.innerHTML = (joueur)
    #sleep(0) # hack pour redonner le control au navigateur pour dessiner
             # le DOM




#EVENEMENTS

#check si tous les elements de la grille sont des bombes et decrement count
#qui doit etre=0 si win
#techniquement, c une fonction qui teste seulement victoire et pas losing scenario
def victoire(ran, col):
    
    count=(ran*col)-nbMine
    done=False
    coded=False
    for i in range(1,ran+1):
        for j in range(1,col+1):
           
            #il faut que casevide/ flag+bombe = nombre de mines
            if grille[i][j]=="DONE":  #rien de devoiler(blank)
                count=count-1
           
            elif grille[i][j]=="D" and bombe[i][j]!=True:
                count=count+1
                coded=True
                break
                
        if coded==True:
            break
        if i==ran+1 and j==ran+1:
            done=True
    
    if coded==True:
        return False
    elif count==0 :
        breakpoint()
        change=image("0")
        coded=True
        id="tuile" + str(ran)+str(col)
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        
        return True
    else:
        return False
                
            
    
    
def placeBombeAleatoire(case):
    global bombe
    global placeBombeListeUnique
    placeBombeListeUnique=[]
    #(1er element)= 1ere case
    x=11
    boo=False
    
    #check si les emplacements des mines sont uniques
    
    while len(placeBombeListeUnique) != nbMine:
        x=random()*59
        x=math.floor(x)
        l=str(x)
       
        #Le 9 a enlever!!!!!!! pour cela il faut rajouter condition de quand tu mets
        #un chiffre, +1 a enelever(convention de programmation; rajout 1 quon veut eviter ici)
        #!!!!!!!!!!!!!!!!!! (IMPORTANT) mais en bas de l'echelle d'importance
        if x>10 and x<59 and x%10!=0 and l[1:]!="9" and l[1:]!="0" and l!=str(case):
            boo=False
            
            for i in range(0,len(placeBombeListeUnique)):
               
                if placeBombeListeUnique[i]==str(x):
                    boo=True
                    break
                        
            if boo==False:
               
                placeBombeListeUnique.append(l)
                row=int(l[:1])
                col=int(l[1:])
               
                bombe[row][col]=True
                 
    #hack pour savoir ou sont les bombes pour faciliter les tests               
    print(placeBombeListeUnique)       


#pas eu besoin mais peut etre utile pour la recursion
def bombeACote(casestr):
    
    pass
    
    
#keep au cas ou mais will probably not be necessary    
def calculeGrille():
    pass
    
# Gestionnaire d'évènement d'un clic sur une case.
# Le paramètre case est un entier représentant l'index de la case cliquée
def clic(case, event):
    global  grille, bombe
    global count, coded
    coded=False
    count=count+1
    
    if count==1:
        init(5,8)
        
        placeBombeAleatoire(case)
   
    casestr=str(case)
    
    id = "tuile" + casestr
    
    
    calculeGrille()
    
    if event.shiftKey and grille[int(casestr[:1])][int(casestr[1:])]=="D":
       
        change=image("blank")
        coded=True
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        
        grille[int(casestr[:1])][int(casestr[1:])]="0"
        
    elif event.shiftKey and (grille[int(casestr[:1])][int(casestr[1:])]=="0" or bombe[int(casestr[:1])][int(casestr[1:])]==True):
        
        change=image("flag")
       
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        
        grille[int(casestr[:1])][int(casestr[1:])]="D"
        
    
    
    if  grille[int(casestr[:1])][int(casestr[1:])]=="0":
        
        if coded==False and (grille[int(casestr[:1])][int(casestr[1:])]=="0") and bombe[int(casestr[:1])][int(casestr[1:])]!=True:
            ###TESTE AVEC MINE mais la il faut appeler la fonction recursive
       
            pos=recurs(casestr)
        
            #l=document.querySelector("#" + id)
            #l.innerHTML=(change)
            
        
            grille[int(casestr[:1])][int(casestr[1:])]="DONE"
           #Mainetant il faut calculer pour les bombes adjacentes
        
            bombeACote(casestr)
            
            #acote=bombeACote()________________________________________________________
            #ICI il faut calculer les bombes a cote a condition qu'on soit au >=2e tour sinon appelle avec 0
        
            change=image("0")
           
            l=document.querySelector("#" + id)
            l.innerHTML=(change)
            #mettreAJourHTML()
        elif coded==True:
            coded=False
            
    if bombe[int(casestr[:1])][int(casestr[1:])]==True and grille[int(casestr[:1])][int(casestr[1:])]!="D":
           
            # grille[1][1]="D"
            devoileBombe(casestr)
        
            change=image("mine-red")
          
            l=document.querySelector("#" + id)
            l.innerHTML=(change)
         
            alert("YOU LOST")
        
            count=0
      
    if victoire(5,8)==True:
            
            devoileBombe(casestr)
            
            alert("YOU WON")
        
            count=0
        
            
                                     
                                     

#IMPORTANT !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#trouver cas de base d'abord
def recurs(rang, colonne):
    grille[[]]=-1
    rang=int(casestr[:1])
    colonne=int(casestr[1:])
    if [grille[rang+1][colonne]]==casevide:
        casestr=str(int(casestr[:1])[int(casestr[1:])])
    if [grille[rang][colonne+1]]==casevide:
        casestr=str(int(casestr[:1])[int(casestr[1:])])
    return     
        
#devoiles les bombes lorsque perdu donc si bombe; si flag et not bombe
def devoileBombe(casestr):
    global placeBombeListeUnique, bombe, grille
    
    for i in range(nbMine):
        
        change=image("mine")
        id= "tuile" + str(placeBombeListeUnique[i])
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        
       # if grille[int(str(placeBombeListeUnique[i])[:1])][int(str(placeBombeListeUnique[i])[1:])]=="D" and str(casestr)!=str(placeBombeListeUnique[i]):
            
        #    change=image("mine-red-x")
         #   id= "tuile" + str(placeBombeListeUnique[i])
          #  l=document.querySelector("#" + id)
           # l.innerHTML=(change)
            
    #for i in range(nbMine):
       
      #  if grille[int(str(placeBombeListeUnique[i])[:1])][int(str(placeBombeListeUnique[i])[1:])]=="D":
            #done=True
        #    change=image("flag")
         #   id= "tuile" + str(placeBombeListeUnique[i])
         #   l=document.querySelector("#" + id)
         #   l.innerHTML=(change)
            
            
    for i in range(1,5+1):
        for j in range(1,8+1):
            p=False
            
            k=-1
            while (k!=(nbMine-1) and p==False):
               # breakpoint()
                k=k+1
                if (bombe[i][j]!=True) and grille[i][j]=="D" :
                   
                    change=image("mine-red-x")
                    id= "tuile" + str(i) + str(j)
                    l=document.querySelector("#" + id)
                    l.innerHTML=(change)
                
                if grille[i][j]=="D" and (placeBombeListeUnique[k]==str(i)+str(j)):
                    #breakpoint()
                    
                    p=True
                    change=image("flag")
                    id= "tuile" + str(i) + str(j)
                    l=document.querySelector("#" + id)
                    l.innerHTML=(change)
                    
                 
                    
                    

#besoin pour demarrage de la 2e et > partie
def start():
    decla(5,8)
    
    
#pour le DOM    
def image(x):
    
    return '<img src="http://codeboot.org/images/minesweeper/'+ str(x) +'.png">'

#1ere partie
init(5,8)
