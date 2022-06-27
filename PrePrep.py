import random
import discord


playingList = [
    "Call of Duty®: WWII",
    "NEKOPARA Vol. 3",
    "PlanetSide 2",
    "Rainbow Six Vegas",
    "Ready or Not",
    "Victory is our tradition",
    "Hell awaits you",
    "Wenfishing",
    "Tactical Superiority",
    "Walking Simulator",
    "Soap trusted you",
]

watchingList = [
    "The Echoes of Vanu",
    "The Idolm@ster",
    "The Rise of Octavian",
    "yes",
    "Your Lie in April",
    "Violet Evergarden",
    "Kiss x Sis",
    "Rainbow Derp: Siege",
    "The Roman Civil War",
    "Skyfall on Auraxis",
    "Nekopara",
]

listeningList = [
    "Delet This Nahui",
    "Rave or Riot",
    "Sapsan",
    "ナナイロ EveryDay",
    "Ange Du Blanc Pur",
    "Davay - Critikal",
    "XI - Aragami",
    "World Fragments II",
    "Murka (Refix 2018)",
    "Erika",
]

streamingList =[
    "Mogu Mogu?",
    "Kalashnikov Theft",
    "The fall of SPQR",
    "No Russian speedrun",
    "They're in the attic",
    "sbeve",
    "HESHed and A2G'd",
    "G15 Error bad",
    "lol combined arms",
    "maStHEaD kIllS a2G",
    "G15Side 2",
    "CheeseSide 2",
    "FlakSide 2",
    "AoESide 2",
    "hehe striker valkyrie",
    "Nerf VS reeeeeeeee",
    "Suck my nuts",
    "Drink Pee in the NC",
    "mmm tasty sand",
    "give me nanites",
]


trivt_list = {
    1: {"question": "Which of the four lords in *Resident Evil: Village* is the most dangerous according to The Duke?", 
    "ans1": "Alcina Dimitrescu", "ans2": "Donna Beneviento", "ans3": "Salvatore Moreau", "ans4": "Karl Heisenberg", "answer": "4"},
    2: {"question": "In *Resident Evil 6*, which final boss does the player encounter in Chris Redfield's campaign?", 
    "ans1": "Derek C. Simmons", "ans2": "HAOS", "ans3": "Ustanak", "ans4": "Albert Wesker", "answer": "2"},
    3: {"question": "In *Undertale*, who was Flowey prior to becoming a flower?", 
    "ans1": "Asriel Dreemurr", "ans2": "Alphys", "ans3": "Asgore Dreemurr", "ans4": "Sans", "answer": "1"},
    4: {"question": "Which two characters were turned into stone statues in Chapter 2 of *Deltarune*?", 
    "ans1": "Susie and Kris", "ans2": "Lancer and Rouxls Kaard", "ans3": "King and Queen", "ans4": "Noelle and Berdly", "answer": "2"},
    5: {"question": "What is the name of the patient the player usually operates on in *Surgeon Simulator*?", 
    "ans1": "Bob", "ans2": "Nigel", "ans3": "Kurt", "ans4": "Madison", "answer": "1"},
    6: {"question": "In *Tom Clancy's Rainbow Six Siege*, which operator CANNOT use the M870 Shotgun?", 
    "ans1": "Bandit", "ans2": "Recruit (Defense)", "ans3": "Kapkan", "ans4": "Jäger", "answer": "3"},
    7: {"question": "How many bits are there in a byte?", 
    "ans1": "4 bits", "ans2": "8 bits", "ans3": "32 bits", "ans4": "64 bits", "answer": "2"},
    8: {"question": "Which of the following is a cryptographic hash function?", 
    "ans1": "MD5", "ans2": "DSS", "ans3": "RSA", "ans4": "SHA", "answer": "4"},
    9: {"question": "Which of the following weapons can you aim down sights (ADS) with in *Counter Strike: Global Offensive*?", 
    "ans1": "Negev", "ans2": "SCAR-20", "ans3": "P90", "ans4": "M249", "answer": "2"},
    10: {"question": "Which of the following prisons is NOT a Transport Prison in *The Escapists 2*?", 
    "ans1": "Cougar Creek Railroad", "ans2": "H.M.S Orca", "ans3": "Air Force Con", "ans4": "U.S.S Anomaly", "answer": "4"},
    11: {"question": "What is Fool's Gold also known as?", 
    "ans1": "Ferrite", "ans2": "Granite", "ans3": "Pyrite", "ans4": "Aurite", "answer": "3"},
    12: {"question": "Which of the following elements is a halogen?", 
    "ans1": "Oxygen", "ans2": "Astatine", "ans3": "Strontium", "ans4": "Tungsten", "answer": "2"},
    13: {"question": "In *PlanetSide 2*, which Lightning tank cannon is capable of killing standard infantry using flak armour with a single direct hit?", 
    "ans1": "L100 Python AP", "ans2": "L100 Python HEAT", "ans3": "L100 Python HESH", "ans4": "C75 Viper", "answer": "3"},
    14: {"question": "Which of the following is NOT a sidearm in *Tom Clancy's Rainbow Six Siege*?", 
    "ans1": "P10 RONI", "ans2": "P12", "ans3": "SDP 9mm", "ans4": "SMG-11", "answer": "1"},
    15: {"question": "What is the term used when referring to the production and behaviour of materials at very low temperatures?", 
    "ans1": "Cryonics", "ans2": "Cryostasis", "ans3": "Cryoablation", "ans4": "Cryogenics", "answer": "4"},
    16: {"question": "\"Lesion\" Liu Tze Long appears in *Tom Clacncy's Ghost Recon* as mission control under a call sign. What is this call sign?", 
    "ans1": "Overlord", "ans2": "R6 Actual", "ans3": "Rainbow Six", "ans4": "Lesion", "answer": "2"},
    17: {"question": "Which of the following titles did the Roman general Gaius Julius Caesar NOT hold?", 
    "ans1": "Dictator", "ans2": "Princeps Senatus", "ans3": "Pontifex Maximus", "ans4": "Imperator", "answer": "2"},
    18: {"question": "The Spyglass in *Minecraft* reduces your FOV by a certain percentage when used. What is this percentage reduction?", 
    "ans1": "50%", "ans2": "70%", "ans3": "90%", "ans4": "100%", "answer": "3"},
    19: {"question": "What is the arming distance of grenades fired from standard Underbarrel Grenade, Smoke, and Incendiary Launchers in *PlanetSide 2*?", 
    "ans1": "5 metres", "ans2": "10 metres", "ans3": "15 metres", "ans4": "There is no arming distance", "answer": "2"},
    20: {"question": "Which of the following is the Heavy Assault's Adaptive Class Underbarrel grenade type in *PlanetSide 2*?", 
    "ans1": "Havoc Grenades", "ans2": "Concussion Grenades", "ans3": "Impulse Grenades", "ans4": "Fragmentation Grenades", "answer": "1"},
    21: {"question": "In *PlanetSide 2*, how much damage can a Nanite Mesh Generator overshield absorb before failing?", 
    "ans1": "300", "ans2": "350", "ans3": "400", "ans4": "450", "answer": "4"},
    22: {"question": "In *Tom Clancy's Rainbow Six Siege*, the following shotguns are pump-action EXCEPT for:", 
    "ans1": "M590A1", "ans2": "Supernova", "ans3": "FO-12", "ans4": "ITA12L", "answer": "3"},
    23: {"question": "Which of the following operators have access to 3 primary weapon choices in *Tom Clancy's Rainbow Six Siege*?", 
    "ans1": "Tachanka", "ans2": "Mozzie", "ans3": "Blackbeard", "ans4": "Fuze", "answer": "4"},
    24: {"question": "In *Tom Clancy's Rainbow Six Siege*, the following Attacking operators have access to Ballistic Shields EXCEPT for:", 
    "ans1": "Blitz", "ans2": "Blackbeard", "ans3": "Montagne", "ans4": "Fuze", "answer": "2"},
    25: {"question": "Which of these words holds the definition \"stubbornly refusing to change one's opinion or chosen course of action in spite of persuation\"?", 
    "ans1": "Cantankerous", "ans2": "Crotchety", "ans3": "Obstinate", "ans4": "Iniquitous", "answer": "3"},
    26: {"question": "In *PlanetSide 2*, which of these empire-specific sniper rifles does not come pre-mounted with a scope?", 
    "ans1": "AF-8 RailJack", "ans2": "TRAP-M1", "ans3": "Phaseshift VX-S", "ans4": "ADVX // Mako", "answer": "2"},
    27: {"question": "In *Tom Clancy's Rainbow Six Siege*, how much health can Doc's MPD-0 Stim Pistol restore to an operator NOT in DBNO?", 
    "ans1": "40HP", "ans2": "45HP", "ans3": "50HP", "ans4": "55HP", "answer": "1"},
    28: {"question": "In *Phasmophobia*, which ghost type decreases its activity when players stay together?", 
    "ans1": "Revenant", "ans2": "Yurei", "ans3": "Shade", "ans4": "Demon", "answer": "3"},
    29: {"question": "Which of the following sidearms in *Tom Clancy's Rainbow Six Siege* features a green laser sight?", 
    "ans1": "P226 Mk 25", "ans2": "5.7 USG", "ans3": "P-10C", "ans4": "RG15", "answer": "4"},
    30: {"question": "What does the CAMRS in *Tom Clancy's Rainbow Six Siege* stand for?", 
    "ans1": "Canadian Advanced Mil-dot Reticle Standard", "ans2": "Canadian Army Marksman Rifle System", 
    "ans3": "Canadian Advanced Marksman Rifle System", "ans4": "Customizable Anti Material Rifle System", "answer": "2"},
    31: {"question": "What is the real life counterpart of the .357 Keratos in *Tom Clancy's Rainbow Six Siege*?", 
    "ans1": "Taurus Judge", "ans2": "S&W Model 586", "ans3": "Chiappa Rhino", "ans4": "Colt Python", "answer": "3"},
    32: {"question": "In *PlanetSide 2*, which of the following is part of the Terran Republic's \"Trident\" arsenal?", 
    "ans1": "MGR-A1 Vanquisher", "ans2": "MG-H1 Watchman", "ans3": "VE-S Canis", "ans4": "NS-44L Blackhand", "answer": "2"},
    33: {"question": "In *PlanetSide 2*, which of the following is NOT an IRNV (night vision) optic?", 
    "ans1": "DV6", "ans2": "Nx1", "ans3": "HS/NV Scope", "ans4": "NiCO", "answer": "4"},
    34: {"question": "In *PlanetSide 2*, which of the following is a Nanite Systems optic?", 
    "ans1": "TSO-1", "ans2": "Rx1", "ans3": "Corona IR", "ans4": "CCLR", "answer": "4"},
    35: {"question": "In *Tom Clancy's Rainbow Six Siege*, which of the following optic magnifications does NOT exist?", 
    "ans1": "x4.0", "ans2": "x5.0", "ans3": "x8.0", "ans4": "x12.0", "answer": "3"},
    36: {"question": "In the Nekopara series, which of the following characters is Kashou's grandmother?", 
    "ans1": "Azuki", "ans2": "Beignet", "ans3": "Maple", "ans4": "Shigure", "answer": "2"},
    37: {"question": "In the Nekopara series, which of the following breeds of cat is Fraise?", 
    "ans1": "Scottish Curl", "ans2": "Maine Coon", "ans3": "Chinchilla Persian", "ans4": "Munchkin", "answer": "3"},
    38: {"question": "In *PlanetSide 2*, which of the following damage types does the M18 Needler use?", 
    "ans1": "Air to Ground Warheads", "ans2": "Small Arms", "ans3": "Infantry Rocket Launchers", "ans4": "Aircraft Machine Guns", "answer": "4"},
    39: {"question": "In *PlanetSide 2*, what is the frontal damage mitigation provided by the Forward Vanguard Shield?", 
    "ans1": "20%", "ans2": "34%", "ans3": "67%", "ans4": "88%", "answer": "3"},
    40: {"question": "All tanks in *PlanetSide 2* sport one single barrel, with the exception of the:", 
    "ans1": "Vanguard", "ans2": "Prowler", "ans3": "Magrider", "ans4": "Colossus", "answer": "2"},
    41: {"question": "Which of the following vehicles in *PlanetSide 2* CANNOT be pulled without spending nanites?", 
    "ans1": "Sunderer", "ans2": "ANT", "ans3": "Liberator", "ans4": "Flash", "answer": "3"},
    42: {"question": "In *PlanetSide 2*, which of the following Reaver nose cannons is exclusive to Interceptor variants?", 
    "ans1": "M20 Kestrel", "ans2": "M20-W Appaloosa", "ans3": "Vortek Rotary", "ans4": "M20 Mustang", "answer": "2"},
    43: {"question": "In *PlanetSide 2*, which of the following weapons is capable of dealing flak damage?", 
    "ans1": "G40-F Ranger", "ans2": "Titan-150 AP", "ans3": "M4-F Pillager", "ans4": "L105 Zephyr", "answer": "1"},
    44: {"question": "In *PlanetSide 2*, which of the following Flash primary weapons is a common pool weapon?", 
    "ans1": "M4-F Pillager", "ans2": "LA7 Buzzard", "ans3": "V30-F Starfall", "ans4": "M12 Kobalt-F", "answer": "4"},
    45: {"question": "Which of the following melee weapons in *PlanetSide 2* can be powered to deal additional damage?", 
    "ans1": "NSX Amaterasu", "ans2": "Chainblade", "ans3": "Carver", "ans4": "Damascus Edge", "answer": "3"},
    46: {"question": "In the Call of Duty: Zombies storyline, who was responsible for poisoning the drinks of the Primis and Ultimis crews?", 
    "ans1": "Primis Richtofen", "ans2": "Primis Nikolai", "ans3": "Primis Takeo", "ans4": "Ultimis Nikolai", "answer": "2"},
    47: {"question": "In *Dead Frontier 2*, which of the following effects does the Paramedic's Bag NOT cleanse?", 
    "ans1": "Severe Burns", "ans2": "Radiation Poisoning", "ans3": "Bacterial Infection", "ans4": "Bleeding", "answer": "2"},
    48: {"question": "In *Dead Frontier 2*, which of the following effects is NOT an \"Intoxicated\" effect?", 
    "ans1": "-20% Maximum Accuracay", "ans2": "-5% Incoming Damage", "ans3": "-20% Minimum Accuracy", "ans4": "-10% Aim Speed", "answer": "4"},
    49: {"question": "Which of the following is the smallest map in *PlayerUnknown's Battlegrounds*?", 
    "ans1": "Haven", "ans2": "Taego", "ans3": "Paramo", "ans4": "Karakin", "answer": "1"}, 
    50: {"question": "Which of the following potions in *Minecraft* is brewed with an Awkward Potion, Golden Carrot, and Fermented Spider Eye?", 
    "ans1": "Potion of Night Vision", "ans2": "Potion of Blindness", "ans3": "Potion of Invisibility", 
    "ans4": "None of the above", "answer": "3"},
    51: {"question": "Which of the following sidearms in *Ready or Not* can be equipped with an IR Laser?", 
    "ans1": "G19", "ans2": ".357 Magnum", "ans3": "M45A1", "ans4": "P92X", "answer": "1"},
    52: {"question": "Which of the following is NOT a headgear option in *Ready or Not*?", 
    "ans1": "Anti-Flash Goggles", "ans2": "Ballistic Mask", "ans3": "NVGS", "ans4": "Face Shield", "answer": "4"},
    53: {"question": "Which mission mode in *Ready or Not* has a difficulty rating of Insane?", 
    "ans1": "Raid", "ans2": "Hostage Rescue", "ans3": "Active Shooter", "ans4": "Barricaded Suspects", "answer": "2"},
    54: {"question": "Which of the following is NOT an armour level in *Ready or Not*? ", 
    "ans1": "No Armour", "ans2": "Light Armour", "ans3": "Medium Armour", "ans4": "Heavy Armour", "answer": "3"},
    55: {"question": "In the anime seires *The Idolm@ster*, which idol's story did Episode 21 \"Promise\" focus on?", 
    "ans1": "Kisaragi Chihaya", "ans2": "Minase Iori", "ans3": "Haruka Amami", "ans4": "Futami Ami", "answer": "1"},
    56: {"question": "What is the fastest ground vehicle in *PlanetSide 2*?", 
    "ans1": "Flash", "ans2": "Harasser", "ans3": "Sunderer", "ans4": "Lightning", "answer": "2"},
    57: {"question": "In *PlanetSide 2*, what type of vehicle CANNOT be pulled from the Flotillas on Oshur?", 
    "ans1": "Light Vehicles", "ans2": "Support Vehicles", "ans3": "Mobile Armour", "ans4": "Heavy Aircraft", "answer": "3"},
    58: {"question": "In *PlanetSide 2*, Exodus PPCs can be found on the Flotillas on Oshur. What does \"PPC\" stand for?", 
    "ans1": "Pulsed Particle Cannon", "ans2": "Particle Projection Cannon", 
    "ans3": "Personnel Protection Convoy", "ans4": "Polystellarite Preparation Canister", "answer": "2"},
    59: {"question": "In *PlanetSide 2*, which of the following Terran Republic weapons can equip KCAP Ammunition?", 
    "ans1": "T1S Cycler", "ans2": "TMG-50", "ans3": "MG-S1 Jackal", "ans4": "AMR-66", "answer": "3"},
    60: {"question": "In *PlanetSide 2*, which of the following is a fully automatic shotgun?", 
    "ans1": "LA39 Bruiser", "ans2": "FA1 Barrage", "ans3": "Pandora VX25", "ans4": "HSG-400", "answer": "3"},
    61: {"question": "In *Ready or Not*, which of the following devices CANNOT unlock a locked door?", 
    "ans1": "Lockpick Gun", "ans2": "Multitool", "ans3": "C2 Charge", "ans4": "Door Wedge", "answer": "4"},
    62: {"question": "In *Ready or Not*, what ammunition does the M32A1 Launcher fire?", 
    "ans1": "Flash", "ans2": "CS Gas", "ans3": "Stinger", "ans4": "Fragmentation", "answer": "1"},
    63: {"question": "In the anime series *My Teen Romantic Comedy SNAFU*, what is the first name of Hikigaya's sister?", 
    "ans1": "Yui", "ans2": "Yukino", "ans3": "Komachi", "ans4": "Iroha", "answer": "3"},
    64: {"question": "In the *Nekopara* anime series, what name did the nameless stray catgirl receive?",
    "ans1": "Sugarcane", "ans2": "Fraise", "ans3": "Cacao", "ans4": "Milk", "answer": "3"},
    65: {"question": "In *Hell Let Loose*, which faction uses Morphine Ampoules to revive downed soldiers?", 
    "ans1": "United States", "ans2": "Germany", "ans3": "Soviet Union", "ans4": "All of the above", "answer": "2"},
    66: {"question": "In *Hell Let Loose*, which of the following tanks lacks a driver-controlled hull machine gun?", 
    "ans1": "Sherman M4A1", "ans2": "IS-1", "ans3": "Luchs", "ans4": "Stuart", "answer": "3"},
    67: {"question": "In *Hell Let Loose*, which of the following spawn options features the longest wave timer?", 
    "ans1": "Outposts", "ans2": "Garrisons", "ans3": "Half Tracks", "ans4": "Airheads", "answer": "3"},
    68: {"question": "In *Hell Let Loose*, which of the following weapons is NOT a standard issue Machine Gunner weapon?", 
    "ans1": "Browning M1919", "ans2": "MG34", "ans3": "MG42", "ans4": "DP-27", "answer": "3"},
    69: {"question": "In *Hell Let Loose*, what weapon does the German \"Sanitäter\" Medic class use?", 
    "ans1": "Karabiner 98K", "ans2": "MP40", "ans3": "Walther P38", "ans4": "Luger P08", "answer": "4"},
    70: {"question": "In *Hell Let Loose*, besides Officers, which other Infantry class can see markers from recon scans?", 
    "ans1": "Support", "ans2": "Engineer", "ans3": "Medic", "ans4": "Machine Gunner", "answer": "1"},
    71: {"question": "In *Hell Let Loose*, which faction's standard Assault uses a semi-auto rifle instead of an SMG?", 
    "ans1": "United States", "ans2": "Germany", "ans3": "Soviet Union", "ans4": "None of the above", "answer": "2"},
    72: {"question": "In *Hell Let Loose*, how many Bunker blueprints can an Engineer place at any given time?", 
    "ans1": "1", "ans2": "2", "ans3": "3", "ans4": "4", "answer": "1"},
    73: {"question": "In *PlanetSide 2*, what benefit does the Angled Forward Grip provide?", 
    "ans1": "-60% First shot recoil", "ans2": "-20% ADS bloom", "ans3": "-25% Vertical recoil", "ans4": "-25% Horizontal recoil", "answer": "1"},
    74: {"question": "In *PlanetSide 2*, what benefit does the Mobile Prediction Laser provide?", 
    "ans1": "+33% Hipfire accuracy", "ans2": "-20% ADS bloom", "ans3": "-60% Hipfire horizontal & vertical recoil", 
    "ans4": "-40% Hipfire bloom", "answer": "3"},
    75: {"question": "In *PlanetSide 2*, which of the following is NOT a Chimera main cannon?", 
    "ans1": "CT-102 Satyr", "ans2": "CT-120 Squash Head", "ans3": "CT-135", "ans4": "CT-150 Cyclops", "answer": "2"},
    76: {"question": "In *PlanetSide 2*, which empire-specific Basilisk deals the highest damage per shot?", 
    "ans1": "N30 Trawler", "ans2": "M18 Palisade", "ans3": "V42 Pariah", "ans4": "CT2-20 HCG", "answer": "1"},
    77: {"question": "In *PlanetSide 2*, which of the following TR scout rifles CANNOT be equipped with explosive ammo?", 
    "ans1": "MG-HBR1 Dragoon", "ans2": "HSR-1", "ans3": "SOAS-20", "ans4": "DMR-99", "answer": "3"},
    78: {"question": "In *Tom Clancy's Rainbow Six Vegas 2*, under which A.C.E.S branch is the Shield unlocked?", 
    "ans1": "Marksman", "ans2": "Assault", "ans3": "CQB", "ans4": "The Shield is unlocked by default", "answer": "2"},
    79: {"question": "What is the maximum range on artillery guns in *Hell Let Loose*?", 
    "ans1": "1600m", "ans2": "1750m", "ans3": "1850m", "ans4": "1900m", "answer": "1"},
    80: {"question": "In *Hell Let Loose*, which faction's Assault does not get access to the \"Raider\" loadout?", 
    "ans1": "United States", "ans2": "Germany", "ans3": "Soviet Union", "ans4": "None of the above", "answer": "3"},
    81: {"question": "In the *Nekopara* anime series, which catgirl suffers from heterochromia?", 
    "ans1": "Vanilla", "ans2": "Coconut", "ans3": "Cinnamon", "ans4": "Chocola", "answer": "2"},
    82: {"question": "Which of the following currencies in *PlanetSide 2* can be used to purchase weapons?", 
    "ans1": "Nanites", "ans2": "A7", "ans3": "ISO-4", "ans4": "Merit", "answer": "2"},
    83: {"question": "In *PlanetSide 2*, the Colossus heavy tank can be equipped with the MAD. What does MAD stand for?", 
    "ans1": "Mortar and Artillery Dampener", "ans2": "Modular Augmentation Device", "ans3": "Mass Accelerator Drive", 
    "ans4": "Munitions Assembly Device", "answer": "3"},
    84: {"question": "In *Hell Let Loose*, which Mosin Nagant variant is issued to Soviet Grenadier Riflemen?", 
    "ans1": "Mosin Nagant 1891", "ans2": "Mosin Nagant 91/30", "ans3": "Mosin Nagant M38", "ans4": "Mosin Nagant 91/30 Scoped", "answer": "3"},
    85: {"question": "In *Hell Let Loose*, which Mosin Nagant variant is issued to standard Soviet Riflemen?", 
    "ans1": "Mosin Nagant 1891", "ans2": "Mosin Nagant 91/30", "ans3": "Mosin Nagant M38", "ans4": "Mosin Nagant 91/30 Scoped", "answer": "1"},
    86: {"question": "In *Hell Let Loose*, which Mosin Nagant variant is issued to standard Soviet Engineers?", 
    "ans1": "Mosin Nagant 1891", "ans2": "Mosin Nagant 91/30", "ans3": "Mosin Nagant M38", "ans4": "Mosin Nagant 91/30 Scoped", "answer": "2"},
    87: {"question": "In *Hell Let Loose*, which of the following classes CANNOT use the Gewehr 43 in any of their loadouts?", 
    "ans1": "Engineer", "ans2": "Commander", "ans3": "Assault", "ans4": "Rifleman", "answer": "1"},
    88: {"question": "In *Hell Let Loose*, what is the third loadout of Soviet Officers called?", 
    "ans1": "NCO", "ans2": "Starshina", "ans3": "Veteran", "ans4": "Praporshchik", "answer": "2"},
    89: {"question": "In *Hell Let Loose*, which of the following vehicles CANNOT be spawned with 500 Fuel?", 
    "ans1": "Sd.Kfz. 251 Half-track", "ans2": "IS-1 ", "ans3": "Sherman \"Jumbo\" 75mm", "ans4": "Luchs", "answer": "2"},
    90: {"question": "In *Hell Let Loose*, which faction's recon vehicle has its engine located at the front of the vehicle?", 
    "ans1": "US M8 Greyhound", "ans2": "German Puma", "ans3": "Soviet BA-10", "ans4": "All of the above", "answer": "3"},
    91: {"question": "In *Hell Let Loose*, which tank is capable of firing smoke shells?", 
    "ans1": "Sherman \"Jumbo\" 75mm", "ans2": "T-34", "ans3": "Tiger I", "ans4": "Sherman \"Jumbo\" 76mm", "answer": "1"},
    92: {"question": "In *Hell Let Loose*, what is the quantity of supplies required to construct a level 1 Bunker?", 
    "ans1": "20", "ans2": "50", "ans3": "75", "ans4": "90", "answer": "3"},
    93: {"question": "In *Hell Let Loose*, which faction's Sniper does NOT have access to a semi-auto rifle?", 
    "ans1": "United States", "ans2": "Germany", "ans3": "Soviet Union", "ans4": "All of the above", "answer": "1"},
    94: {"question": "In *Hell Let Loose*, which Soviet leadership role has the Tokarev TT-33 pistol as part of its standard issue loadout?", 
    "ans1": "Commander", "ans2": "Officer", "ans3": "Tank Commander", "ans4": "Spotter", "answer": "2"},
    95: {"question": "In *Hell Let Loose*, which of the following classes CANNOT drop firearms ammo boxes?", 
    "ans1": "Rifleman", "ans2": "Support", "ans3": "Engineer", "ans4": "Spotter", "answer": "3"},
    96: {"question": "In *Hell Let Loose*, which of the following roles can drop explosive ammo boxes?", 
    "ans1": "Rifleman", "ans2": "Anti-Tank", "ans3": "Engineer", "ans4": "Assault", "answer": "1"},
    97: {"question": "In *Hell Let Loose*, what is the default punishment applied for killing a friendly?", 
    "ans1": "The offending player is killed", "ans2": "+10s respawn time per teamkill", "ans3": "+50 grief points per teamkill", 
    "ans4": "All of the above", "answer": "2"},
    98: {"question": "In *The Escapists 2*, what action can be performed by the plastic fork?", 
    "ans1": "Cutting", "ans2": "Chipping", "ans3": "Digging", "ans4": "All of the above", "answer": "2"},
    99: {"question": "In *The Escapists 2*, which of the following weapons CANNOT knock out an unarmoured target in one hit?", 
    "ans1": "Cup of Molten Chocolate", "ans2": "Stungun", "ans3": "Cattle Prod", "ans4": "Makeshift Sledgehammer", "answer": "4"},
    100: {"question": "In the anime series *The Helpful Fox Senko-san*, what is the colour of Shiro's hair?", 
    "ans1": "Orange", "ans2": "Purple", "ans3": "White", "ans4": "Blue", "answer": "3"},
    101: {"question": "Name the error that plagued *PlanetSide 2* for over a month after the Arsenal Update.", 
    "ans1": "G2 Error", "ans2": "G15 Error", "ans3": "G21 Error", "ans4": "G99 Error", "answer": "2"},
    102: {"question": "Which *PlanetSide 2* server experienced issues with its API for months after the Arsenal Update?", 
    "ans1": "Connery", "ans2": "SolTech", "ans3": "Emerald", "ans4": "Miller", "answer": "2"},
    103: {"question": "Right after the Arsenal Update in *PlanetSide 2*, what bug did vehicles with turbo systems experience?", 
    "ans1": "Turbo duration was infinite", "ans2": "Turbo boost did not increase their speed", 
    "ans3": "Turbo activation cost was higher than usual", "ans4": "Turbo recharge rate was delayed", "answer": "3"},
    104: {"question": "What was Senātus Populusque Rōmānus abbreviated as?", 
    "ans1": "SPR", "ans2": "SPRM", "ans3": "SPLR", "ans4": "SPQR", "answer": "4"},
    105: {"question": "During the period of the Roman Empire, which standard bearer carried a legion's eagle standard?", 
    "ans1": "Aquilifer", "ans2": "Signifer", "ans3": "Vexillifer", "ans4": "Imaginifer", "answer": "1"},
    106: {"question": "Which *PlanetSide 2* faction does the quote \"Freedom over Oppression\" belong to?", 
    "ans1": "New Conglomerate", "ans2": "Terran Republic", "ans3": "Vanu Sovereignty", "ans4": "Nanite Systems Operative", "answer": "1"},
    107: {"question": "There is only one semi-automatic shotgun in *Tom Clancy's Rainbow Six Vegas* and *Tom Clancy's Rainbow Six Vegas 2*. What is this shotgun?", 
    "ans1": "870MCS", "ans2": "M3", "ans3": "SPAS-12", "ans4": "XM-26 LSS", "answer": "4"},
    108: {"question": "In *Resident Evil 2*, who will be the player's partner be should the player choose Chris Redfield as their character?", 
    "ans1": "Jill Valentine", "ans2": "Rebecca Chambers", "ans3": "Barry Burton", "ans4": "Leon Kennedy", "answer": "2"},
    109: {"question": "In the Resident Evil 2 DLC *Ghost Survivors*, which of the following charactes does NOT receive an alternate story?", 
    "ans1": "Robert Kendo", "ans2": "Katherine Warren", "ans3": "Ghost", "ans4": "Annette Birkin", "answer": "4"},
    110: {"question": "In *Hell Let Loose*, which of the following classes has access to the SVT-40?", 
    "ans1": "Rifleman", "ans2": "Assault", "ans3": "Support", "ans4": "Anti-Tank", "answer": "3"},
    111: {"question": "In *Hell Let Loose*, which of the following requirements must be met in order to earn the \"This Is Ridiculous\" achievement?", 
    "ans1": "Kill 75 enemies without dying", "ans2": "Drop 2,500 ammo boxes", "ans3": "Spend 1,000,000 supplies on building defences", 
    "ans4": "Kill a Sniper with a pistol", "answer": "2"},
    112: {"question": "In *Hell Let Loose*, what uniform is unlocked for Soviet infantry classes upon reaching Level V?", 
    "ans1": "M40 Winter Coat", "ans2": "M40 Cape Plash-Palatka", "ans3": "M43 Winter Coat", "ans4": "Vatnik M40", "answer": "1"},
    113: {"question": "In *Hell Let Loose*, which headgear is unlocked for German leadership classes upon reaching Level IV?", 
    "ans1": "M43 Field Cap", "ans2": "Visor Cap", "ans3": "Tiger Covered M38", "ans4": "Eastern Covered M38", "answer": "2"},
    114: {"question": "Which machine gun in *Hell Let Loose* can be fired continuously for the longest period of time?", 
    "ans1": "Browning M1919", "ans2": "MG34", "ans3": "MG42", "ans4": "DP-27", "answer": "1"},
    115: {"question": "In *Hell Let Loose*, what weapon do US Sapper Engineers gain access to?", 
    "ans1": "M3 Grease Gun", "ans2": "M1 Garand", "ans3": "M1 Carbine", "ans4": "M97 Trench Gun", "answer": "4"},
    116: {"question": "Which Ushanka variant is unlocked at Level V for all Soviet classes in *Hell Let Loose*?", 
    "ans1": "Default", "ans2": "Furlined", "ans3": "Tied", "ans4": "Battle Worn", "answer": "3"},
    117: {"question": "Which of the following TR weapons in *PlanetSide 2* does not have access to Impact Ammunition?", 
    "ans1": "MG-H1 Watchman", "ans2": "MG-A1 Arbalest", "ans3": "TORQ-9", "ans4": "MG-C1 Kindred", "answer": "4"},
    118: {"question": "Which of the following default shotugns in *PlanetSide 2* has the highest magazine capacity?", 
    "ans1": "Mauler S6", "ans2": "FA1 Barrage", "ans3": "Thanatos VE70", "ans4": "SG-100", "answer": "4"},
    119: {"question": "In *PlanetSide 2*, which shotgun variant does the Phobos VX86 belong to?", 
    "ans1": "Automatic", "ans2": "Semi Automatic", "ans3": "Heavy Pump Action", "ans4": "Light Pump Action", "answer": "4"},
    120: {"question": "In *PlanetSide 2*, what fire mode does the NSX Yumi use?", 
    "ans1": "Semi Automatic", "ans2": "5x Burst", "ans3": "6x Burst", "ans4": "Automatic", "answer": "2"},
    121: {"question": "Which empire-specific assault rifle in *PlanetSide 2* uses a 6 round burst fire mode?", 
    "ans1": "MGR-A1 Vanquisher", "ans2": "MG-A1 Arbalest", "ans3": "VE-A Lacerta", "ans4": "AR-N203", "answer": "2"},
    122: {"question": "In *PlanetSide 2*, prior to the Arsenal Update, what did the BX Adapter do?", 
    "ans1": "Adds an alternative 750 RPM wind up fire mode", "ans2": "Increases the maximum damage of the weapon to 142", 
    "ans3": "Adds an alternative wind-up 9x burst fire mode", "ans4": "Enhances the weapon's ammunition adaptively", "answer": "3"},
    123: {"question": "Which of the following continents in *PlanetSide 2* contains only one Tech Plant?", 
    "ans1": "Indar", "ans2": "Esamir", "ans3": "Hossin", "ans4": "Amerish", "answer": "2"},
    124: {"question": "Which of the following Bio Labs in *PlanetSide 2* features vehicle-capturable control points?", 
    "ans1": "Allatum Bio Lab", "ans2": "Onatha Bio Lab", "ans3": "Ikanam Bio Lab", "ans4": "Acan Bio Lab", "answer": "3"},
    125: {"question": "Which of the following Amp Stations in *PlanetSide 2* can be found on Hossin?", 
    "ans1": "Peris Amp Station", "ans2": "Freyr Amp Station", "ans3": "Sungrey Amp Station", "ans4": "Ixtab Amp Station", "answer": "4"},
    126: {"question": "Which of the following vehicles in *PlanetSide 2* CANNOT be deployed?", 
    "ans1": "Sunderer", "ans2": "Prowler", "ans3": "Harasser", "ans4": "Colossus", "answer": "3"},
    127: {"question": "Which of the following aircraft in *PlanetSide 2* can be deployed?", 
    "ans1": "Dervish", "ans2": "Valkyrie", "ans3": "Liberator", "ans4": "Galaxy", "answer": "4"},
    128: {"question": "In *PlanetSide 2*, which bolt-action sniper variant does the LA80 belong to?", 
    "ans1": "Balanced", "ans2": "Close Quarters", "ans3": "High Damage", "ans4": "High Capacity", "answer": "4"},
    129: {"question": "Which weapon in the TR arsenal in *PlanetSide 2* has the highest rate of fire?", 
    "ans1": "SMG-46 Armistice", "ans2": "T4 AMP", "ans3": "LC2 Lynx", "ans4": "MG-H1 Watchman", "answer": "2"},
    130: {"question": "Which of the following classes in *PlanetSide 2* has Advanced Shield Capacitor 5 unlocked by default?", 
    "ans1": "Light Assault", "ans2": "Combat Medic", "ans3": "Engineer", "ans4": "Heavy Assault", "answer": "1"},
    131: {"question": "In *PlanetSide 2*, which damage type does the Hellfire Rocket Pods deal on a direct hit?", 
    "ans1": "Explosive Splash", "ans2": "Air to Ground Warheads", "ans3": "Light Anti-Vehicle", "ans4": "Aircraft Machine Guns", "answer": "3"},
    132: {"question": "Which of the following MBT AP cannons in *PlanetSide 2* deals the most direct damage per shot?", 
    "ans1": "Titan-150 AP", "ans2": "P2-120 AP", "ans3": "Supernova FPC", "ans4": "CT-150 Cyclops", "answer": "4"},
    133: {"question": "Which of the following tank cannons deals the most direct damage per magazine?", 
    "ans1": "P2-120 AP", "ans2": "C75 Viper", "ans3": "Mammoth Cannon", "ans4": "CT-102 Satyr", "answer": "4"},
    134: {"question": "Which of the following weapons in *PlanetSide 2* is NOT a black market weapon?", 
    "ans1": "NS-30 Vandal", "ans2": "NS Viscount G6", "ans3": "NS-44L Showdown", "ans4": "Havoc Missiles", "answer": "1"},
    135: {"question": "Which of the following NSO weapons in *PlanetSide 2* uses an automatic 3 round burst fire mode?", 
    "ans1": "AR-N203", "ans2": "BAR-A50", "ans3": "XMG-155", "ans4": "SR-L75", "answer": "1"},
    136: {"question": "What is the full name of the \"Auraxium\" NSO scout rifle in *PlanetSide 2*?", 
    "ans1": "BAR-ARX Rutherford", "ans2": "BAR-ARX Schrodinger", "ans3": "BAR-ARX Feynman", "ans4": "BAR-ARX Dirac", "answer": "3"},
    137: {"question": "Which of the following VS weapons in *PlanetSide 2* CANNOT equip Lashing Ammunition?", 
    "ans1": "Corvus VA55", "ans2": "Darkstar", "ans3": "VE-A Lacerta", "ans4": "Lasher X2", "answer": "4"},
    138: {"question": "Which of the following scout rifles in *PlanetSide 2* have a 0.75x ADS move speed multiplier?", 
    "ans1": "Warden", "ans2": "HSR-1", "ans3": "VE-LR Obelisk", "ans4": "NS-30 Vandal", "answer": "4"},
    139: {"question": "Which of the following sniper rifles in *PlanetSide 2* has a 0.75x ADS move speed multiplier?", 
    "ans1": "SR-L75", "ans2": "Parallax VX3", "ans3": "99SV", "ans4": "SAS-R", "answer": "1"},
    140: {"question": "What is the minimum arming distance of the NS Scorpion in *PlanetSide 2*?", 
    "ans1": "10m", "ans2": "20m", "ans3": "30m", "ans4": "40m", "answer": "4"},
    141: {"question": "What was the longest calendar year in human history?", 
    "ans1": "48 BC", "ans2": "47 BC", "ans3": "46 BC", "ans4": "45 BC", "answer": "3"},
    142: {"question": "Who did Gaius Julius Caesar appoint as his *magister equitum* during his dictatorship for life?", 
    "ans1": "Marcus Antonius", "ans2": "Marcus Aemilius Lepidus", "ans3": "Marcus Junius Brutus", "ans4": "Gaius Octavius", "answer": "2"},
    143: {"question": "What was the last civil war of the Roman Republic?", 
    "ans1": "The Battle of Philipi", "ans2": "The Battle of Mutina", "ans3": "The Battle of Pharsalus", "ans4": "The Battle of Actium", "answer": "4"},
    144: {"question": "Which of the following Roman politicians did NOT take part in the assasination of Gaius Julius Caesar?", 
    "ans1": "Gaius Trebonius", "ans2": "Marcus Tullius Cicero", "ans3": "Publius Servilius Casca", "ans4": "Tillius Cimber", "answer": "2"},
    145: {"question": "Which legion did Gaius Julius Caesar cross the Rubicon river with in 49 BC during his march on Rome?", 
    "ans1": "Legio I Germanica", "ans2": "Legio IV Macedonica", "ans3": "Legio X Equestris", "ans4": "Legio XIII Gemina", "answer": "4"},
    145: {"question": "Which of the four Roman emperors emerged as the emperor of Rome following the Year of the Four Emperors?", 
    "ans1": "Servius Sulpicius Galba", "ans2": "Marcus Salvius Otho", "ans3": "Aulus Vitellius Germanicus", "ans4": "Titus Flavius Vespasian", "answer": "4"},
    146: {"question": "How many lictors was a Roman praetor escorted by?", "ans1": "4", "ans2": "6", "ans3": "8", "ans4": "12", "answer": "2"},
    700: {"question": "", "ans1": "", "ans2": "", "ans3": "", "ans4": "", "answer": ""},
}


def colRan():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b= random.randint(0,255)
    colour=discord.Colour.from_rgb(r, g, b)
    return colour


cmdWhitelist = [
    521293177315917850,
    591074600411070502,
    "WhatTheVeggies#1197",
    "Krygswyrfer#8394",
    "<@!521293177315917850>",
    "<@!591074600411070502>",
]


planetguns = [
    "TORQ-9", "HC1 Cougar", "T5 AMC", "FA1 Barrage", "SABR-13", "RAMS .50M", "MG-HBR1 Dragoon", "MG-A1 Arbalest", "Cycler TRV", "MG-S1 Jackal",
    "AMR-66", "TX1 Repeater", "Lc2 Lynx", "T9 CARV", "TMG-50", "MSW-R", "T1A Unity", "M9 SKEP Launcher", "T7 Mini Chaingun",

    "Reaper DMR", "NC9 A-Tross", "MGR-A1 Vanquisher", "MGR-L1 Promise", "NC12 Sweeper", "NC6 Gauss SAW", "NC14 Bolt Driver", "AF-8 RailJack",
    "NC05 Jackhammer", "NC15 Phoenix", "AF-8 Stalker",

    "Phaseshift VX-S", "VE-S Canis", "VE-H Maw", "Eridani SX5", "SVA-88",

    "AR-N203", "PMG-3XB", "CB-X75", "SG-A25", "HSG-400", "XMG-150", "LAV-AG", "ADVX // Mako", "BAR-A50", "SR-L75", "U-200 Harbinger",
    "SG-ARX Rutherford", "BAR-ARX Feynman", "XMG-ARX Galilei", "U-ARX Dirac",

    "NS-AM7 Archer", "NS-11C", "MKV Suppressed", "NS-30 Vandal", "NS Swarm-03", "NS-44L Blackhand", "NS-15M2",

    "NSX Amaterasu", "NSX Tanto", "NS-45 Pilot", "NSX Naginata",

    "NSX Kappa", "NSX Sesshin", "NSX Yawara", "NS-357IA", "NS-30 Tranquility", 
    ]