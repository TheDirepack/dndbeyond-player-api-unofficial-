import json

def readf(other):
  f = open('carlist.txt', 'r')
  file = json.loads(f.read())
  f.close()
  x=0
  fileout=[]
  while (x<len(file)):
    f = open(str(file[x])+'.txt', 'r')
    file1 = json.loads(f.read())
    f.close()
    fileout.append(file1)
    x=x+1
  if other==1:
    fileout=file
  else:
    fileout=fileout
  return (fileout) 

def writef(file):
  f = open('carlist.txt', 'r')
  list = json.loads(f.read())
  f.close()
  x=0
  while (x<len(list)):
    f = open(str(list[x])+'c.txt', 'w+')
    f.write(json.dumps(file.get(list[x],"")))
    f.close()
    x=x+1
  return (file)

def dejson(dict,location,locationlist):
  dict2={}
  loop=0
  while len(locationlist)>loop:
    if (location!=0):
      dict2[str(locationlist[loop])]=dict.get(str(location),"1").get(str(locationlist[loop]),"2")
    else:
      dict2[str(locationlist[loop])]=dict.get(str(locationlist[loop]),"2") 
    loop=loop+1
  return (dict2)

def raceget(modic):
  modic=modic.get("modifiers","stat3")
  racemod=modic.get("race","stat4")
  loop=0
  loop2=0
  out={}
  out2=[]
  raceinfo=['subType','type','friendlySubtypeName','isGranted','value',]
  while len(racemod)>loop:
    loop2=0
    racemod2=racemod[loop]
    while len(raceinfo)>loop2:
      out[raceinfo[loop2]]=racemod2.get(raceinfo[loop2],"null")
      loop2=loop2+1
    out2.append(out)
    out={}
    loop=loop+1
  return (out2)

def racextract(list):
  loop=0
  loop2=0
  lang=[]
  bonus={}
  out={}
  statlist=['strength-score', 'dexterity-score', 'constitution-score', 'intelligence-score', 'wisdom-score', 'charisma-score']
  while len(list)>loop:
    racepos=list[loop]
    typep=racepos.get("type","1")
    if (typep=='language'):
      lang.append(racepos.get('subType',"2"))
    elif (typep=='bonus'):
      loop2=0
      while len(statlist)>loop2:
        if statlist[loop2]==racepos.get('subType',"3"):
          bonus[statlist[loop2]]=racepos.get('value',"4")
        loop2=loop2+1
    else:
      print (typep)
    loop=loop+1
    out["Rlanguage"]=lang
    out['Rbonus']=bonus
  return (out)

def invextract(list):
  loop=0
  out={}
  armlist=['weight','name','type','cost','rarity','armorClass','magic','filterType']
  weplist=['weight','name','type','cost','rarity','damageType','range','longRange','magic','filterType']
  othlist=['weight','name','type','cost','rarity','magic','type','filterType']
  while len(list)>loop:
    typec=list[loop]
    typep=typec.get('filterType',"1")
    if (typep=='Armor'):
      out["inv "+str(loop+1)]=dejson(typec,0,armlist)
    elif (typep=='Weapon'):
      temp=dejson(typec,0,weplist)
      temp.update(dejson(typec,"damage",['diceCount','diceValue','diceMultiplier','fixedValue']))
      out["inv "+str(loop+1)]=temp
    elif (typep== 'Other Gear'):
      out["inv "+str(loop+1)]=dejson(typec,0,othlist)
    else:
      print (typep)
    loop=loop+1
  out["invmax"]=loop
  return (out)

def classxtract(list):
  loop=0
  out=[]
  out2={}
  while len(list)>loop:
    racepos=list[loop]
    typep=racepos.get("type","1")
    if (typep=='proficiency'):
      out.append(racepos.get('subType',"2"))
      out.append(racepos.get('isGranted',"2"))
    elif (typep=='expertise'):
      out.append(racepos.get('subType',"2"))
      out.append(racepos.get('isGranted',"2"))
    else:
      print (typep)
    loop=loop+1
  out2["class"]=out
  return (out2)

def getlist(dic,re1,re2,list):
  dic1=dic.get(re1,"stat3")
  dic2=dic1.get(re2,"stat4")
  loop=0
  loop2=0
  out={}
  out2=[]
  while len(dic2)>loop:
    loop2=0
    racemod2=dic2[loop]
    while len(list)>loop2:
      out[list[loop2]]=racemod2.get(list[loop2],"null")
      loop2=loop2+1
    out2.append(out)
    out={}
    loop=loop+1
  return (out2)
  
def classget(modic):
  modic=modic.get("modifiers","stat3")
  racemod=modic.get("class","stat4")
  loop=0
  loop2=0
  out={}
  out2=[]
  classinfo=['type','subType','friendlyTypeName','friendlySubtypeName','isGranted']
  while len(racemod)>loop:
    loop2=0
    racemod2=racemod[loop]
    while len(classinfo)>loop2:
      out[classinfo[loop2]]=racemod2.get(classinfo[loop2],"null")
      loop2=loop2+1
    out2.append(out)
    out={}
    loop=loop+1
  return (out2)

def statget(dict2):
  loop=0
  outS={}
  statlist=['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
  while len(statlist)>loop:
    outS["S"+str(statlist[loop])]=str(dict2.get("stats","stat1")[loop].get("value","stat2"))
    loop=loop+1
  return (outS)

def invget(dict2):
  loop=0
  invlist1=["id","quantity","equipped","isAttuned"]
  invlist2=["damage","weight","baseItemId","damageType","categoryId","range","longRange","id","magic","name","type","rarity","filterType","cost","baseArmorName","armorClass","stealthCheck","armorTypeId","baseTypeId"]  
  inventory = dict2.get("inventory","3")
  out=[]
  while len(inventory)>loop:
    outdic={}
    indic={}
    loop1=0
    loop2=0
    invget=inventory[loop]
    while len(invlist1)>loop1:
      outdic[invlist1[loop1]]=invget.get(invlist1[loop1],"7")
      loop1=loop1+1
    while len(invlist2)>loop2:
      if (invget.get("definition","null").get(invlist2[loop2],"null")!="null"):
        indic[invlist2[loop2]]=invget.get("definition","9").get(invlist2[loop2],"18")
      loop2=loop2+1
    indic.update(outdic)
    out.append(indic)
    loop=loop+1
  return (out)

def asemble(text):
  list=["name","gender","faith","age","height","weight","inspiration","baseHitPoints","removedHitPoints","bonusHitPoints","overrideHitPoints","temporaryHitPoints","alignmentId","currentXp","lifestyleId","skillProficienciesDescription"]
  classlist=['type','subType','friendlyTypeName','friendlySubtypeName','isGranted']
  carlist=text.get("character","junk")
  mainout={}
  mainout["characterinfo"]=(getlist(carlist,"modifiers","class",classlist))
  mainout.update(invextract(invget(carlist)))
  mainout.update(statget(carlist))
  mainout.update(dejson(text,"character",list))
  mainout.update(racextract(raceget(carlist)))
  mainout.update(classxtract(classget(carlist)))
  return (mainout)
x=0
final={}
while (x<len(readf(0))):
  final[readf(1)[x]]=asemble(readf(0)[x])
  x=x+1
writef(final)
