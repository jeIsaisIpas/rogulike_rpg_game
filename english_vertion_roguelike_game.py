# English UI translation generated automatically. Identifiers kept to preserve compatibility.
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#V18 - ROGUELIKE DES CATACOMBES

import os 
import json 
import random 
from dataclasses import dataclass ,field 
from typing import List ,Dict ,Tuple ,Optional 

# ======================================================
# ANSI Colors
# ======================================================
COLOR_RESET ="\033[0m"
COLOR_RED ="\033[91m"
COLOR_GREEN ="\033[92m"
COLOR_YELLOW ="\033[93m"
COLOR_BLUE ="\033[94m"
COLOR_MAGENTA ="\033[95m"
COLOR_CYAN ="\033[96m"
COLOR_BOLD ="\033[1m"

def rgb (r ,g ,b ):
    """Return a 24-bit ANSI color code (RGB)."""
    return f"[38;2;{r };{g };{b }m"

def rgb_bg (r ,g ,b ):
    """Return a 24-bit ANSI background code (RGB)."""
    return f"[48;2;{r };{g };{b }m"

    # Redefinition of colors in RGB style for V18
COLOR_RED =rgb (255 ,80 ,80 )
COLOR_GREEN =rgb (80 ,255 ,80 )
COLOR_YELLOW =rgb (255 ,220 ,50 )
COLOR_BLUE =rgb (80 ,160 ,255 )
COLOR_MAGENTA =rgb (220 ,80 ,255 )
COLOR_CYAN =rgb (80 ,255 ,255 )
COLOR_BOLD ="[1m"


def clear_console ()->None :
    os .system ('cls'if os .name =='nt'else 'clear')


def attendre_entree ()->None :
    input ("Press Enter to continue...")


    # ======================================================
    # Base data : player classes, weapons, relics, zones
    # ======================================================
PLAYER_CLASSES :Dict [str ,Dict ]={
"1":{"name":"Warrior","hp":35 ,"attack":6 ,"defense":3 ,"mana":5 ,"power":"Techniques de combat"},
"2":{"name":"Mage","hp":22 ,"attack":4 ,"defense":1 ,"mana":15 ,"power":"Arcanes élémentaires"},
"3":{"name":"Rogue","hp":28 ,"attack":5 ,"defense":2 ,"mana":8 ,"power":"Arts furtifs"},
"4":{"name":"Paladin","hp":40 ,"attack":5 ,"defense":4 ,"mana":8 ,"power":"Lumière sacrée"},
"5":{"name":"Ranger","hp":30 ,"attack":6 ,"defense":2 ,"mana":7 ,"power":"Maîtrise de l'arc"},
"6":{"name":"Necromancer","hp":24 ,"attack":5 ,"defense":1 ,"mana":18 ,"power":"Magies interdites"},
"7":{"name":"Assassin de l'Ombre","hp":26 ,"attack":7 ,"defense":2 ,"mana":10 ,"power":"Arts des ombres"},
"8":{"name":"Berserker","hp":38 ,"attack":8 ,"defense":2 ,"mana":4 ,"power":"Rage sanguinaire"},
"9":{"name":"Bard","hp":27 ,"attack":4 ,"defense":2 ,"mana":14 ,"power":"Chants inspirants"},
"10":{"name":"Monk","hp":32 ,"attack":5 ,"defense":3 ,"mana":9 ,"power":"Arts martiaux spirituels"},
"11":{"name":"Summoner","hp":23 ,"attack":3 ,"defense":1 ,"mana":20 ,"power":"Invocations ancestrales"},
}


@dataclass 
class Weapon :
    nom :str 
    atk_bonus :int =0 
    crit_bonus :float =0.0 
    description :str =""


WEAPONS :List [Weapon ]=[
Weapon ("Épée d'entraînement",atk_bonus =0 ,crit_bonus =0.0 ,
description ="Une vieille épée sans bonus particulier."),
Weapon ("Épée longue",atk_bonus =2 ,crit_bonus =0.05 ,
description ="Une épée solide qui inflige plus de dégâts que la moyenne."),
Weapon ("Hache lourde",atk_bonus =3 ,crit_bonus =0.0 ,
description ="Une hache très puissante, idéale pour les gros coups bruts."),
Weapon ("Dagues jumelles",atk_bonus =1 ,crit_bonus =0.12 ,
description ="Deux dagues rapides : critiques élevés et petite chance d'empoisonner."),
Weapon ("Clavier Runique des 1000 Lignes",atk_bonus =5 ,crit_bonus =0.25 ,
description ="Arme runique : très gros dégâts et critiques dévastateurs."),
Weapon ("Masse sacrée",atk_bonus =2 ,crit_bonus =0.02 ,
description ="Une masse bénie, modérément puissante et très fiable."),
Weapon ("Lame de braise",atk_bonus =2 ,crit_bonus =0.08 ,
description ="Une lame brûlante : dégâts accrus et critiques plus fréquents."),
Weapon ("Arc des ombres",atk_bonus =1 ,crit_bonus =0.15 ,
description ="Un arc léger : peu d'attack brute mais énormes chances critiques."),
]


@dataclass 
class Relic :
    nom :str 
    atk_bonus :int =0 
    def_bonus :int =0 
    crit_bonus :float =0.0 
    lifesteal :float =0.0 
    description :str =""


RELICS :List [Relic ]=[
Relic ("Amulette de Fureur",atk_bonus =2 ,crit_bonus =0.05 ,
description ="+2 ATQ et +5% critique."),
Relic ("Talisman de Pierre",def_bonus =2 ,
description ="+2 DEF."),
Relic ("Anneau Vampirique",lifesteal =0.3 ,
description ="Vol de vie 30% des dégâts infligés."),
Relic ("Œil du Critique",crit_bonus =0.2 ,
description ="+20% chance de coup critique."),
Relic ("Plume du Créateur",atk_bonus =3 ,def_bonus =1 ,crit_bonus =0.15 ,lifesteal =0.15 ,
description ="Relique mythique : ATQ+3, DEF+1, crit+15%, vol de vie."),
Relic ("Charme du Golem",def_bonus =3 ,
description ="+3 DEF : ta peau se durcit comme la pierre."),
Relic ("Sceau du Vampire",lifesteal =0.2 ,
description ="Vol de vie 20% : chaque coup te soigne légèrement."),
Relic ("Fragment d'étoile",atk_bonus =1 ,crit_bonus =0.1 ,
description ="+1 ATQ et +10% crit : tes coups frappent comme des éclats stellaires."),
]


# ======================================================
# Cards (progression system V17)
# ======================================================
@dataclass 
class Card :
    nom :str 
    description :str 
    rarete :str # "Common", "Rare", "Epic", "Legendary"
    classes_autorisees :Optional [List [str ]]=None # None => générique
    bonus_pv_max :int =0 
    bonus_attaque :int =0 
    bonus_defense :int =0 
    bonus_mana_max :int =0 
    bonus_potions :int =0 
    bonus_critique :float =0.0 


CARDS_POOL :List [Card ]=[
# Communes génériques
Card ("Endurance","+5 PV max","Common",bonus_pv_max =5 ),
Card ("Muscles tendus","+1 ATQ","Common",bonus_attaque =1 ),
Card ("Posture défensive","+1 DEF","Common",bonus_defense =1 ),
Card ("Méditation","+2 Mana max","Common",bonus_mana_max =2 ),
Card ("Flasque de secours","+1 potion","Common",bonus_potions =1 ),

# Rares génériques
Card ("Sang de guerrier","+10 PV max","Rare",bonus_pv_max =10 ),
Card ("Lame affûtée","+2 ATQ","Rare",bonus_attaque =2 ),
Card ("Armure ajustée","+2 DEF","Rare",bonus_defense =2 ),
Card ("Esprit focalisé","+4 Mana max","Rare",bonus_mana_max =4 ),
Card ("Pharmacie ambulante","+2 potions","Rare",bonus_potions =2 ),

# Épiques génériques
Card ("Robustesse surnaturelle","+15 PV max","Epic",bonus_pv_max =15 ),
Card ("Force brute","+3 ATQ","Epic",bonus_attaque =3 ),
Card ("Mur de fer","+3 DEF","Epic",bonus_defense =3 ),
Card ("Réservoir mystique","+6 Mana max","Epic",bonus_mana_max =6 ),
Card ("Spécialiste des fioles","+3 potions","Epic",bonus_potions =3 ),

# Légendaires génériques
Card ("Colosse immortel","+25 PV max, +2 DEF","Legendary",bonus_pv_max =25 ,bonus_defense =2 ),
Card ("Lame du destin","+5 ATQ, +10% crit","Legendary",bonus_attaque =5 ,bonus_critique =0.10 ),
Card ("Maître arcanique","+8 Mana max, +2 ATQ","Legendary",bonus_mana_max =8 ,bonus_attaque =2 ),

# Cards spécifiques de classe (exemples)
Card ("Discipline guerrière","+3 ATQ (Warrior)","Rare",
classes_autorisees =["Warrior"],bonus_attaque =3 ),
Card ("Études occultes","+5 Mana max (Necromancer)","Rare",
classes_autorisees =["Necromancer"],bonus_mana_max =5 ),
Card ("Instinct furtif","+10% crit (Rogue / Assassin de l'Ombre)","Rare",
classes_autorisees =["Rogue","Assassin de l'Ombre"],bonus_critique =0.10 ),
]


# Enemies & zones
CATACOMBES_ENNEMIS =[
{"name":"Rat géant","hp":12 ,"attack":3 ,"defense":1 ,"gold":(3 ,7 ),"xp":(5 ,8 )},
{"name":"Gobelin","hp":18 ,"attack":4 ,"defense":1 ,"gold":(6 ,12 ),"xp":(8 ,12 )},
{"name":"Squelette","hp":20 ,"attack":5 ,"defense":2 ,"gold":(10 ,18 ),"xp":(10 ,14 )},
]

FORET_ENNEMIS =[
{"name":"Loup sombre","hp":22 ,"attack":6 ,"defense":2 ,"gold":(10 ,18 ),"xp":(12 ,18 )},
{"name":"Dryade corrompue","hp":26 ,"attack":5 ,"defense":3 ,"gold":(12 ,20 ),"xp":(14 ,20 )},
{"name":"Ent déchaîné","hp":30 ,"attack":7 ,"defense":3 ,"gold":(15 ,24 ),"xp":(16 ,22 )},
]

CITADELLE_ENNEMIS =[
{"name":"Garde runique","hp":32 ,"attack":8 ,"defense":4 ,"gold":(18 ,26 ),"xp":(18 ,26 )},
{"name":"Mage de cristal","hp":28 ,"attack":9 ,"defense":3 ,"gold":(20 ,30 ),"xp":(20 ,28 )},
{"name":"Chevalier spectral","hp":36 ,"attack":9 ,"defense":4 ,"gold":(24 ,34 ),"xp":(22 ,30 )},
]

CATACOMBES_BOSSES =[
{"name":"Seigneur des Os","hp":45 ,"attack":7 ,"defense":3 ,"gold":(30 ,45 ),"xp":(35 ,50 )},
{"name":"Liche des Profondeurs","hp":40 ,"attack":9 ,"defense":2 ,"gold":(30 ,45 ),"xp":(35 ,50 )},
]

FORET_BOSSES =[
{"name":"Esprit de la Forêt Putride","hp":55 ,"attack":9 ,"defense":4 ,"gold":(40 ,60 ),"xp":(45 ,65 )},
{"name":"Reine Araignée","hp":50 ,"attack":10 ,"defense":3 ,"gold":(40 ,60 ),"xp":(45 ,65 )},
]

CITADELLE_BOSSES =[
{"name":"Seigneur Runique","hp":70 ,"attack":11 ,"defense":5 ,"gold":(60 ,80 ),"xp":(70 ,90 )},
{"name":"Champion du Vide","hp":65 ,"attack":12 ,"defense":4 ,"gold":(60 ,80 ),"xp":(70 ,90 )},
]

ZONES =[
{"name":"Catacombs","debut":1 ,"fin":10 ,"ennemis":CATACOMBES_ENNEMIS ,"bosses":CATACOMBES_BOSSES },
{"name":"Cursed Forest","debut":11 ,"fin":20 ,"ennemis":FORET_ENNEMIS ,"bosses":FORET_BOSSES },
{"name":"Runic Citadel","debut":21 ,"fin":30 ,"ennemis":CITADELLE_ENNEMIS ,"bosses":CITADELLE_BOSSES },
]

MAX_ETAGES =100 


# ======================================================
# Skill tree (skill tree) V17.2
# ======================================================
SKILL_TREE :Dict [str ,Dict ]={
# Améliorations de stats de base
"pv1":{
"name":"+5 PV de base",
"description":"Augmente les PV de base de 5 pour toutes les runs.",
"cout":5 ,
"type":"stat",
"cible":"pv_bonus",
"valeur":5 ,
"prerequis":[],
},
"atk1":{
"name":"+1 ATQ de base",
"description":"Augmente l'attack de base de 1.",
"cout":5 ,
"type":"stat",
"cible":"attaque_bonus",
"valeur":1 ,
"prerequis":[],
},
"def1":{
"name":"+1 DEF de base",
"description":"Augmente la défense de base de 1.",
"cout":5 ,
"type":"stat",
"cible":"defense_bonus",
"valeur":1 ,
"prerequis":[],
},
"mana1":{
"name":"+2 Mana de base",
"description":"Augmente le mana de base de 2.",
"cout":4 ,
"type":"stat",
"cible":"mana_bonus",
"valeur":2 ,
"prerequis":[],
},

# Ressources de départ
"potion1":{
"name":"+1 potion de départ",
"description":"Commencer chaque run avec une potion en plus.",
"cout":6 ,
"type":"start_res",
"cible":"potions_debut",
"valeur":1 ,
"prerequis":["pv1"],
},
"or1":{
"name":"+5 or de départ",
"description":"Commencer chaque run avec +5 or.",
"cout":4 ,
"type":"start_res",
"cible":"or_debut",
"valeur":5 ,
"prerequis":["atk1"],
},

# Chances de shop / mystère
"shop1":{
"name":"+1 niveau de chance de boutique",
"description":"Augmente la probabilité de tomber sur une boutique.",
"cout":6 ,
"type":"chance",
"cible":"bonus_chance_shop",
"valeur":1 ,
"prerequis":["or1"],
},
"mystere1":{
"name":"+1 niveau de chance d'événement mystère",
"description":"Augmente la probabilité de déclencher un événement mystère.",
"cout":6 ,
"type":"chance",
"cible":"bonus_chance_mystere",
"valeur":1 ,
"prerequis":["mana1"],
},

# Déblocage de classes déjà existantes
"class_paladin":{
"name":"Débloquer Paladin",
"description":"Permet de choisir la classe Paladin au début de la run.",
"cout":8 ,
"type":"unlock_class",
"cible":"Paladin",
"valeur":1 ,
"prerequis":["pv1"],
},
"class_rodeur":{
"name":"Débloquer Ranger",
"description":"Permet de choisir la classe Ranger au début de la run.",
"cout":8 ,
"type":"unlock_class",
"cible":"Ranger",
"valeur":1 ,
"prerequis":["atk1"],
},
"class_necromancien":{
"name":"Débloquer Necromancer",
"description":"Permet de choisir la classe Necromancer au début de la run.",
"cout":9 ,
"type":"unlock_class",
"cible":"Necromancer",
"valeur":1 ,
"prerequis":["mana1"],
},
"class_assassin_ombre":{
"name":"Débloquer Assassin de l'Ombre",
"description":"Permet de choisir la classe Assassin de l'Ombre au début de la run.",
"cout":10 ,
"type":"unlock_class",
"cible":"Assassin de l'Ombre",
"valeur":1 ,
"prerequis":["atk1","def1"],
},

# Nouvelles classes avancées
"class_berserker":{
"name":"Débloquer Berserker",
"description":"Permet de choisir la classe Berserker au début de la run.",
"cout":9 ,
"type":"unlock_class",
"cible":"Berserker",
"valeur":1 ,
"prerequis":["atk1"],
},
"class_barde":{
"name":"Débloquer Bard",
"description":"Permet de choisir la classe Bard au début de la run.",
"cout":8 ,
"type":"unlock_class",
"cible":"Bard",
"valeur":1 ,
"prerequis":["mana1"],
},
"class_moine":{
"name":"Débloquer Monk",
"description":"Permet de choisir la classe Monk au début de la run.",
"cout":9 ,
"type":"unlock_class",
"cible":"Monk",
"valeur":1 ,
"prerequis":["def1"],
},
"class_invocateur":{
"name":"Débloquer Summoner",
"description":"Permet de choisir la classe Summoner au début de la run.",
"cout":10 ,
"type":"unlock_class",
"cible":"Summoner",
"valeur":1 ,
"prerequis":["mana1","pv1"],
},
}


# ======================================================
# Meta-progression
# ======================================================
@dataclass 
class Meta :
    essence :int =0 
    pv_bonus :int =0 
    attaque_bonus :int =0 
    defense_bonus :int =0 
    mana_bonus :int =0 
    or_debut :int =0 
    potions_debut :int =0 
    bonus_chance_shop :int =0 
    bonus_chance_mystere :int =0 
    succes :Dict [str ,Dict ]=field (default_factory =dict )
    classes_debloquees :List [str ]=field (default_factory =lambda :["Warrior","Mage","Rogue"])
    talents_debloques :List [str ]=field (default_factory =list )
    filename :Optional [str ]=None 

    @classmethod 
    def choisir_slot (cls )->"Meta":
        while True :
            clear_console ()
            print (COLOR_CYAN +"===== CHOIX DU SLOT DE SAUVEGARDE ====="+COLOR_RESET )
            print (" 1) Slot 1")
            print (" 2) Slot 2")
            print (" 3) Slot 3")
            choix =input (">> ").strip ()
            if choix in ("1","2","3"):
                filename =f"meta_save_slot{choix }.json"
                return cls .charger (filename )
            print ("Choix invalide.")
            attendre_entree ()

    @classmethod 
    def charger (cls ,filename :str )->"Meta":
        if not os .path .exists (filename ):
            meta =cls ()
            meta .filename =filename 
            return meta 
        try :
            with open (filename ,'r',encoding ='utf-8')as f :
                data =json .load (f )
        except Exception :
            meta =cls ()
            meta .filename =filename 
            return meta 
        meta =cls (
        essence =data .get ("essence",0 ),
        pv_bonus =data .get ("pv_bonus",0 ),
        attaque_bonus =data .get ("attaque_bonus",0 ),
        defense_bonus =data .get ("defense_bonus",0 ),
        mana_bonus =data .get ("mana_bonus",0 ),
        or_debut =data .get ("or_debut",0 ),
        potions_debut =data .get ("potions_debut",0 ),
        bonus_chance_shop =data .get ("bonus_chance_shop",0 ),
        bonus_chance_mystere =data .get ("bonus_chance_mystere",0 ),
        succes =data .get ("succes",{}),
        classes_debloquees =data .get ("classes_debloquees",["Warrior","Mage","Rogue"]),
        talents_debloques =data .get ("talents_debloques",[]),
        filename =filename ,
        )
        return meta 

    def sauvegarder (self )->None :
        if not self .filename :
            return 
        data ={
        "essence":self .essence ,
        "pv_bonus":self .pv_bonus ,
        "attaque_bonus":self .attaque_bonus ,
        "defense_bonus":self .defense_bonus ,
        "mana_bonus":self .mana_bonus ,
        "or_debut":self .or_debut ,
        "potions_debut":self .potions_debut ,
        "bonus_chance_shop":self .bonus_chance_shop ,
        "bonus_chance_mystere":self .bonus_chance_mystere ,
        "succes":self .succes ,
        "classes_debloquees":self .classes_debloquees ,
        "talents_debloques":self .talents_debloques ,
        }
        try :
            with open (self .filename ,'w',encoding ='utf-8')as f :
                json .dump (data ,f ,ensure_ascii =False ,indent =2 )
        except Exception :
            pass 

    def debloquer_succes (self ,cle :str ,description :Optional [str ]=None )->bool :
        if cle in self .succes :
            return False 
        if cle =="premier_boss":
            self .attaque_bonus +=1 
            desc_defaut ="Premier boss vaincu (+1 ATQ de base)"
        elif cle =="tueur_de_monstres":
            self .pv_bonus +=5 
            desc_defaut ="A tué au moins 20 ennemis en une run (+5 PV de base)"
        elif cle =="explorateur":
            self .or_debut +=5 
            desc_defaut ="A atteint au moins l'étage 10 (+5 or au début de chaque run)"
        else :
            desc_defaut =cle 
        self .succes [cle ]={"description":description or desc_defaut }
        self .sauvegarder ()
        print (">>> SUCCÈS DÉBLOQUÉ : "+self .succes [cle ]["description"]+" <<<")
        return True 


        # ======================================================
        # Entities
        # ======================================================
@dataclass 
class Status :
    poison :int =0 
    brulure :int =0 
    stun :int =0 


@dataclass 
class Entity :
    nom :str 
    pv :int 
    pv_max :int 
    attaque :int 
    defense :int 
    mana :int =0 
    mana_max :int =0 
    statuts :Status =field (default_factory =Status )

    def est_vivant (self )->bool :
        return self .pv >0 

    def barre_vie (self ,longueur :int =20 )->str :
        if self .pv_max <=0 :
            return "["+"-"*longueur +"]"
        ratio =max (0 ,min (1 ,self .pv /self .pv_max ))
        rempli =int (ratio *longueur )
        vide =longueur -rempli 
        return "["+"#"*rempli +"-"*vide +"]"

    def appliquer_statuts (self )->bool :
        mort =False 
        if self .statuts .poison >0 :
            deg =max (1 ,int (self .pv_max *0.07 ))
            self .pv -=deg 
            self .statuts .poison -=1 
            print (f"{self .nom } souffre du poison et perd {deg } PV !")
            if self .pv <=0 :
                mort =True 
        if (not mort )and self .statuts .brulure >0 :
            deg =max (1 ,int (self .pv_max *0.09 ))
            self .pv -=deg 
            self .statuts .brulure -=1 
            print (f"{self .nom } est brûlé et perd {deg } PV !")
            if self .pv <=0 :
                mort =True 
        return mort 

    def est_stun (self )->bool :
        if self .statuts .stun >0 :
            self .statuts .stun -=1 
            return True 
        return False 


@dataclass 
class Player (Entity ):
    classe :str =""
    pouvoir :str =""
    niveau :int =1 
    xp :int =0 
    xp_next :int =20 
    potions :int =0 
    gold :int =0 
    etages_parcourus :int =0 
    ennemis_tues :int =0 
    boss_tues :int =0 
    or_gagne_total :int =0 
    arme :Weapon =field (default_factory =lambda :WEAPONS [0 ])
    armes :List [Weapon ]=field (default_factory =list )
    relique :Optional [Relic ]=None 
    invocation_squelette_tours :int =0 
    bonus_critique :float =0.0 

    def atq_effective (self )->int :
        atk =self .attaque 
        if self .arme :
            atk +=self .arme .atk_bonus 
        if self .relique :
            atk +=self .relique .atk_bonus 
        return atk 

    def def_effective (self )->int :
        df =self .defense 
        if self .relique :
            df +=self .relique .def_bonus 
        return df 

    def crit_chance (self )->float :
        base =0.05 
        if self .arme :
            base +=self .arme .crit_bonus 
        if self .relique :
            base +=self .relique .crit_bonus 
        base +=self .bonus_critique 
        return min (0.8 ,base )

    def lifesteal (self )->float :
        return self .relique .lifesteal if self .relique else 0.0 


@dataclass 
class Enemy (Entity ):
    gold_range :Tuple [int ,int ]=(0 ,0 )
    xp_range :Tuple [int ,int ]=(0 ,0 )
    element_resistances :Dict [str ,float ]=field (default_factory =dict )
    element_weaknesses :Dict [str ,float ]=field (default_factory =dict )


    # ======================================================
    # Game class
    # ======================================================
class Game :
    def __init__ (self ):
        self .meta :Meta =Meta .choisir_slot ()
        self .joueur :Optional [Player ]=None 

        # ------------------ Création joueur ------------------
    def creer_joueur (self )->Player :
        clear_console ()
        print (COLOR_MAGENTA +"="*30 +COLOR_RESET )
        print (COLOR_BOLD +" ROGUELIKE DES CATACOMBES"+COLOR_RESET )
        print (" Édition Roguelike ASCII")
        print (COLOR_MAGENTA +"="*30 +COLOR_RESET )
        print ()
        nom =input ("Entre le name de ton héros : ")or "Héros"
        print ()

        # Construire la liste des classes débloquées
        classes_disponibles :Dict [str ,Dict ]={}
        index =1 
        for _ ,infos in PLAYER_CLASSES .items ():
            if infos ["name"]in self .meta .classes_debloquees :
                classes_disponibles [str (index )]=infos 
                index +=1 

        if not classes_disponibles :
        # Sécurité : si jamais aucune classe n'est débloquée, on autorise les trois de base
            for _ ,infos in PLAYER_CLASSES .items ():
                if infos ["name"]in ("Warrior","Mage","Rogue"):
                    key =str (len (classes_disponibles )+1 )
                    classes_disponibles [key ]=infos 

        print ("Choisis une classe :")
        for key ,infos in classes_disponibles .items ():
            print (
            f" {key }) {infos ['name']} "
            f"PV:{infos ['hp']} ATQ:{infos ['attack']} "
            f"DEF:{infos ['defense']} Mana:{infos ['mana']}"
            )

        choix =None 
        while choix not in classes_disponibles :
            choix =input ("Ton choix : ").strip ()
        base =classes_disponibles [choix ]

        pv_base =base ['hp']+self .meta .pv_bonus 
        mana_base =base ['mana']+self .meta .mana_bonus 
        attaque_base =base ['attack']+self .meta .attaque_bonus 
        defense_base =base ['defense']+self .meta .defense_bonus 
        arme_base =WEAPONS [0 ]

        joueur =Player (
        nom =nom ,
        classe =base ['name'],
        pv =pv_base ,
        pv_max =pv_base ,
        attaque =attaque_base ,
        defense =defense_base ,
        mana =mana_base ,
        mana_max =mana_base ,
        statuts =Status (),
        pouvoir =base ['power'],
        niveau =1 ,
        xp =0 ,
        xp_next =20 ,
        potions =2 +self .meta .potions_debut ,
        gold =self .meta .or_debut ,
        etages_parcourus =0 ,
        ennemis_tues =0 ,
        boss_tues =0 ,
        or_gagne_total =0 ,
        arme =arme_base ,
        armes =[arme_base ],
        relique =None ,
        invocation_squelette_tours =0 ,
        bonus_critique =0.0 ,
        )

        clear_console ()
        print (f"Bienvenue, {joueur .nom } le {joueur .classe } !")
        print ("Les catacombes t'attendent...")
        attendre_entree ()
        self .joueur =joueur 
        return joueur 

        # ------------------ Affichage ------------------
    def afficher_statuts (self ,entite :Entity ,est_joueur :bool =True )->None :
        s =entite .statuts 
        actifs =[]
        if s .poison >0 :
            actifs .append (f"Poison({s .poison })")
        if s .brulure >0 :
            actifs .append (f"Brûlure({s .brulure })")
        if s .stun >0 :
            actifs .append (f"Stun({s .stun })")
        if actifs :
            cible ="Toi"if est_joueur else "Lui"
            print (f"Statuts {cible } : "+", ".join (actifs ))

    def afficher_etat_joueur (self )->None :
        j =self .joueur 
        if j is None :
            return 
        ratio_pv =j .pv /j .pv_max if j .pv_max >0 else 0 
        ratio_mana =j .mana /j .mana_max if j .mana_max >0 else 0 
        if ratio_pv >=0.6 :
            col_pv =COLOR_GREEN 
        elif ratio_pv >=0.3 :
            col_pv =COLOR_YELLOW 
        else :
            col_pv =COLOR_RED 
        if ratio_mana >=0.6 :
            col_mana =COLOR_CYAN 
        elif ratio_mana >=0.3 :
            col_mana =COLOR_BLUE 
        else :
            col_mana =COLOR_MAGENTA 
        print (COLOR_MAGENTA +"="*50 +COLOR_RESET )
        print (COLOR_CYAN +COLOR_BOLD +f"Héros : {j .nom } le {j .classe } // Niveau {j .niveau }"+COLOR_RESET )
        print (col_pv +"PV :"+COLOR_RESET ,col_pv +j .barre_vie ()+COLOR_RESET ,f"{j .pv }/{j .pv_max }")
        print (col_mana +"Mana :"+COLOR_RESET ,col_mana +j .barre_vie ()+COLOR_RESET ,f"{j .mana }/{j .mana_max }")
        print (f"ATQ : {j .attaque } DEF : {j .defense }")
        arme_nom =j .arme .nom if j .arme else "Aucune"
        relique_nom =j .relique .nom if j .relique else "Aucune"
        print (f"Arme : {arme_nom }")
        print (f"Relique: {relique_nom }")
        print (f"Potions : {j .potions } // Or : {j .gold }")
        if j .classe =="Necromancer"and j .invocation_squelette_tours >0 :
            print (f"Invocation : Squelette actif ({j .invocation_squelette_tours } tour(s) restant(s))")
        self .afficher_statuts (j ,est_joueur =True )
        print (COLOR_MAGENTA +"="*50 +COLOR_RESET )

        # ------------------ Combat ------------------
    @staticmethod 
    def calculer_degats (base_atq :int ,base_def :int )->int :
        base =base_atq -base_def 
        variance =random .randint (-1 ,2 )
        return max (1 ,base +variance )

    def appliquer_degats_joueur (self ,degats :int )->int :
        j =self .joueur 
        if j is None :
            return 0 
        effective_def =j .def_effective ()
        dodge_chance =min (0.25 ,0.02 *effective_def )
        if random .random ()<dodge_chance :
            print ("Tu esquives habilement l'attack !")
            return 0 
        j .pv -=degats 
        return degats 

        # --------- Système élémentaire ---------
    def appliquer_element (self ,degats :int ,ennemi :Enemy ,element :Optional [str ])->int :
        if element is None :
            return degats 
        mult =1.0 
        if element in ennemi .element_resistances :
            mult *=ennemi .element_resistances [element ]
        if element in ennemi .element_weaknesses :
            mult *=ennemi .element_weaknesses [element ]
        deg =int (degats *mult )
        if mult >1.0 :
            print (COLOR_YELLOW +"C'est super efficace !"+COLOR_RESET )
        elif mult <1.0 :
            print (COLOR_BLUE +"L'ennemi résiste à cet élément..."+COLOR_RESET )
        return max (1 ,deg )

    def attaque_joueur_sur_ennemi (self ,ennemi :Enemy ,base_atq :int ,element :str ="physique")->int :
        j =self .joueur 
        if j is None :
            return 0 
        degats =self .calculer_degats (base_atq ,ennemi .defense )
        if random .random ()<j .crit_chance ():
            degats =int (degats *1.8 )
            print (COLOR_YELLOW +"COUP CRITIQUE !!"+COLOR_RESET )
        degats =self .appliquer_element (degats ,ennemi ,element )
        ls =j .lifesteal ()
        if ls >0 :
            soin =int (degats *ls )
            if soin >0 :
                j .pv =min (j .pv_max ,j .pv +soin )
                print (f"Ta relique draine {soin } PV de l'ennemi.")
        ennemi .pv -=degats 
        if j .arme and j .arme .nom =="Dagues jumelles":
            if random .random ()<0.35 :
                ennemi .statuts .poison +=2 
                print (COLOR_GREEN +"Les dagues injectent un poison dans les veines de l'ennemi !"+COLOR_RESET )
        return degats 

        # ------------------ Tours de combat ------------------
    def tour_joueur (self ,ennemi :Enemy )->str :
        j =self .joueur 
        if j is None :
            return "mort"
        mort =j .appliquer_statuts ()
        if mort :
            print ("Les effets de statut ont eu raison de toi...")
            attendre_entree ()
            return "mort"
        if j .est_stun ():
            print ("Tu es étourdi et ne peux pas agir !")
            attendre_entree ()
            return "stun"
        while True :
            print ()
            print ("Ton action :")
            print (" 1) Attaquer")
            print (" 2) Défendre")
            print (f" 3) Pouvoir spécial ({j .pouvoir })")
            print (" 4) Utiliser une potion")
            choix =input (">> ").strip ()
            if choix =="1":
                atq_eff =j .atq_effective ()
                degats =self .attaque_joueur_sur_ennemi (ennemi ,atq_eff ,element ="physique")
                if j .classe =="Rogue"and random .random ()<0.25 :
                    ennemi .statuts .poison +=3 
                    print ("Tu empoisonnes l'ennemi !")
                elif j .classe =="Mage"and random .random ()<0.25 :
                    ennemi .statuts .brulure +=2 
                    print ("Tu enflammes l'ennemi !")
                clear_console ()
                print (f"Tu frappes {ennemi .nom } et infliges {degats } dégâts !")
                return "attack"
            if choix =="2":
                clear_console ()
                print ("Tu te prépares à encaisser le prochain coup (DEF x2 ce tour).")
                return "defense"
            if choix =="3":
                res =self .choisir_pouvoir_et_utiliser (j ,ennemi )
                if res is None :
                    continue 
                msg ,degats =res 
                clear_console ()
                print (msg )
                if degats >0 :
                    print (f"Tu infliges {degats } dégâts à {ennemi .nom } !")
                return "power"
            if choix =="4":
                if j .potions <=0 :
                    clear_console ()
                    print ("Tu n'as plus de potion...")
                    continue 
                self .utiliser_potion ()
                return "potion"
            print ("Choix invalide.")
            attendre_entree ()

            # Sous-menu de pouvoirs par classe
    def choisir_pouvoir_et_utiliser (self ,j :Player ,ennemi :Enemy ):
    # Necromancer : 2 sorts
        if j .classe =="Necromancer":
            while True :
                clear_console ()
                print ("=== Sorts de Necromancer ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Drain d'âme (5 mana)")
                print (" 2) Invocation de squelette (10 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =5 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Drain d'âme !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =10 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Invocation de squelette !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Warrior : 2 techniques
        if j .classe =="Warrior":
            while True :
                clear_console ()
                print ("=== Techniques du Warrior ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Coup puissant (3 mana)")
                print (" 2) Fracas de bouclier (4 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =3 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Coup puissant !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =4 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Fracas de bouclier !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Mage : 2 sorts
        if j .classe =="Mage":
            while True :
                clear_console ()
                print ("=== Arcanes du Mage ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Boule de feu (5 mana)")
                print (" 2) Nova de glace (6 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =5 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Boule de feu !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =6 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Nova de glace !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Rogue : 2 arts furtifs
        if j .classe =="Rogue":
            while True :
                clear_console ()
                print ("=== Arts furtifs du Rogue ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Attaque furtive (3 mana)")
                print (" 2) Pluie de dagues (4 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =3 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Attaque furtive !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =4 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Pluie de dagues !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Paladin : 2 pouvoirs sacrés
        if j .classe =="Paladin":
            while True :
                clear_console ()
                print ("=== Pouvoirs du Paladin ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Lumière sacrée (4 mana)")
                print (" 2) Bénédiction protectrice (5 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =4 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Lumière sacrée !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =5 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Bénédiction protectrice !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Ranger : 2 tirs
        if j .classe =="Ranger":
            while True :
                clear_console ()
                print ("=== Techniques du Ranger ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Tir précis (3 mana)")
                print (" 2) Tir multiple (4 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =3 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Tir précis !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =4 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Tir multiple !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Assassin de l'Ombre : 2 arts des ombres
        if j .classe =="Assassin de l'Ombre":
            while True :
                clear_console ()
                print ("=== Arts des ombres (Assassin) ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Lame spectrale (4 mana)")
                print (" 2) Disparition dans l'ombre (5 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =4 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Lame spectrale !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =5 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Disparition dans l'ombre !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Berserker : 2 attaques sauvages
        if j .classe =="Berserker":
            while True :
                clear_console ()
                print ("=== Rages du Berserker ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Frappe enragée (3 mana)")
                print (" 2) Rage incontrôlable (0 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =3 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Frappe enragée !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Bard : 2 chants
        if j .classe =="Bard":
            while True :
                clear_console ()
                print ("=== Chants du Bard ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Chant de bravoure (4 mana)")
                print (" 2) Ballade apaisante (5 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =4 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Chant de bravoure !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =5 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Ballade apaisante !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Monk : 2 techniques spirituelles
        if j .classe =="Monk":
            while True :
                clear_console ()
                print ("=== Arts martiaux spirituels (Monk) ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Paume vibrante (3 mana)")
                print (" 2) Méditation profonde (4 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =3 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Paume vibrante !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =4 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Méditation profonde !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

                # Summoner : 2 incantations
        if j .classe =="Summoner":
            while True :
                clear_console ()
                print ("=== Incantations de l'Summoner ===")
                print (f"Mana actuel : {j .mana }/{j .mana_max }")
                print (" 1) Salve astrale (6 mana)")
                print (" 2) Rempart des esprits (8 mana)")
                print (" 0) Annuler")
                choix =input (">> ").strip ()
                if choix =="0":
                    return None 
                if choix =="1":
                    cout =6 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Salve astrale !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =1 )
                if choix =="2":
                    cout =8 
                    if j .mana <cout :
                        print ("Pas assez de mana pour Rempart des esprits !")
                        attendre_entree ()
                        continue 
                    j .mana -=cout 
                    return self .utiliser_pouvoir_special (j ,ennemi ,ability_id =2 )
                print ("Choix invalide.")
                attendre_entree ()

        return None 

    def utiliser_pouvoir_special (self ,j :Player ,ennemi :Enemy ,ability_id :int =1 ):
    # Warrior
        if j .classe =="Warrior":
            if ability_id ==1 :
                atq_eff =j .atq_effective ()+4 
                degats =self .attaque_joueur_sur_ennemi (ennemi ,atq_eff ,element ="physique")
                if random .random ()<0.35 :
                    ennemi .statuts .stun +=1 
                    print ("Ton coup puissant étourdit l'ennemi !")
                return "Coup puissant !!",degats 
            if ability_id ==2 :
                degats =self .calculer_degats (j .atq_effective (),ennemi .defense )
                degats =self .appliquer_element (degats ,ennemi ,"physique")
                ennemi .pv -=degats 
                ennemi .defense =max (0 ,ennemi .defense -2 )
                return "Fracas de bouclier ! Tu réduis la défense de l'ennemi.",degats 

                # Mage
        if j .classe =="Mage":
            if ability_id ==1 :
                base =j .attaque +random .randint (6 ,10 )
                degats =base 
                if random .random ()<j .crit_chance ():
                    degats =int (degats *1.8 )
                    msg ="Boule de feu CRITIQUE !!"
                else :
                    msg ="Tu lances une énorme boule de feu !!"
                degats =self .appliquer_element (degats ,ennemi ,"feu")
                ennemi .pv -=degats 
                ennemi .statuts .brulure +=3 
                print ("L'ennemi est enflammé par ta magie !")
                ls =j .lifesteal ()
                if ls >0 :
                    soin =int (degats *ls )
                    if soin >0 :
                        j .pv =min (j .pv_max ,j .pv +soin )
                return msg ,degats 
            if ability_id ==2 :
                base =j .attaque +random .randint (4 ,7 )
                degats =base 
                degats =self .appliquer_element (degats ,ennemi ,"glace")
                ennemi .pv -=degats 
                if random .random ()<0.4 :
                    ennemi .statuts .stun +=1 
                    msg ="Nova de glace ! L'ennemi est gelé sur place !"
                else :
                    msg ="Nova de glace ! L'ennemi est ralenti par le froid."
                ennemi .attaque =max (1 ,ennemi .attaque -1 )
                return msg ,degats 

                # Rogue
        if j .classe =="Rogue":
            if ability_id ==1 :
                atq_eff =j .atq_effective ()+2 
                degats =self .attaque_joueur_sur_ennemi (ennemi ,atq_eff ,element ="physique")
                if random .random ()<0.4 :
                    ennemi .statuts .poison +=2 
                    print ("Ton attack furtive empoisonne l'ennemi !")
                if random .random ()<0.2 :
                    ennemi .statuts .stun +=1 
                    print ("Tu surprends l'ennemi, il est étourdi !")
                return "Attaque furtive ! Tu vises un point faible.",degats 
            if ability_id ==2 :
                total =0 
                for _ in range (3 ):
                    d =self .calculer_degats (max (1 ,j .atq_effective ()-1 ),ennemi .defense )
                    d =self .appliquer_element (d ,ennemi ,"physique")
                    ennemi .pv -=d 
                    total +=d 
                ennemi .statuts .poison +=1 
                ennemi .statuts .brulure +=1 
                return "Pluie de dagues ! Tu lacères ton adversaire de tous côtés.",total 

                # Paladin
        if j .classe =="Paladin":
            if ability_id ==1 :
                soin =random .randint (10 ,16 )
                j .pv =min (j .pv_max ,j .pv +soin )
                degats =self .calculer_degats (j .atq_effective (),ennemi .defense )
                degats =self .appliquer_element (degats ,ennemi ,"sacre")
                ennemi .pv -=degats 
                return f"Lumière sacrée ! Tu te soignes de {soin } PV et infliges {degats } dégâts.",degats 
            if ability_id ==2 :
                soin =random .randint (8 ,14 )
                j .pv =min (j .pv_max ,j .pv +soin )
                j .defense +=2 
                return "Bénédiction protectrice ! Tu renforces ta défense et soignes tes blessures.",0 

                # Ranger
        if j .classe =="Ranger":
            if ability_id ==1 :
                base =j .atq_effective ()+random .randint (2 ,5 )
                degats =base 
                crit =j .crit_chance ()+0.15 
                if random .random ()<crit :
                    degats =int (degats *2.2 )
                    msg ="Tir précis CRITIQUE !!"
                else :
                    msg ="Tu décoches une flèche mortelle."
                degats =self .appliquer_element (degats ,ennemi ,"physique")
                ennemi .pv -=degats 
                return msg ,degats 
            if ability_id ==2 :
                d1 =self .calculer_degats (max (1 ,j .atq_effective ()-1 ),ennemi .defense )
                d2 =self .calculer_degats (max (1 ,j .atq_effective ()-1 ),ennemi .defense )
                d1 =self .appliquer_element (d1 ,ennemi ,"physique")
                d2 =self .appliquer_element (d2 ,ennemi ,"physique")
                total =d1 +d2 
                ennemi .pv -=total 
                return "Tir multiple ! Deux flèches frappent leur cible.",total 

                # Necromancer
        if j .classe =="Necromancer":
            if ability_id ==1 :
                base =j .attaque +random .randint (4 ,8 )
                degats =base 
                degats =self .appliquer_element (degats ,ennemi ,"ombre")
                ennemi .pv -=degats 
                soin =int (degats *0.7 )
                j .pv =min (j .pv_max ,j .pv +soin )
                return f"Drain d'âme ! Tu voles {soin } PV à {ennemi .nom }.",degats 
            if ability_id ==2 :
                if j .invocation_squelette_tours >0 :
                    return "Tu as déjà un squelette invoqué !",0 
                j .invocation_squelette_tours =3 
                return "Tu invoques un squelette des catacombes pour combattre à tes côtés !",0 

                # Assassin de l'Ombre
        if j .classe =="Assassin de l'Ombre":
            if ability_id ==1 :
                base =j .atq_effective ()+random .randint (3 ,6 )
                degats =self .calculer_degats (base ,ennemi .defense )
                if random .random ()<j .crit_chance ()+0.1 :
                    degats =int (degats *2.0 )
                    msg ="Lame spectrale CRITIQUE !"
                else :
                    msg ="Tu frappes depuis les ténèbres avec ta lame spectrale."
                degats =self .appliquer_element (degats ,ennemi ,"ombre")
                ennemi .pv -=degats 
                return msg ,degats 
            if ability_id ==2 :
                j .bonus_critique +=0.15 
                j .defense +=1 
                return "Tu te fonds dans l'ombre, tes prochains coups seront plus meurtriers.",0 

                # Berserker
        if j .classe =="Berserker":
            if ability_id ==1 :
                base =j .atq_effective ()+random .randint (4 ,7 )
                degats =self .calculer_degats (base ,ennemi .defense )
                degats =self .appliquer_element (degats ,ennemi ,"physique")
                ennemi .pv -=degats 
                recul =max (1 ,int (degats *0.15 ))
                j .pv =max (1 ,j .pv -recul )
                return f"Frappe enragée ! Tu infliges {degats } dégâts mais subis {recul } PV de recul.",degats 
            if ability_id ==2 :
                j .attaque +=2 
                j .defense =max (0 ,j .defense -1 )
                j .pv =min (j .pv_max ,j .pv +5 )
                return "Rage incontrôlable ! ATQ +2, DEF -1, tu regagnes un peu de PV.",0 

                # Bard
        if j .classe =="Bard":
            if ability_id ==1 :
                j .attaque +=1 
                j .defense +=1 
                return "Chant de bravoure ! Tes statistiques offensives et défensives augmentent légèrement.",0 
            if ability_id ==2 :
                soin =random .randint (10 ,16 )
                j .pv =min (j .pv_max ,j .pv +soin )
                j .statuts .poison =0 
                j .statuts .brulure =0 
                j .statuts .stun =0 
                return f"Ballade apaisante ! Tu récupères {soin } PV et tes altérations d'état disparaissent.",0 

                # Monk
        if j .classe =="Monk":
            if ability_id ==1 :
                base =j .atq_effective ()+random .randint (2 ,4 )
                degats =self .calculer_degats (base ,ennemi .defense )
                degats =self .appliquer_element (degats ,ennemi ,"sacre")
                ennemi .pv -=degats 
                if random .random ()<0.35 :
                    ennemi .statuts .stun +=1 
                    return "Paume vibrante ! L'ennemi est frappé et étourdi.",degats 
                return "Paume vibrante ! Tu frappes les points vitaux de ton adversaire.",degats 
            if ability_id ==2 :
                soin =random .randint (8 ,12 )
                mana_gain =random .randint (5 ,8 )
                j .pv =min (j .pv_max ,j .pv +soin )
                j .mana =min (j .mana_max ,j .mana +mana_gain )
                j .statuts .poison =max (0 ,j .statuts .poison -1 )
                j .statuts .brulure =max (0 ,j .statuts .brulure -1 )
                return f"Méditation profonde ! Tu récupères {soin } PV et {mana_gain } mana.",0 

                # Summoner
        if j .classe =="Summoner":
            if ability_id ==1 :
            # Salve astrale : dégâts magiques multi-éléments
                base =j .attaque +random .randint (8 ,14 )
                degats =self .appliquer_element (base ,ennemi ,"ombre")
                ennemi .pv -=degats 
                return "Salve astrale ! Une pluie d'énergie frappe ton ennemi.",degats 
            if ability_id ==2 :
            # Rempart des esprits : bouclier défensif
                j .defense +=2 
                j .pv =min (j .pv_max ,j .pv +6 )
                return "Rempart des esprits ! Ta défense augmente et les esprits te soignent un peu.",0 

                # fallback
        degats =self .attaque_joueur_sur_ennemi (ennemi ,j .atq_effective (),element ="physique")
        return "Pouvoir mystérieux...",degats 

    def utiliser_potion (self )->None :
        j =self .joueur 
        if j is None :
            return 
        while True :
            clear_console ()
            print (f"Tu as {j .potions } potion(s).")
            print ("Quel type de potion veux-tu utiliser ?")
            print (" 1) Potion de soin (beaucoup de PV)")
            print (" 2) Potion de mana (beaucoup de mana)")
            print (" 3) Potion mixte (un peu de PV et un peu de mana)")
            choix_p =input (">> ").strip ()
            if choix_p =="1":
                soin =random .randint (14 ,20 )
                j .pv =min (j .pv_max ,j .pv +soin )
                j .potions -=1 
                clear_console ()
                print (f"Tu bois une potion de soin et récupères {soin } PV !")
                break 
            if choix_p =="2":
                mana_gain =random .randint (10 ,16 )
                j .mana =min (j .mana_max ,j .mana +mana_gain )
                j .potions -=1 
                clear_console ()
                print (f"Tu bois une potion de mana et récupères {mana_gain } mana !")
                break 
            if choix_p =="3":
                soin =random .randint (7 ,11 )
                mana_gain =random .randint (5 ,9 )
                j .pv =min (j .pv_max ,j .pv +soin )
                j .mana =min (j .mana_max ,j .mana +mana_gain )
                j .potions -=1 
                clear_console ()
                print (f"Tu bois une potion mixte et récupères {soin } PV et {mana_gain } mana !")
                break 
            print ("Choix de potion invalide.")
            attendre_entree ()

    def squelette_attaque (self ,ennemi :Enemy )->None :
        j =self .joueur 
        if j is None :
            return 
        if j .invocation_squelette_tours <=0 :
            return 
        base_atq =max (1 ,j .attaque -1 )
        degats =self .calculer_degats (base_atq ,ennemi .defense )
        degats =self .appliquer_element (degats ,ennemi ,"physique")
        ennemi .pv -=degats 
        print (f"Ton squelette invoqué frappe {ennemi .nom } et inflige {degats } dégâts !")
        j .invocation_squelette_tours -=1 
        if j .invocation_squelette_tours <=0 :
            print ("Ton squelette se désagrège en poussière d'os...")

    def ennemi_competence_speciale (self ,ennemi :Enemy )->None :
        j =self .joueur 
        if j is None :
            return 
            # Boss plus dangereux
        if "Seigneur"in ennemi .nom or "Champion"in ennemi .nom or "Reine"in ennemi .nom :
            print (COLOR_RED +f"{ennemi .nom } déclenche une COMPÉTENCE ULTIME !"+COLOR_RESET )
            degats_base =int (ennemi .attaque *1.8 )
            degats =self .appliquer_degats_joueur (degats_base )
            if degats >0 :
                print (f"Tu subis {degats } dégâts dévastateurs !")
            if random .random ()<0.4 :
                j .statuts .stun +=1 
                print ("La puissance du coup t'étourdit !")
            return 
            # Enemies normaux : buff ou débuff
        choix =random .choice (["rage","malédiction"])
        if choix =="rage":
            print (f"{ennemi .nom } entre en rage ! Son attaque augmente.")
            ennemi .attaque +=2 
        else :
            print (f"{ennemi .nom } murmure une malédiction...")
            j .attaque =max (1 ,j .attaque -1 )
            print ("Tu te sens affaibli : ATQ -1.")

            #------------------ attack ennemi ------------------
    def tour_ennemi (self ,ennemi :Enemy ,action_joueur :str )->None :
        j =self .joueur 
        if j is None :
            return 
        mort =ennemi .appliquer_statuts ()
        if mort :
            return 
        if ennemi .est_stun ():
            print (f"{ennemi .nom } est étourdi et ne peut pas agir !")
            return 
            # Chance de compétence spéciale
        if random .random ()<0.20 :
            self .ennemi_competence_speciale (ennemi )
            return 
        effective_def =j .def_effective ()
        if action_joueur =="defense":
            effective_def *=2 
        degats_base =self .calculer_degats (ennemi .attaque ,effective_def )
        degats =self .appliquer_degats_joueur (degats_base )
        if degats >0 :
            print (f"{ennemi .nom } t'attaque et inflige {degats } dégâts !")
        if random .random ()<0.15 :
            j .statuts .poison +=2 
            print ("L'attack de l'ennemi t'empoisonne !")
        elif random .random ()<0.15 :
            j .statuts .brulure +=2 
            print ("L'attack de l'ennemi te brûle !")

            # ------------------ Cards ------------------
    def tirer_cartes (self ,n :int =3 )->List [Card ]:
        cartes :List [Card ]=[]
        j =self .joueur 
        for _ in range (n ):
            r =random .random ()
            if r <0.60 :
                rarete_visee ="Common"
            elif r <0.85 :
                rarete_visee ="Rare"
            elif r <0.97 :
                rarete_visee ="Epic"
            else :
                rarete_visee ="Legendary"
            cand =[c for c in CARDS_POOL if c .rarete ==rarete_visee ]
            if j is not None :
                cand =[c for c in cand if (c .classes_autorisees is None or j .classe in c .classes_autorisees )]
            if not cand :
            # Fallback : cartes génériques de cette rareté, ou tout le pool
                cand =[c for c in CARDS_POOL if c .rarete ==rarete_visee and c .classes_autorisees is None ]or CARDS_POOL 
            cartes .append (random .choice (cand ))
        return cartes 

    def appliquer_carte (self ,carte :Card )->None :
        j =self .joueur 
        if j is None :
            return 
        j .pv_max +=carte .bonus_pv_max 
        j .attaque +=carte .bonus_attaque 
        j .defense +=carte .bonus_defense 
        j .mana_max +=carte .bonus_mana_max 
        j .potions +=carte .bonus_potions 
        j .bonus_critique +=carte .bonus_critique 
        if carte .bonus_pv_max >0 :
            j .pv +=carte .bonus_pv_max 
        j .pv =min (j .pv_max ,j .pv )
        j .mana =min (j .mana_max ,j .mana )
        #------------------ cartes recompenses ------------------
    def choix_cartes_apres_combat (self )->None :
        j =self .joueur 
        if j is None :
            return 
        cartes =self .tirer_cartes (3 )
        while True :
            clear_console ()
            print ("===== RÉCOMPENSE : CHOIX DE CARTE =====")
            for i ,c in enumerate (cartes ,start =1 ):
                restriction =""
                if c .classes_autorisees is not None :
                    restriction =" (spécifique)"
                print (f" {i }) [{c .rarete }] {c .nom }{restriction } - {c .description }")
            print (" 0) Ne prendre aucune carte (pas recommandé)")
            choix =input ("Choisis une carte (0-3) : ").strip ()
            if choix =="0":
                print ("Tu ignores ces pouvoirs... choix risqué.")
                attendre_entree ()
                return 
            try :
                idx =int (choix )-1 
            except ValueError :
                print ("Choix invalide.")
                attendre_entree ()
                continue 
            if 0 <=idx <len (cartes ):
                carte =cartes [idx ]
                clear_console ()
                print (f"Tu choisis la carte [{carte .rarete }] {carte .nom } !")
                self .appliquer_carte (carte )
                attendre_entree ()
                return 
            print ("Choix invalide.")
            attendre_entree ()

            # ------------------ Résolution de combat ------------------
    def gagner_recompenses (self ,ennemi :Enemy )->None :
        j =self .joueur 
        if j is None :
            return 
        gold_gagne =random .randint (*ennemi .gold_range )
        xp_gagne =random .randint (*ennemi .xp_range )
        if gold_gagne >0 :
            j .gold +=gold_gagne +1 
            j .or_gagne_total +=gold_gagne 
            print (f"Tu ramasses {gold_gagne } pièces d'or.")
        j .xp +=xp_gagne 
        # Le mana se régénère à la fin du combat
        j .mana =j .mana_max 
        print ("Ton mana se régénère entièrement après le combat.")
        # Choix d'une carte de progression
        self .choix_cartes_apres_combat ()

        #------------------ menu de combat ------------------
    def combat (self ,ennemi :Enemy )->bool :
        j =self .joueur 
        if j is None :
            return False 
        clear_console ()
        print ("-"*40 )
        print (COLOR_RED +f"Un {ennemi .nom } apparaît !"+COLOR_RESET )
        print ("-"*40 )
        while j .est_vivant ()and ennemi .est_vivant ():
            self .afficher_etat_joueur ()
            self .afficher_statuts (ennemi ,est_joueur =False )
            print (f"Ennemi : {ennemi .nom }")
            print ("PV ennemi :",ennemi .barre_vie (),f"{ennemi .pv }/{ennemi .pv_max }")
            action =self .tour_joueur (ennemi )
            if action =="mort":
                return False 
            if not ennemi .est_vivant ():
                print (f"Tu as vaincu {ennemi .nom } !")
                j .ennemis_tues +=1 
                self .gagner_recompenses (ennemi )
                attendre_entree ()
                return True 
            if j .classe =="Necromancer"and j .invocation_squelette_tours >0 and ennemi .est_vivant ():
                self .squelette_attaque (ennemi )
                if not ennemi .est_vivant ():
                    print (f"Ton squelette achève {ennemi .nom } !")
                    j .ennemis_tues +=1 
                    self .gagner_recompenses (ennemi )
                    attendre_entree ()
                    return True 
            self .tour_ennemi (ennemi ,action )
            if not j .est_vivant ():
                print ("Tu es tombé au combat...")
                attendre_entree ()
                return False 
            attendre_entree ()
            clear_console ()
        return j .est_vivant ()

        # ------------------ Boutique ------------------
    def boutique (self )->None :
        j =self .joueur 
        if j is None :
            return 
        while True :
            clear_console ()
            print (COLOR_YELLOW +"========== BOUTIQUE =========="+COLOR_RESET )
            print (f"Or actuel : {j .gold } pièces")
            print (" 0) Quitter la boutique")
            print (" 1) Potion de soin (+1) - 10 or")
            print (" 2) Augmenter l'attack (+1) - 25 or")
            print (" 3) Augmenter la défense (+1) - 25 or")
            print (" 4) Augmenter PV max (+5) - 30 or")
            choix =input (">> ").strip ()
            if choix =="0":
                break 
            if choix =="1":
                if j .gold <10 :
                    print ("Pas assez d'or !")
                else :
                    j .gold -=10 
                    j .potions +=1 
                    print ("Tu achètes une potion de soin.")
                attendre_entree ()
                continue 
            if choix =="2":
                if j .gold <25 :
                    print ("Pas assez d'or !")
                else :
                    j .gold -=25 
                    j .attaque +=1 
                    print ("Ton attack augmente de 1 ! (pour cette run)")
                attendre_entree ()
                continue 
            if choix =="3":
                if j .gold <25 :
                    print ("Pas assez d'or !")
                else :
                    j .gold -=25 
                    j .defense +=1 
                    print ("Ta défense augmente de 1 ! (pour cette run)")
                attendre_entree ()
                continue 
            if choix =="4":
                if j .gold <30 :
                    print ("Pas assez d'or !")
                else :
                    j .gold -=30 
                    j .pv_max +=5 
                    j .pv =j .pv_max 
                    print ("Tes PV max augmentent de 5 ! (pour cette run)")
                attendre_entree ()
                continue 
            print ("Choix invalide. Utilise 0 pour quitter ou 1-4 pour acheter.")
            attendre_entree ()

            # ------------------ Loot : weapons & relics ------------------
    def donner_arme_random (self )->None :
        j =self .joueur 
        if j is None :
            return 
        nouvelle =random .choice (WEAPONS [1 :])
        print (COLOR_YELLOW +f"Tu trouves une nouvelle arme : {nouvelle .nom } !"+COLOR_RESET )
        if nouvelle .description :
            print ("Description :",nouvelle .description )
        arme_actuelle =j .arme 
        if arme_actuelle :
            print ("Ton arme actuelle :",arme_actuelle .nom )
            if arme_actuelle .description :
                print ("Description actuelle :",arme_actuelle .description )
        if not j .armes :
            j .armes =[arme_actuelle ]if arme_actuelle else []
        while True :
            print ("Que veux-tu faire ?")
            print (" 1) Équiper immédiatement la nouvelle arme")
            print (" 2) Garder l'arme actuelle mais ajouter la nouvelle à l'inventaire")
            print (" 3) Laisser l'arme et continue ton chemin")
            choix =input (">> ").strip ()
            if choix =="1":
                j .armes .append (nouvelle )
                j .arme =nouvelle 
                print (f"Tu équipes {nouvelle .nom } !")
                break 
            if choix =="2":
                j .armes .append (nouvelle )
                print (f"Tu ranges {nouvelle .nom } dans ton inventaire.")
                break 
            if choix =="3":
                print ("Tu laisses l'arme derrière toi.")
                break 
            print ("Choix invalide, recommence.")

    def donner_relique_random (self )->None :
        j =self .joueur 
        if j is None :
            return 
        nouvelle =random .choice (RELICS )
        actuelle =j .relique 
        if actuelle is None :
            j .relique =nouvelle 
            print (f"Tu ressens un pouvoir ancien : tu obtiens la relique '{nouvelle .nom }'.")
            if nouvelle .description :
                print ("Description :",nouvelle .description )
            return 
        print (f"Tu découvres une nouvelle relique : {nouvelle .nom }")
        print ("Description nouvelle :",nouvelle .description or "???")
        print ("Relique actuelle :",actuelle .nom )
        print ("Description actuelle :",actuelle .description or "???")
        while True :
            print ("Que veux-tu faire ?")
            print (" 1) Remplacer la relique actuelle par la nouvelle")
            print (" 2) Garder la relique actuelle et laisser la nouvelle")
            choix =input (">> ").strip ()
            if choix =="1":
                j .relique =nouvelle 
                print (f"Tu remplaces ta relique par {nouvelle .nom }.")
                break 
            if choix =="2":
                print ("Tu décides de garder ta relique actuelle.")
                break 
            print ("Choix invalide.")

            # ------------------ Inventaire d'weapons ------------------
    def menu_armes (self )->None :
        j =self .joueur 
        if j is None :
            return 
        if not j .armes :
            print ("Tu n'as aucune arme dans ton inventaire.")
            attendre_entree ()
            return 
        while True :
            clear_console ()
            print ("====== INVENTAIRE D'ARMES ======")
            print ("(Choisis une arme à équiper)")
            for i ,arme in enumerate (j .armes ,start =1 ):
                marque =" [Équipée]"if j .arme is arme else ""
                print (f" {i }) {arme .nom }{marque }")
            print (" 0) Quitter l'inventaire")
            choix =input (">> ").strip ()
            if choix =="0":
                break 
            try :
                idx =int (choix )-1 
            except ValueError :
                print ("Choix invalide.")
                attendre_entree ()
                continue 
            if 0 <=idx <len (j .armes ):
                j .arme =j .armes [idx ]
                print (f"Tu équipes {j .armes [idx ].nom }.")
                attendre_entree ()
                break 
            print ("Choix invalide.")
            attendre_entree ()

            # ------------------ Evénements ------------------
    def evenement_tresor (self )->None :
        j =self .joueur 
        if j is None :
            return 
        clear_console ()
        print ("Tu trouves un petit coffre abandonné...")
        contenu =random .choice (["or","potion","arme","relique","rien"])
        if contenu =="or":
            gain =random .randint (10 ,25 )
            j .gold +=gain 
            j .or_gagne_total +=gain 
            print (f"Le coffre contient {gain } pièces d'or !")
        elif contenu =="potion":
            j .potions +=1 
            print ("Tu trouves une potion de soin !")
        elif contenu =="arme":
            self .donner_arme_random ()
        elif contenu =="relique":
            self .donner_relique_random ()
        else :
            print ("Le coffre est vide... dommage.")
        attendre_entree ()

    def evenement_feu_de_camp (self )->None :
        j =self .joueur 
        if j is None :
            return 
        clear_console ()
        print ("Tu arrives près d'un feu de camp mystérieux.")
        print ("Tu décides de te reposer un moment.")
        soin =int (j .pv_max *0.5 )
        mana_recup =int (j .mana_max *0.6 )
        j .pv =min (j .pv_max ,j .pv +soin )
        j .mana =min (j .mana_max ,j .mana +mana_recup )
        print (f"Tu récupères {soin } PV et {mana_recup } mana.")
        attendre_entree ()

    def evenement_mystere (self )->None :
        j =self .joueur 
        if j is None :
            return 
        clear_console ()
        print ("Tu sens une étrange présence... Un événement mystère se déclenche !")
        attendre_entree ()
        effet =random .choice (["bon","bon","mauvais","mixte","arme","relique"])
        if effet =="arme":
            self .donner_arme_random ()
            return 
        if effet =="relique":
            self .donner_relique_random ()
            return 
        if effet =="bon":
            choix =random .choice (["hp","attack","or"])
            if choix =="hp":
                bonus =8 
                j .pv_max +=bonus 
                j .pv +=bonus 
                print (f"Une énergie bienveillante t'entoure. Tes PV max augmentent de {bonus } !")
            elif choix =="attack":
                j .attaque +=2 
                print ("Tu ressens une nouvelle force dans ton bras : ATQ +2 !")
            else :
                gain =30 
                j .gold +=gain 
                j .or_gagne_total +=gain 
                print (f"Tu trouves un tas d'or spectral : +{gain } or !")
            attendre_entree ()
            return 
        if effet =="mauvais":
            malus =random .choice (["hp","attack"])
            if malus =="hp":
                perte =max (1 ,int (j .pv_max *0.15 ))
                j .pv_max -=perte 
                j .pv =max (1 ,j .pv -perte )
                print (f"Une malédiction ronge ton corps : -{perte } PV max...")
            else :
                j .attaque =max (1 ,j .attaque -1 )
                print ("Un froid étrange affaiblit tes muscles : ATQ -1.")
            attendre_entree ()
            return 
        print ("Un pacte étrange... Tu gagnes en puissance mais tu perds aussi quelque chose.")
        j .attaque +=2 
        perte =max (1 ,int (j .pv_max *0.1 ))
        j .pv_max -=perte 
        if j .pv >j .pv_max :
            j .pv =j .pv_max 
        print (f"ATQ +2 mais -{perte } PV max.")
        attendre_entree ()

        # ------------------ Difficulté & zones ------------------
    @staticmethod 
    def facteur_difficulte (etage :int )->float :
        palier =max (0 ,(etage -1 )//10 )
        return 1.0 +palier *0.25 

    @staticmethod 
    def zone_pour_etage (etage :int )->Dict :
        for zone in ZONES :
            if zone ['debut']<=etage <=zone ['fin']:
                return zone 
        return ZONES [-1 ]

    @staticmethod 
    def est_etage_boss (etage :int )->bool :
        return etage %10 ==0 

    def choisir_chemins (self ,etage :int )->List [str ]:
        chemins =["combat","combat"]
        proba_shop =0.25 +self .meta .bonus_chance_shop *0.05 
        proba_mystere =0.10 +self .meta .bonus_chance_mystere *0.04 
        if random .random ()<proba_shop :
            idx =random .randint (0 ,len (chemins )-1 )
            chemins [idx ]="shop"
        if random .random ()<proba_mystere :
            indices_dispo =[i for i ,c in enumerate (chemins )if c =="combat"]
            if indices_dispo :
                idx =random .choice (indices_dispo )
                chemins [idx ]="mystere"
        if "combat"not in chemins :
            idx =random .randint (0 ,len (chemins )-1 )
            chemins [idx ]="combat"
        return chemins 

    @staticmethod 
    def decrire_chemin (chemin_type :str )->str :
        if chemin_type =="combat":
            return COLOR_RED +"Combat"+COLOR_RESET 
        if chemin_type =="shop":
            return COLOR_YELLOW +"Boutique"+COLOR_RESET 
        if chemin_type =="mystere":
            return COLOR_BLUE +"? Événement mystère ?"+COLOR_RESET 
        return "Inconnu"

        # ------------------ Etages ------------------
    def etage_roguelike (self ,etage :int )->bool :
        j =self .joueur 
        if j is None :
            return False 
        zone =self .zone_pour_etage (etage )
        clear_console ()
        j .etages_parcourus =max (j .etages_parcourus ,etage )
        print ("#"*50 )
        print (COLOR_CYAN +f"ETAGE {etage } - Zone : {zone ['name']}"+COLOR_RESET )
        print ("#"*50 )
        diff =self .facteur_difficulte (etage )
        if self .est_etage_boss (etage ):
            boss_data =random .choice (zone ['bosses']).copy ()
            # Exemple simple de résistances/faiblesses selon le boss
            resist ={}
            weak ={}
            if "Os"in boss_data ['name']:
                resist ={"physique":0.8 ,"feu":0.5 }
                weak ={"glace":1.4 }
            elif "Forêt"in boss_data ['name']or "Ent"in boss_data ['name']:
                resist ={"glace":0.7 }
                weak ={"feu":1.5 }
            elif "Runique"in boss_data ['name']or "Cristal"in boss_data ['name']:
                resist ={"sacre":0.7 }
                weak ={"ombre":1.4 }
            ennemi =Enemy (
            nom =boss_data ['name'],
            pv =int (boss_data ['hp']*diff ),
            pv_max =int (boss_data ['hp']*diff ),
            attaque =int (boss_data ['attack']*diff ),
            defense =max (1 ,int (boss_data ['defense']+(diff -1 )*4 )),
            mana =0 ,
            mana_max =0 ,
            statuts =Status (),
            gold_range =boss_data ['gold'],
            xp_range =boss_data ['xp'],
            element_resistances =resist ,
            element_weaknesses =weak ,
            )
            print (COLOR_RED +"Un puissant boss se dresse sur ton chemin !"+COLOR_RESET )
            attendre_entree ()
            victoire =self .combat (ennemi )
            if victoire :
                j .boss_tues +=1 
                clear_console ()
                print (f"Tu as vaincu {ennemi .nom } !")
                if etage <MAX_ETAGES :
                    print ("Tu ressens le monde qui change autour de toi...")
                    print ("Tu t'enfonces plus loin dans le danger.")
                    attendre_entree ()
                return True 
            return False 

        chemins =self .choisir_chemins (etage )
        while True :
            clear_console ()
            print ("#"*50 )
            print (COLOR_CYAN +f"ETAGE {etage } - Zone : {zone ['name']}"+COLOR_RESET )
            print ("#"*50 )
            self .afficher_etat_joueur ()
            print ("Chemins disponibles :")
            for i ,ch in enumerate (chemins ,start =1 ):
                print (f" {i }) {self .decrire_chemin (ch )}")
            print ("(Astuce : 1 ou 2 pour choisir un chemin, 'i' pour gérer tes weapons, 'admin' pour le menu secret.)")
            choix =input ("Vers quel chemin veux-tu aller ? (1/2) : ").strip ()
            if choix .lower ()=="i":
                self .menu_armes ()
                continue 
            if choix =="admin":
                self .menu_admin ()
                continue 
            if choix not in ("1","2"):
                print ("Choix invalide.")
                attendre_entree ()
                continue 
            idx =int (choix )-1 
            chemin_type =chemins [idx ]
            if chemin_type =="combat":
                ennemi_data =random .choice (zone ['ennemis']).copy ()
                resist ={}
                weak ={}
                if "Squelette"in ennemi_data ['name']:
                    resist ={"feu":0.5 ,"physique":0.9 }
                    weak ={"glace":1.3 }
                elif "Loup"in ennemi_data ['name']:
                    resist ={"physique":0.9 }
                    weak ={"feu":1.2 }
                elif "Mage"in ennemi_data ['name']:
                    resist ={"feu":0.8 ,"glace":0.8 }
                    weak ={"ombre":1.3 }
                ennemi =Enemy (
                nom =ennemi_data ['name'],
                pv =int (ennemi_data ['hp']*diff ),
                pv_max =int (ennemi_data ['hp']*diff ),
                attaque =int (ennemi_data ['attack']*diff ),
                defense =max (1 ,int (ennemi_data ['defense']+(diff -1 )*3 )),
                mana =0 ,
                mana_max =0 ,
                statuts =Status (),
                gold_range =ennemi_data ['gold'],
                xp_range =ennemi_data ['xp'],
                element_resistances =resist ,
                element_weaknesses =weak ,
                )
                return self .combat (ennemi )
            if chemin_type =="shop":
                self .boutique ()
                return True 
            if chemin_type =="mystere":
                self .evenement_mystere ()
                return True 

                # ------------------ Sanctuaire de la mort (Skill tree) ------------------
    def calcul_essence_gagnee (self )->int :
        j =self .joueur 
        if j is None :
            return 1 
        essence =0 
        essence +=j .etages_parcourus *2 
        essence +=j .ennemis_tues *1 
        essence +=j .boss_tues *5 
        essence +=j .or_gagne_total //50 
        return max (1 ,essence )

    def appliquer_talent (self ,talent_id :str ,node :Dict )->None :
        t_type =node .get ("type")
        cible =node .get ("cible")
        val =node .get ("valeur",0 )
        if t_type in ("stat","start_res","chance")and cible :
            actuel =getattr (self .meta ,cible ,0 )
            setattr (self .meta ,cible ,actuel +val )
            print (f"Le talent '{node ['name']}' renforce {cible } de {val }.")
        elif t_type =="unlock_class":
            classe =node .get ("cible")
            if classe and classe not in self .meta .classes_debloquees :
                self .meta .classes_debloquees .append (classe )
                print (f"Nouvelle classe débloquée : {classe } !")

    def death_shop (self )->None :
    # Sanctuaire = arbre de talents V17.2
        while True :
            clear_console ()
            print ("====== SANCTUAIRE DE LA MORT - ARBRE DE TALENTS ======")
            print (f"Essence d'âme disponible : {self .meta .essence }")
            print ()
            print ("Talents déjà débloqués :")
            if not self .meta .talents_debloques :
                print ("  Aucun pour le moment.")
            else :
                for tid in self .meta .talents_debloques :
                    node =SKILL_TREE .get (tid )
                    if node :
                        print (f"  - {node ['name']}")
            print ()
            # Construire la liste des talents achetables
            disponibles =[]
            for tid ,node in SKILL_TREE .items ():
                if tid in self .meta .talents_debloques :
                    continue 
                prereq =node .get ("prerequis",[])
                if all (p in self .meta .talents_debloques for p in prereq ):
                    disponibles .append ((tid ,node ))
            if not disponibles :
                print ("Aucun talent supplémentaire n'est actuellement disponible.")
                print ("Tape 0 pour quitter.")
            else :
                print ("Talents disponibles :")
                for i ,(tid ,node )in enumerate (disponibles ,start =1 ):
                    print (f" {i }) {node ['name']} ({node ['cout']} essence) - {node ['description']}")
            print (" 0) Quitter le sanctuaire")
            choix =input (">> ").strip ()
            if choix =="0":
                break 
            try :
                idx =int (choix )-1 
            except ValueError :
                print ("Choix invalide.")
                attendre_entree ()
                continue 
            if idx <0 or idx >=len (disponibles ):
                print ("Choix invalide.")
                attendre_entree ()
                continue 
            tid ,node =disponibles [idx ]
            cout =node .get ("cout",0 )
            if self .meta .essence <cout :
                print ("Pas assez d'essence d'âme...")
                attendre_entree ()
                continue 
            self .meta .essence -=cout 
            self .appliquer_talent (tid ,node )
            self .meta .talents_debloques .append (tid )
            self .meta .sauvegarder ()
            attendre_entree ()

            # ------------------ Menu admin secret (amélioré) ------------------
    def menu_admin (self )->None :
        while True :
            clear_console ()
            print ("===== MENU ADMIN (DEBUG) =====")
            print ("ATTENTION : réservé aux tests. Utilise avec précaution.")
            print ()
            print ("[MÉTA-PROGRESSION]")
            print (f"  Essence actuelle : {self .meta .essence }")
            print (f"  Classes débloquées : {', '.join (self .meta .classes_debloquees )}")
            print ()
            print (" 1) +100 essence d'âme")
            print (" 2) Débloquer toutes les classes")
            print (" 3) Réinitialiser entièrement la méta-progression")
            print ()
            print ("[RUN ACTUELLE]")
            if self .joueur is not None :
                print (f"  Joueur : {self .joueur .nom } ({self .joueur .classe }) - PV {self .joueur .pv }/{self .joueur .pv_max }, Mana {self .joueur .mana }/{self .joueur .mana_max }")
                print (" 4) Donner 999 or au joueur")
                print (" 5) Soigner entièrement le joueur (PV/Mana)")
            else :
                print ("  Aucun joueur actif (lance une run pour débloquer ces options).")
            print ()
            print ("[DIVERS]")
            print (" 6) Afficher le détail complet de la méta (debug)")
            print (" 0) Quitter le menu admin")
            choix =input (">> ").strip ()
            if choix =="0":
                break 
            if choix =="1":
                self .meta .essence +=100 
                self .meta .sauvegarder ()
                print ("+100 essence ajoutée.")
                attendre_entree ()
                continue 
            elif choix =="2":
                for infos in PLAYER_CLASSES .values ():
                    nom_classe =infos ["name"]
                    if nom_classe not in self .meta .classes_debloquees :
                        self .meta .classes_debloquees .append (nom_classe )
                self .meta .sauvegarder ()
                print ("Toutes les classes sont maintenant débloquées.")
                attendre_entree ()
                continue 
            elif choix =="3":
                confirm =input ("Es-tu sûr de vouloir TOUT réinitialiser ? (oui/non) : ").strip ().lower ()
                if confirm =="oui":
                    filename =self .meta .filename 
                    self .meta =Meta ()
                    self .meta .filename =filename 
                    self .meta .sauvegarder ()
                    print ("Meta-progression réinitialisée.")
                else :
                    print ("Réinitialisation annulée.")
                attendre_entree ()
                continue 
            elif choix =="4"and self .joueur is not None :
                self .joueur .gold +=999 
                print ("Le joueur reçoit 999 or.")
                attendre_entree ()
                continue 
            elif choix =="5"and self .joueur is not None :
                self .joueur .pv =self .joueur .pv_max 
                self .joueur .mana =self .joueur .mana_max 
                print ("Le joueur est entièrement soigné.")
                attendre_entree ()
                continue 
            elif choix =="6":
                clear_console ()
                print ("===== DÉTAIL DE LA MÉTA =====")
                print (f"Essence : {self .meta .essence }")
                print (f"PV bonus : {self .meta .pv_bonus }")
                print (f"ATQ bonus : {self .meta .attaque_bonus }")
                print (f"DEF bonus : {self .meta .defense_bonus }")
                print (f"Mana bonus : {self .meta .mana_bonus }")
                print (f"Or de départ : {self .meta .or_debut }")
                print (f"Potions de départ : {self .meta .potions_debut }")
                print (f"Bonus chance shop : {self .meta .bonus_chance_shop }")
                print (f"Bonus chance mystère : {self .meta .bonus_chance_mystere }")
                print (f"Talents débloqués : {', '.join (self .meta .talents_debloques )if self .meta .talents_debloques else 'aucun'}")
                attendre_entree ()
                continue 
            print ("Choix invalide.")
            attendre_entree ()

            # ------------------ Une run ------------------
    def une_run (self )->None :
        self .creer_joueur ()
        j =self .joueur 
        if j is None :
            return 
        etage =1 
        while j .est_vivant ()and etage <=MAX_ETAGES :
            succes_etage =self .etage_roguelike (etage )
            if not succes_etage :
                break 
            etage +=1 
            clear_console ()
        clear_console ()
        if j .est_vivant ()and etage >MAX_ETAGES :
            print ("INCROYABLE ! Tu as survécu à toutes les zones du donjon !")
            print ("Les catacombes se taisent... pour l'instant.")
        else :
            print ("Ta run se termine ici... Mais la mort n'est qu'un nouveau départ.")
        essence_gagnee =self .calcul_essence_gagnee ()
        if j .boss_tues >=1 :
            self .meta .debloquer_succes ('premier_boss')
        if j .ennemis_tues >=20 :
            self .meta .debloquer_succes ('tueur_de_monstres')
        if j .etages_parcourus >=10 :
            self .meta .debloquer_succes ('explorateur')
        print (f"Pendant cette run, tu as parcouru {j .etages_parcourus } étages,")
        print (f"vaincu {j .ennemis_tues } ennemis et {j .boss_tues } boss.")
        print (f"Tu as gagné {essence_gagnee } essence d'âme.")
        self .meta .essence +=essence_gagnee 
        self .meta .sauvegarder ()
        attendre_entree ()

        # ------------------ Menu principal ------------------
    def afficher_succes (self )->None :
        clear_console ()
        print ("===== SUCCÈS DÉBLOQUÉS =====")
        if not self .meta .succes :
            print ("Aucun succès débloqué pour le moment.")
        else :
            for cle ,data in self .meta .succes .items ():
                print (f"- {data .get ('description',cle )}")
        attendre_entree ()

    def afficher_features (self )->None :
        clear_console ()
        print ("===== RÉSUMÉ DES FONCTIONNALITÉS =====")
        print ("- Roguelike à étages avec 3 zones (Catacombs, Cursed Forest, Runic Citadel).")
        print ("- Système de combat au tour par tour avec statuts (poison, brûlure, étourdissement).")
        print ("- Armes et relics avec bonus, coups critiques et vol de vie.")
        print ("- Meta-progression avec essence d'âme et arbre de talents permanent.")
        print ("- Classes jouables avec pouvoirs spéciaux (Warrior, Mage, Rogue et classes avancées à débloquer).")
        print ("- Système de cartes de progression après chaque combat, avec certaines cartes spécifiques à une classe.")
        print ("- Événements : trésors, feu de camp, événements mystère.")
        print ("- Menu admin secret pour aider au test (tape 'admin' dans certains menus).")
        attendre_entree ()

    def main_menu (self )->None :
        while True :
            clear_console ()
            print (COLOR_MAGENTA +"="*30 +COLOR_RESET )
            print (COLOR_BOLD +" ROGUELIKE DES CATACOMBES"+COLOR_RESET )
            print (" V18 - Édition Roguelike ASCII")
            print (COLOR_MAGENTA +"="*30 +COLOR_RESET )
            print (f"Essence d'âme actuelle : {self .meta .essence }")
            print (" 1) Lancer une nouvelle run")
            print (" 2) Ouvrir le Sanctuaire de la Mort (arbre de talents)")
            print (" 3) Voir les succès et quitter le jeu")
            print (" 4) Voir un résumé des fonctionnalités")
            choix =input (">> ").strip ()
            if choix =="admin":
                self .menu_admin ()
                continue 
            if choix =="1":
                self .une_run ()
                continue 
            if choix =="2":
                self .death_shop ()
                continue 
            if choix =="3":
                self .afficher_succes ()
                clear_console ()
                print ("Merci d'avoir joué à ce roguelike ASCII !")
                break 
            if choix =="4":
                self .afficher_features ()
                continue 
            print ("Choix invalide.")
            attendre_entree ()


def main ():
    game =Game ()
    game .main_menu ()


if __name__ =="__main__":
    main ()
