#Vennila Sooben(20235256) et Alexandra Morin (20236038)
#TP2 - IFT1015
#Mercredi 21 decembre 2022

#Ce programme permet de jouer au jeu demineur. En cliquant sur les tuiles, il faut faire attention de ne pas toucher une mine. 
#Les chiffres dévoilé indique la proximité de la mine (Par exemple: 1 veut dire que la bombe est à coté).

#DECLAS
#grille pour l'emplacement des bombes
#grilleInfo avec l'emplacement des bombes+drapeaux


#placeBombeListeUnique; liste avec emplacement exactement uniquement (check 
#if can erase grilleBombe and use just that and check for inverse as well =
#reduce data redundancy)

#count- increment till nombre de bombes (doit etre = nbMine(constante))
global grille, bombe, count, grilleInfo
global gRangee,gColonne
global nbMine
global placeBombeListeUnique
global bPremierClick
global nbCaseVue

count=0
caseVide=0
caseBombe=100
casevue=200
casepasclic=300
caseDrapeau=400
bPremierClick=True
nbCaseVue = 0

#commencer une nouvelle partie= nouveau code HTML avec case vides, nouvelles bombes etc
def decla(ran, col):
    global placeBombeListeUnique
    placeBombeListeUnique=[""]
    global grille
    grille=[]
    
    for i in range(1,gRangee+2):
        grille1=[]
        grille2=[]
        for j in range(1,gColonne+2):
            grille1.append(caseVide)
            grille2.append(False)
                
        grille.append(grille1)  

# Prend un entier représentant l'index d'une tuile et retourne
# l'identifiant HTML(id) de l'élément représentant cette case dans le DOM
def idCase(colonne,rangee):
    return "tuile" + colRow(rangee,colonne)

#logique de row+col pour les cases (12: 1 row, 2 columns i.e case representant cela)
def colRow(rangee,colonne):
    return str(rangee)+str(caseVide)+str(colonne)
    
def detecteClickShift(case):
    grille[case]="flag"
    pic=image(case)
    num=idCase(case)
    num=document.querySelector('#main')
    num.innerHTML=pic
        
# La procédure init(largeur, hauteur) démarre la partie de démineur.
# Cette procédure prend deux entiers en paramètres représentant 
# respectivement la largeur de la grille de jeu et la hauteur de la grille.
def init(rang,colo):
    global grille
    global gRangee, gColonne
    
    gRangee=rang
    gColonne=colo
    start()
    
    main=document.querySelector('#main')
    main.innerHTML=""
    string=decideRangeeCol(rang,colo)
    main.innerHTML = string
    
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
    for i in range(1,gRangee+1):
        counts=0
        string=string + '<tr>\n'
        for j in range(1,gColonne+1):
            counts=counts+1
            string=string + '<td id="' +idCase(counts,i) + '" onclick="clic('+str(colRow(i,counts))+', event)"><img src="http://codeboot.org/images/minesweeper/blank.png"></td>'+'\n'
        string=string + '</tr>\n'

    string=string + '</table>'
    return string

#EVENEMENTS

#check si tous les elements de la grille sont des bombes et decrement count
#qui doit etre=0 si win
#techniquement, c une fonction qui teste seulement victoire et pas losing scenario
def victoire():
    global gRangee,gColonne, nbMine, grilleInfo
    print(grilleInfo)
    count=nbMine
    done=False
    
    for i in range(1,gRangee+1):
        for j in range(1,gColonne+1):
            #il faut que casevide/ flag+bombe = nombre de mines
            #if grilleDevoilee[i][j]==False:  #rien de devoiler(blank)
            #    count=count-1
            if grilleInfo[i][j] == caseVide:
                
                count=count-1
                
        if i==gRangee+1 and j==gRangee+1:
            done=True
    
    print(count)
    if count==nbMine :
        change=image("0")
        id="tuile" + str(gRangee)+str(gColonne)
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        return True
    else:
        return False
    
def placeBombeAleatoire(case):
    global bombe, gRangee,gColonne, nbMine, grilleInfo
    global placeBombeListeUnique
   
    boo=False
    bbombe=False
    b=False
    ranAc=math.floor(case/100)
    colAc=case-ranAc*100
    
    chooserowcol=math.floor(random()*3)  
    if chooserowcol==1:
        nbMine=math.floor(random()*(gRangee+1))
    else:
        nbMine=math.floor(random()*(gColonne+1))
    nbMine+=1 #Pour avoir au moin 1 mine
    placeBombeListeUnique=[]
    grilleInfo=[]
    #check si les emplacements des mines sont uniques
    while len(placeBombeListeUnique) != nbMine:
        r=math.floor(random()*gRangee)
        c=math.floor(random()*gColonne)
        l=str(r) + str(c)
        x=int(l)
       
        #Le 9 a enlever!!!!!!! pour cela il faut rajouter condition de quand tu mets
        #un chiffre, +1 a enelever(convention de programmation; rajout 1 quon veut eviter ici)
        #!!!!!!!!!!!!!!!!!! (IMPORTANT) mais en bas de l'echelle d'importance
        if r>0 and c>0 and grille[r][c] != caseBombe and r!= ranAc and c!=colAc:
            
            grille[r][c]=caseBombe
           
            placeBombeListeUnique.append(str(r) + str(caseVide) + str(c))
            #Ceci calcule les chiffres proche des bombes
            if r+1 <= gRangee and grille[r+1][c]!=caseBombe:
                grille[r+1][c]+=1
            if r+1 <= gRangee and c+1 <= gColonne and grille[r+1][c+1]!=caseBombe:
                grille[r+1][c+1]+=1
            if c+1 <= gColonne and grille[r][c+1]!=caseBombe:
                grille[r][c+1]+=1
            if c-1 >= 0 and grille[r][c-1]!=caseBombe:
                grille[r][c-1]+=1
            if r-1 >= 0 and c-1 >= 0 and grille[r-1][c-1]!=caseBombe:
                grille[r-1][c-1]+=1
            if r+1 <= gRangee and c-1 >= 0 and grille[r+1][c-1]!=caseBombe:
                grille[r+1][c-1]+=1
            if r-1 >= 0 and grille[r-1][c]!=caseBombe:
                grille[r-1][c]+=1
            if r-1 >= 0 and c+1 <= gColonne and grille[r-1][c+1]!=caseBombe:
                grille[r-1][c+1]+=1
           
        #else:
            #print("Case prise", r, c )
                 
    #hack pour savoir ou sont les bombes pour faciliter les tests               
    grilleInfo=grille
    for i in range(1,gRangee+1):
        for j in range(1,gColonne+1):
            if not(grilleInfo[i][j]==0 or grille[i][j]==100):
                grilleInfo[i][j]=0
                
           
    print(placeBombeListeUnique)       
    
# Gestionnaire d'évènement d'un clic sur une case.
# Le paramètre case est un entier représentant l'index de la case cliquée
# La procédure clic(...) traite les évènements onclick sur les tuiles de
# la grille. Le nombre et le type des paramètres sont laissés au choix, 
# car cela dépendra de votre choix de représentation de la grille dans 
# votre programme. 
# La procédure clic(...) doit être appelée dans les champs onclick de vos
# tuiles avec les paramètres requis afin d'identifier la position du clic 
# et si la touche SHIFT était enfoncée au moment du clic.
def clic(case, event):
    global grille, bombe,gRangee, gColonne, grilleInfo
    global count, coded
    global bPremierClick

    
    # Ce n'est que lors du premier clic sur une tuile que les mines sont 
    # placées aléatoirement dans la grille afin d'éviter que le premier clic
    # du joueur ne soit sur un mine. 
   
    coded=False
    count=count+1
    casestr=str(case)
    id = "tuile" + casestr
    rangee = int(casestr[:1])
    colonne = int(casestr[1:])
    if count==1:
        init(gRangee,gColonne)
        
        placeBombeAleatoire(case)
    print(grilleInfo)
    if event.shiftKey and grilleInfo[rangee][colonne]==caseDrapeau:
        change=image("blank")
        coded=True
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        grille[int(casestr[:1])][int(casestr[1:])]=caseVide
        
    elif event.shiftKey:
        change=image("flag")
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        grilleInfo[rangee][colonne]=caseDrapeau
    
    elif grille[rangee][colonne]==caseVide:
        if coded==False and grille[rangee][colonne]!=caseBombe:
            pos=recurs(rangee, colonne) 
        elif coded==True:
            coded=False
            
    elif grille[rangee][colonne]==caseBombe:
            devoileBombe(casestr)
            change=image("mine-red")
            l=document.querySelector("#" + id)
            l.innerHTML=(change)
            alert("YOU LOST")
            count=0
    elif not(event.shiftKey):
        change=image(str(grille[rangee][colonne]))
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        grilleInfo[rangee][colonne]=casevue
        
    if victoire()==True:
            devoileBombe(casestr)
            alert("YOU WON")
            
            count=0

#Cette fonction permet de devoilée les cases vides qui se touche dès qu'une
#casevide est cliquer
def recurs(rang,colonne):
    global nbCaseVue
    nbCaseVue += 1
    grille[rang][colonne]=casevue
    change=image("0")
    id= "tuile" + str(rang) +"0" + str(colonne)
    l=document.querySelector("#" + id)
    l.innerHTML=(change)
    
    if grille[rang][colonne]==caseBombe:
        return nbCaseVue
    #permet de devoile la cases vide cliquer
    elif grille[rang][colonne]==caseVide:
        recurs(rang, colonne)
    #Si la case directement en bas est vide,elle est devoilee
    elif rang+1<=gRangee and grille[rang+1][colonne]==caseVide:
        recurs(rang+1, colonne)
    #Si la case directement en haut est vide,elle est devoilee
    elif rang-1>0-1 and grille[rang-1][colonne]==caseVide:
        recurs(rang-1, colonne)
    #Si la case directement a droite est vide,elle est devoilee
    elif colonne+1 <= gColonne and grille[rang][colonne+1]==caseVide:
        recurs(rang, colonne+1)
    #Si la case directement a gauche est vide,elle est devoilee
    elif colonne-1>0-1 and grille[rang][colonne-1]==caseVide:
        recurs(rang, colonne-1)
    #Si la case diagonale haute-gauche est vide,elle est devoilee
    elif colonne-1>0-1 and rang-1>0-1 and grille[rang-1][colonne-1]==caseVide:
        recurs(rang-1, colonne-1)
    #Si la case diagonale haute-droite est vide,elle est devoilee
    elif colonne+1 <= gColonne and rang-1>0-1 and grille[rang-1][colonne+1]==caseVide:
        recurs(rang-1, colonne+1)
    #Si la case diagonale bas-gauche est vide,elle est devoilee
    elif colonne-1>0-1 and rang+1<=gRangee and grille[rang+1][colonne-1]==caseVide:
        recurs(rang+1, colonne-1)
    #Si la case diagonale bas-droite est vide,elle est devoilee
    elif colonne+1 <= gColonne and rang+1<=gRangee and grille[rang+1][colonne+1]==caseVide:
        recurs(rang+1, colonne+1)
   
    return nbCaseVue
        
#devoiles les bombes lorsque perdu donc si bombe; si flag et not bombe
def devoileBombe(casestr):
    global placeBombeListeUnique, bombe, grille, rang,col
    
    for i in range(nbMine):
        change=image("mine")
        id= "tuile" + str(placeBombeListeUnique[i])
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
            
    for i in range(1,gRangee+1):
        for j in range(1,gColonne+1):
            p=False
            k=-1
            while (k!=(nbMine-1) and p==False):
              
                k=k+1
                if (grille[i][j]==caseBombe):
                    change=image("mine")
                    id= "tuile" + str(i) +"0" + str(j)
                    l=document.querySelector("#" + id)
                    l.innerHTML=(change)
                
                if grilleInfo[i][j]==caseDrapeau and (placeBombeListeUnique[k]==str(i)+ "0" +str(j)):
                   
                    p=True
                    change=image("flag")
                    id= "tuile" + str(i) + "0" +str(j)
                    l=document.querySelector("#" + id)
                    l.innerHTML=(change)
                    
                elif grilleInfo[i][j]==caseDrapeau:
                    change=image("mine-red-x")
                    id= "tuile" + str(i) + "0" +str(j)
                    l=document.querySelector("#" + id)
                    l.innerHTML=(change)

#besoin pour demarrage de la 2e et > partie
def start():
    global gRangee, gColonne
    
    decla(gRangee,gColonne)
    
#pour le DOM    
def image(x):
    return '<img src="http://codeboot.org/images/minesweeper/'+ str(x) +'.png">'

def testUnitaires():
    if decla(8,8):
        assert recurs(8,8)==64
    if decla(5,8):
        assert recurs(5,8)==40
    if decla(0,0):
        assert recurs(0,0)==0

#1ere partie
init(5,5)
