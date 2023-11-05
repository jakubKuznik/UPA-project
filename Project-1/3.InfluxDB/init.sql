
CREATE DATABASE PARKOVACI_MISTA_V_BRNE;

-- Connect to database 
USE PARKOVACI_MISTA_V_BRNE;

-- TODO  time precision on sec 

-- NOTE: 
-- measurement, tag1=something tag2=kk, field1=k field2=kk

-- SSU  - spaces subsciber vacant  
-- SSO  - spaces subsciber occupied 
-- SAUV - spaces all users vacant 
-- SAUO - spaces all users occupied 

-- We are using actuall time 

INSERT volne_mista,name=parkovaci-dum-domini-park-brno-husova-712-14a,capacity=367,X=49.19447,Y=16.6056528,Latitude=49.19447,Longitude=16.6056528,SSV=76,SAUV=160 SSU=23,SSO=108,cars=207,free=160
INSERT volne_mista,name=p-+-r-parkovaci-dum-river-park-polni-1033-35,capacity=110,X=49.18225,Y=16.60181,Latitude=49.18225,Longitude=16.60181,SSV=0,SAUV=104 SSU=0,SSO=6,cars=6,free=104
INSERT volne_mista,name=parkovaci-dum-pinki-park-brno-kopecna-998-24,capacity=88,X=49.1903733,Y=16.6049692,Latitude=49.1903733,Longitude=16.6049692,SSV=14,SAUV=51 SSU=10,SSO=13,cars=37,free=51
INSERT volne_mista,name=parkoviste-benesova-naproti-hotelu-grand,capacity=80,X=49.1926839,Y=16.6140764,Latitude=49.1926839,Longitude=16.6140764,SSV=0,SAUV=23 SSU=0,SSO=57,cars=57,free=23
INSERT volne_mista,name=parkoviste-veveri,capacity=140,X=49.2072989,Y=16.5925664,Latitude=49.2072989,Longitude=16.5925664,SSV=0,SAUV=86 SSU=0,SSO=54,cars=54,free=86
INSERT volne_mista,name=parking-u-janackova-divadla,capacity=379,X=49.1990306,Y=16.6094689,Latitude=49.1990306,Longitude=16.6094689,SSV=34,SAUV=212 SSU=20,SSO=113,cars=167,free=212
INSERT volne_mista,name=parkoviste-skorepka,capacity=49,X=49.1923911,Y=16.6177942,Latitude=49.1923911,Longitude=16.6177942,SSV=0,SAUV=2 SSU=0,SSO=24,cars=24,free=25
INSERT volne_mista,name=p+r-u-ustredniho-hrbitova,capacity=173,X=49.1701456,Y=16.5987353,Latitude=49.1701456,Longitude=16.5987353,SSV=0,SAUV=150 SSU=0,SSO=23,cars=23,free=150
INSERT volne_mista,name=p+r-lisen-u-zetoru,capacity=224,X=49.2001003,Y=16.6696408,Latitude=49.2001003,Longitude=16.6696408,SSV=0,SAUV=178 SSU=0,SSO=46,cars=46,free=178


/* RAW CSV DATA 
X,Y,ObjectId,name,capacity,free,Latitude,Longitude,spacesSubscribersVacant,spacesSubscribersOccupied,spacesAllUsersVacant,spacesAllUsersOccupied,cars,capacity_procent,startdate,CapacityForPublic
1848532.814,6307923.5356,1,"Parkovací dům DOMINI PARK – Brno, Husova 712/14a",367,160,49.19447,16.6056528,76,23,160,108,207,43.5967302452316,2023/08/18 15:00:00+00,268
1848105.0354,6305842.1747,2,"P + R parkovací dům RIVER PARK, Polní 1033/35",110,104,49.18225,16.60181,0,0,104,6,6,94.5454545454545,2023/08/18 15:00:00+00,110
1848456.716,6307225.7114,3,"Parkovací dům PINKI PARK - Brno, Kopečná 998/24",88,51,49.1903733,16.6049692,14,10,51,13,37,57.9545454545455,2023/08/18 15:00:00+00,64
1849470.5248,6307619.2876,4,Parkoviště Benešova - naproti hotelu Grand,80,23,49.1926839,16.6140764,0,0,23,57,57,28.75,2023/08/18 15:00:00+00,80
1847076.0426,6310109.1602,5,Parkoviště Veveří ,140,86,49.2072989,16.5925664,0,0,86,54,54,61.4285714285714,2023/08/18 15:00:00+00,140
1848957.6203,6308700.4476,6,Parking u Janáčkova divadla,379,212,49.1990306,16.6094689,34,20,212,113,167,55.9366754617414,2023/08/18 15:00:00+00,325
1849884.3885,6307569.4125,7,Parkoviště Skořepka,49,25,49.1923911,16.6177942,0,0,25,24,24,51.0204081632653,2023/08/18 15:00:00+00,49
1847762.7614,6303781.0098,8,P+R u Ústředního hřbitova,173,150,49.1701456,16.5987353,0,0,150,23,23,86.7052023121387,2023/08/18 15:00:00+00,173
1855655.9256,6308882.6846,9,P+R Líšeň u Zetoru,224,178,49.2001003,16.6696408,0,0,178,46,46,79.4642857142857,2023/08/18 15:00:00+00,224
*/
