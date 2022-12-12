# TP2; 
# 
#ALSO; flag thingy was kind of hardcoded; need to fix that if got time

#CHERCHER LES !!!!!!!!!!!!!!!!!!! dans le code pour les points importants

#A faire :
#2. BETTER COMMENTS AND VARIABLE NAMES
#3. TESTS UNITAIRES


#DECLAS
#grille pour noter tous les coups

#grilleBombe pour l'emplacement des bombes (meme format que grilleBombe)

#placeBombeListeUnique; liste avec emplacement exactement uniquement (check 
#if can erase grilleBombe and use just that and check for inverse as well =
#reduce data redundancy)

#count- increment till nombre de bombes (doit etre = nbMine(constante))
global grille, bombe, count
global gRangee,gColonne
global nbMine
global placeBombeListeUnique
global bPremierClick
global nbCaseVue

count=0
casevide=0
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
            grille1.append(casevide)
            grille2.append(False)
                
        grille.append(grille1)  

# Prend un entier représentant l'index d'une tuile et retourne
# l'identifiant HTML(id) de l'élément représentant cette case dans le DOM
def idCase(colonne,rangee):
    return "tuile" + colRow(rangee,colonne)

#logique de row+col pour les cases (12: 1 row, 2 columns i.e case representant cela)
def colRow(rangee,colonne):
    return str(rangee)+str(casevide)+str(colonne)
    
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
    global gRangee,gColonne
   
    count=(gRangee*gColonne)-nbMine
    done=False
    coded=False
    for i in range(1,gRangee+1):
        for j in range(1,gColonne+1):
            #il faut que casevide/ flag+bombe = nombre de mines
            #if grilleDevoilee[i][j]==False:  #rien de devoiler(blank)
            #    count=count-1
            if grille[i][j] != caseBombe:
                count=count+1
                coded=True
                break
                
        if coded==True:
            break
        if i==gRangee+1 and j==gRangee+1:
            done=True
    
    if coded==True:
        return False
    elif count==0 :
        change=image("0")
        coded=True
        id="tuile" + str(gRangee)+str(gColonne)
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        return True
    else:
        return False
    
def placeBombeAleatoire():
    global bombe, gRangee,gColonne, nbMine
    global placeBombeListeUnique

    boo=False
    bbombe=False
    #breakpoint()
    
    nbMine=3 #math.floor(random()*gRangee*gColonne)
    
    placeBombeListeUnique=[]
    print( "Nombre de mine", nbMine)
    
    #check si les emplacements des mines sont uniques
    while len(placeBombeListeUnique) != nbMine:
        r=math.floor(random()*gRangee)
        c=math.floor(random()*gColonne)
        l=str(r) + str(c)
        x=int(l)
        
        #Le 9 a enlever!!!!!!! pour cela il faut rajouter condition de quand tu mets
        #un chiffre, +1 a enelever(convention de programmation; rajout 1 quon veut eviter ici)
        #!!!!!!!!!!!!!!!!!! (IMPORTANT) mais en bas de l'echelle d'importance
        if r>0 and c>0 and grille[r][c] != caseBombe:
            print(r,c)
            grille[r][c]=caseBombe
            placeBombeListeUnique.append(str(r) + str(casevide) + str(c))
            if r+1 < gRangee and grille[r+1][c]!=caseBombe:
                grille[r+1][c]+=1
            if r+1 < gRangee and c+1 < gColonne and grille[r+1][c+1]!=caseBombe:
                grille[r+1][c+1]+=1
            if c+1 < gColonne and grille[r][c+1]!=caseBombe:
                grille[r][c+1]+=1
            if c-1 >= 0 and grille[r][c-1]!=caseBombe:
                grille[r][c-1]+=1
            if r-1 >= 0 and c-1 >= 0 and grille[r-1][c-1]!=caseBombe:
                grille[r-1][c-1]+=1
            if r+1 < gRangee and c-1 >= 0 and grille[r+1][c-1]!=caseBombe:
                grille[r+1][c-1]+=1
            if r-1 >= 0 and grille[r-1][c]!=caseBombe:
                grille[r-1][c]+=1
            if r-1 >= 0 and c+1 > gColonne and grille[r-1][c+1]!=caseBombe:
                grille[r-1][c+1]+=1
        else:
            print("Case prise", r, c )
                 
    #hack pour savoir ou sont les bombes pour faciliter les tests               
    print(grille)
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
    global grille, bombe,gRangee, gColonne
    global count, coded
    global bPremierClick

    if event.currentTarget == None:
        return
    
    # Ce n'est que lors du premier clic sur une tuile que les mines sont 
    # placées aléatoirement dans la grille afin d'éviter que le premier clic
    # du joueur ne soit sur un mine. 
    if bPremierClick == True:
        bPremierClick = False
        #breakpoint()
        placeBombeAleatoire()
        
    coded=False
    count=count+1
    casestr=str(case)
    id = "tuile" + casestr
    rangee = int(casestr[:1])
    colonne = int(casestr[1:])
    
    if event.shiftKey and grille[rangee][colonne]==caseDrapeau:
        change=image("blank")
        coded=True
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        grille[int(casestr[:1])][int(casestr[1:])]="0"
        
    elif event.shiftKey and (grille[rangee][colonne]==caseVide or grille[rangee][colonne]==caseBombe):
        change=image("flag")
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        grille[rangee][colonne]=caseDrapeau
    
    if grille[rangee][colonne]==casevide:
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
    else:
        change=image(str(grille[rangee][colonne]))
        l=document.querySelector("#" + id)
        l.innerHTML=(change)
        
    if victoire()==True:
            devoileBombe(casestr)
            alert("YOU WON")
            count=0

#Cette fonction permet de devoilée les cases vides qui se touche dès qu'une
#casevide est cliquer
def recurs(rang,colonne):
    nbCaseVue += 1
    grille[rang][colonne]=casevue
    print(grille)
    change=image("0")
    id= "tuile" + str(rang) +"0" + str(colonne)
    l=document.querySelector("#" + id)
    l.innerHTML=(change)
    
    #permet de devoile la cases vide cliquer
    if grille[rang][colonne]==casevide:
        recurs(rang, colonne)
    #Si la case directement en bas est vide,elle est devoilee
    if rang+1<gRangee and grille[rang+1][colonne]==casevide:
        recurs(rang+1, colonne)
    #Si la case directement en haut est vide,elle est devoilee
    if rang-1>0-1 and grille[rang-1][colonne]==casevide:
        recurs(rang-1, colonne)
    #Si la case directement a droite est vide,elle est devoilee
    if colonne+1 < gColonne and grille[rang][colonne+1]==casevide:
        recurs(rang, colonne+1)
    #Si la case directement a gauche est vide,elle est devoilee
    if colonne-1>0-1 and grille[rang][colonne-1]==casevide:
        recurs(rang, colonne-1)
    #Si la case diagonale haute-gauche est vide,elle est devoilee
    if colonne-1>0-1 and rang-1>0-1 and grille[rang-1][colonne-1]==casevide:
        recurs(rang-1, colonne-1)
    #Si la case diagonale haute-droite est vide,elle est devoilee
    if colonne+1 < gColonne and rang-1>0-1 and grille[rang-1][colonne+1]==casevide:
        recurs(rang-1, colonne+1)
    #Si la case diagonale bas-gauche est vide,elle est devoilee
    if colonne-1>0-1 and rang+1<gRangee and grille[rang+1][colonne-1]==casevide:
        recurs(rang+1, colonne-1)
    #Si la case diagonale bas-droite est vide,elle est devoilee
    if colonne+1 < gColonne and rang+1<gRangee and grille[rang+1][colonne+1]==casevide:
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
               # breakpoint()
                k=k+1
                if (grille[i][j]==caseBombe):
                    change=image("mine-red-x")
                    id= "tuile" + str(i) +"0" + str(j)
                    l=document.querySelector("#" + id)
                    l.innerHTML=(change)
                
                if grille[i][j]==caseDrapeau and (placeBombeListeUnique[k]==str(i)+ "0" +str(j)):
                    #breakpoint()
                    p=True
                    change=image("flag")
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

#Cette fonction test toutes les fonctions utilisé pour le jeu demineur
def testUnitaires():
    if decla(8,8):
        assert recurs(8,8)==64
    if decla(5,8):
        assert recurs(5,8)==40
    if decla(0,0):
        assert recurs(0,0)==0

#1ere partie
init(5,5)
