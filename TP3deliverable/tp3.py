from bayesTh import * 
from tkinter import *
from image_util import *
import os
import math
here = os.path.dirname(os.path.abspath(__file__))
path=os.path.join(here,"myfile.txt")
def generateResponseNews(newsType):
    print(newsType)
  
    link=''
    if newsType=='US' or newsType=="today's":
        link='https://www.bbc.com/news/world/us_and_canada';
    elif newsType=='world':
        link='https://www.bbc.com/news/world'
    elif newsType=='tech':
        link='https://www.bbc.com/news/technology'
    
    return (link)
import random
def generateResponseGreetings():
    possi=["Hey there!","How can I help you today?"]
    response=random.choice(possi)
    return response

def generateResponseRestaurant(cuisine):
    return "https://www.opentable.com/cuisine/best-"+cuisine[1]+"-restaurants-downtown-pittsburgh-pa"

def generateResponseGenQues(val):
    print('fml')
    qType=val[0]
    if qType=='How':
        return "I am good! You?"
    return ''
class chatBot(object):
    def __init__(self,x,y,size,data):
        robotLink="https://66.media.tumblr.com/4e646f2a515258dbba1437523af8ce34/tumblr_o5mu7lWmgQ1uf5tbgo1_500.gif"
        imageWidth=imageHeight=size
        self.image=PhotoImageFromLink(robotLink, imageWidth, imageHeight)
        
        self.x=x
        self.y=y
        self.chattingText1="How can I help you today?"
        chat1="https://66.media.tumblr.com/730532fad024b50c7d716f68625bb2c8/tumblr_p6ev2g8mmc1vbdodoo1_500.gif"
        self.chattingImage1=PhotoImageFromLink(chat1, imageWidth,imageHeight)
        self.chat1left=0
        self.chat1top=0
        self.typed=''
        self.response='Hey there!'
        self.sendButton=Button(data.width-data.width//20,data.height//20,data.height//20,'send',data,'pink')
        cal1="https://thumbs.gfycat.com/FreeMagnificentCormorant-size_restricted.gif"
        self.cal1image=PhotoImageFromLink(cal1,data.height//5,data.height//5)
        
    def drawRobot(self,canvas):
        robotLeft=x
        robotTop=y
        canvas.create_image(data.imageLeft, data.imageTop,
        anchor=NW, image=self.image)
    def jamieHandler(self):
        text=self.typed
        print(text)
        entity=classifier(text)
        print(entity)
        
        val=getValueOfEntity(text)
        print(val)
        if(entity=='news'):
            print('hereyes')
            self.response=generateResponseNews(val[1])
            
        elif entity=='genQues':
            self.response=generateResponseGenQues(val)
        elif entity=='greetings':
            self.response=generateResponseGreetings()
        elif entity=='restaurant':
            self.response=generateResponseRestaurant(val)
        elif entity=='weather':
            self.response=''
            if val=='cold':
                self.response="It is very cold!"
            if val=='hot':
                self.response="It is freezing"
            self.response=self.response+"\n"+'https://weather.com/weather/tenday/l/Pittsburgh+PA+USPA1290:1:US'
        else:
            self.response="IDK"
            
    def mousePressed(self,x,y):
        
        if self.sendButton.clickedInside(x,y):
              self.jamieHandler()
        self.typed=''
    def keyPressed(self,char):
        print('hi')
        self.typed=self.typed+char
      
    def jamieRedrawAll(self,canvas,data):
        canvas.create_image(data.width//4, data.height//4,
        anchor=NW, image=data.robotImage)
        data.button7.drawButton(canvas)
        
        
        canvas.create_rectangle(0,data.height//2+data.height//8,data.width,data.height,fill='purple')
        canvas.create_text(data.width//2,data.height//16,text="Ask me about the weather, restaurants and news!",font="chalkboard 20 bold")
        canvas.create_text(data.width//2-20,data.height//8,text="Type in the box below.Click to reset",font="chalkboard 50 bold")
        canvas.create_text(data.width//6,data.height//2+data.height//6,text=self.typed,font="chalkboard 50 bold")
        canvas.create_text(data.width//2,data.height//5,text=self.response,font="chalkboard 15 bold")
        self.sendButton.drawButton(canvas)

def startStateRedrawAll(canvas,data):
    
    canvas.create_text(data.width//2,data.height//8,text="Welcome!",font="chalkboard 60 bold")
    canvas.create_text(data.width//2-5,data.height//6+data.height//16,text="I am an assistant bot",font="chalkboard 50 bold")
    canvas.create_image(data.width//30,data.height//35,anchor=NW,image=data.chatBot1.cal1image)
    
    data.buttonA.drawButton(canvas)

    
def endDraw(canvas,data):
    canvas.create_text(data.width//2,data.height//2-data.height//8,text="bye",font="chalkboard 100 bold")  
def timerFired(data):
    pass
def chatRedrawAll(canvas,data):
    data.button7.drawButton(canvas)
    canvas.create_text(data.width//2,data.height//8,text="Choose a button",font="chalkboard 100 bold",fill='black')
    for button in [data.buttonB,data.buttonC,data.buttonD]:
        button.drawButton(canvas)
#taken from112website
def readFile(path):
    with open(path, "rt") as f:
        return f.read()
    
#taken from112website
def writeFile(path, contents):
    with open(path, "wt") as f:
        f.write(contents)
        
        f.flush()



nearest={'downtown':['mountWashington','oakland','shadyside','stripDistrict'],'mountWashington':['downtown','stripDistrict','oakland'],'stripDistrict':['downtown','mountWashington','oakland'],'oakland':['downtown','mountWashington','stripDistrict','shadyside'],'shadyside':['downtown','oakland'],'sewickley':['downtown'],'monroeVille':['downtown']}



localities={'downtown':["marketSquare,","fortPittMuseum,","stationSquare"],'stripDistrict':["pamela Diner,","LaPrima"],
            'mountWashington':["duqesneIncline,","emeraldView"],
            'oakland':["carnegieMuseum,","3riversHeritageTrail"],
            'shadyside':["paintMonkey,","biblicalGardens"],
            'sewickley':["Haye clark bridge,","Old economy village"],
            'monroeVille':["Boyce park,","Rivers of steal"]}

def getTimeSandwich(eventTime,events):
    eventTimeStart=eventTime.split('@')[0]
    eventTimeEnd=eventTime.split('@')[1]
    eventTime=(eventTimeStart,eventTimeEnd)
   
    print('events')
    print(events)
    if(events==''):
        return (0,0)
    listOfStartTimes=[]
    for time in events:
        listOfStartTimes.append(time[0])
    listOfStartTimes.sort()
    listOfEndTimes=[]

    for time in events:
        listOfEndTimes.append(time[1])
    if len(listOfStartTimes)==0:
        return(0,0)
    listOfEndTimes.sort()
    if(len(listOfStartTimes)==1):
        print('in')
        endTime=listOfEndTimes[0].split(':')[0]+'.'+listOfEndTimes[0].split(':')[1]
        endTime=float(endTime)
        startTime=listOfStartTimes[0].split(':')[0]+'.'+listOfStartTimes[0].split(':')[1]
        startTime=float(startTime)
        eventBeg=(eventTimeStart.split(':')[0])+'.'+(eventTimeStart.split(':')[1])
        eventBeg=float(eventBeg)
     
        eventEnd=(eventTimeEnd.split(':')[0])+'.'+(eventTimeEnd.split(':')[1])
        eventEnd=float(eventEnd)
        if(endTime<eventEnd):
            if eventEnd<startTime or eventBeg>endTime:
                return(0,0)
            else:
                return (-1,-1)
                    
            
    i=0
    print(eventTime)
    print(len(listOfStartTimes))
    if eventTime[0]>listOfEndTimes[-1]:
        return(0,0)
    if(eventTime[1]<listOfStartTimes[0]):
        return (0,0)
    
    
    while(i<len(listOfStartTimes)-1):
        if(listOfEndTimes[i]<eventTime[0] and listOfStartTimes[i+1]>eventTime[1]):
            endTime=listOfEndTimes[i].split(':')[0]+'.'+listOfEndTimes[i].split(':')[1]
            startTime=listOfStartTimes[i+1].split(':')[0]+'.'+listOfStartTimes[i+1].split(':')[1]
            print("here"+ startTime+endTime)
            return(endTime,startTime)
        i=i+1
    return(-1,-1)
    
def getLocationSandwich(eventBeforeEnd,eventAfterStart,events): #things to do
    eventBeforeEnd=str(eventBeforeEnd)
    eventBeforeEnd=eventBeforeEnd.split('.')[0]+':'+eventBeforeEnd.split('.')[1]
    eventAfterStart=str(eventAfterStart)
    eventAfterStart=eventAfterStart.split('.')[0]+':'+eventAfterStart.split('.')[1]
    
    locations=[0]*2
    for time in events:
        print('fo')
        if(time[1]==eventBeforeEnd):
            locations[0]=events[time][1]
        if(time[0]==eventAfterStart):
            locations[1]=events[time][1]
        print(locations)
    print(locations)
    return locations
            
        
    



def entertainment(location):
    return localities[location]
def optimise(data):
    possibilities={}
    if data.cal.type=='fixed':
        print('hi')
        for dates in range (1,30):
            print(dates)
            data.cal.date=dates
            data.cal.dayToDraw={}
            events=getCurrData(data)
            if(len(events)==0):
                continue
            [eventBeforeEnd,eventAfterStart]=getTimeSandwich(data.cal.eventTime,events)
            print([eventBeforeEnd,eventAfterStart])
         
            if(eventBeforeEnd,eventAfterStart)==(-1,-1):
                continue
            if ((eventBeforeEnd,eventAfterStart)!=(0,0)): #its not just one event for the day
               
                (eventBeforeLocation,eventAfterLocation)=getLocationSandwich(eventBeforeEnd,eventAfterStart,events)
                optimal=1
                print(eventBeforeLocation,eventAfterLocation)
                if (isNear(eventBeforeLocation,data.cal.eventLocation) and isNear(eventAfterLocation,data.cal.eventLocation)):
                    optimal+=1 
                    eventBeforeEnd=float(eventBeforeEnd)
                    eventAfterStart=float(eventAfterStart)
                    eventBeg=(data.cal.eventTime.split('@')[0])
                    eventBeg=float(eventBeg.split(':')[0])+float(eventBeg.split(':')[1])
                    eventEnd=(data.cal.eventTime.split('@')[1])
                    eventEnd=float(eventEnd.split(':')[0])+float(eventEnd.split(':')[1])
                    
                    
                    if(eventBeg-eventBeforeEnd)<1:
                            optimal+=2
                    if eventBeg-eventBeforeEnd>=1 and eventAfterStart-eventEnd<=3 :
                            thingsToDo=entertainment(data.cal.eventLocation)
                            
                            optimal+=1
                    possibilities[dates]=[thingsToDo,optimal]
                
            
            else:
                thingsToDo=entertainment(data.cal.eventLocation)
                optimal=1
                possibilities[dates]=[thingsToDo,optimal]
        return possibilities
                
                
    
    #not fixed time
    
    elif data.cal.type=='variable':
        for dates in range (1,30):
          
            data.cal.date=dates
            data.cal.dayToDraw={}
            events=getCurrData(data)
            print('jjj')
            print(data.cal.eventLocation)
            if(len(events)==0):
                print("date")
                
                continue
            for i in (range(len(events)-1)):
                firstTime,firstLocation=eventDetails(events,i+1)
                print(firstLocation)
                print(firstTime)
                secondTime,secondLocation=eventDetails(events,i+2)
                print(secondTime)
                print(secondLocation)
                firstTime[0]=float(firstTime[0].split(':')[0])+float(firstTime[0].split(':')[1])
                firstTime[1]=float(firstTime[1].split(':')[0])+float(firstTime[1].split(':')[1])
                secondTime[0]=float(secondTime[0].split(':')[0])+float(secondTime[0].split(':')[1])
                secondTime[1]=float(secondTime[1].split(':')[0])+float(secondTime[1].split(':')[1])
                if(secondTime[0]-firstTime[1]<int(data.cal.eventLength)):
                    o=-1
                    continue
                if(isNear(firstLocation,data.cal.eventLocation) and isNear(secondLocation,data.cal.eventLocation)):
                    o=1
                #get break after event
                possiTime1=firstTime[1]+0.30
                if(possiTime1%10>=6):
                    possiTime1=int(possiTime1)+1+(6-possiTime1%10)
                thingsToDo=entertainment(secondLocation)
                    
                #get break before event
                possiTime2=secondTime[0]-0.30-int(data.cal.eventLength)
                if(possiTime2%10>=6):
                    possiTime2=int(possiTime2)+1+(6-possiTime2%10)
                thingsToDo=entertainment(firstLocation)
                possibilities[dates]=[[possiTime1,thingsToDo],[possiTime2,thingsToDo]]
                
        if possibilities=={}:
            possibilities='No optimal schedules found!!'
        return possibilities
  
                    
                
    
   
                    
                
    
    
def isNear(loc1,loc2):
    if(loc1==loc2):
        return True
  
    if loc1 in nearest[loc2]:
        return True
    
    
def eventDetails(events,eventNo):
    listOfStartTimes=[]
    for time in events:
        listOfStartTimes.append(time[0])
    listOfStartTimes.sort()
    reqdTime=listOfStartTimes[eventNo-1]
    for time in events:
        if time[0]==reqdTime:
            loc=events[time][1]
            return ([time[0],time[1]],loc)

def isLegal(time,eventTime,events):
    listOfStartTimes=[]
    for time in events: 
        listOfStartTimes.append(time[0])
    listOfStartTimes.sort()
    i=listOfStartTimes.find(time[0])
    eventReqd1=eventDetails(events,i+1)
    eventsReqd2=eventDetails(event,i-1)
    if(eventsReqd1[0]<time[1]) or (eventsReqd2[1]>time[0]): #clash
        return False
    return True


def prevEndTimes(time,event):
    listOfStartTimes=[]
    for times in events:
        listOfStartTimes.append(times[0])
    listOfStartTimes.sort()
    ind=listOfStartTimes(time[0])
    start,end=(eventDetails(events,ind-1))
    return end
    
    
class Button(object):
    def __init__(self,x,y,r,text,data,fill='red'):
        self.centreX=x
        self.type=''
        self.centreY=y
        self.radius=r
        self.text=text
        self.fill=fill
        self.t=-1
    def clickedInside(self,x2,y2):
        d = ((self.centreX - x2)**2 + (self.centreY - y2)**2)**0.5
        
        
        if(d <= self.radius):
            if(self.t==-1):
                self.fill='pink'
                self.t*=-1
            else:
                self.fill='blue'
                self.t*=-1
            return True
    def __repr__(self):
        return self.text
    def getText(self):
        return self.text
    def getColor(self):
        return self.fill
    def drawButton(self,canvas):
        
        
        canvas.create_oval(self.centreX-self.radius, self.centreY-self.radius,
                           self.centreX+self.radius, self.centreY+self.radius,
                           fill=self.fill)
        canvas.create_text(self.centreX, self.centreY, text=self.text,font='chalkboard 18 bold')
    def changeText(self,text):
        self.text=text     
    def deselect(self):
        if self.fill=='pink':
            self.fill='blue'
def init(data):
    
    robotLink="https://66.media.tumblr.com/4e646f2a515258dbba1437523af8ce34/tumblr_o5mu7lWmgQ1uf5tbgo1_500.gif"
    data.robotImage = PhotoImageFromLink(robotLink, data.width//2, data.height//2)
    data.cal=calender(data)
    data.modeMain='startState'
    data.chatBot1=chatBot(data.width//2,data.height//2,data.width//10,data)
    data.buttonA=Button(data.width-data.width//8,data.height//2,data.width//10,'click to begin',data,fill='pink')
    data.buttonB=Button(data.width//2,data.height//2-data.height//4,data.width//15,'chat',data,fill='blue')
    data.buttonC=Button(data.width//2,data.height//2,data.width//15,'calender',data,fill='green')
    data.buttonD=Button(data.width//2,data.height//2+data.height//4,data.width//15,'exit',data,fill='purple')
    data.months={'January':[2,31],'February':[5,28],'March':[5,31],'April':[1,31],'May':[3,31],'June':[0,30],'July':[1,31],'August':[4,31],'September':[0,30],'October':[2,31],'November':[5,30],'December':[0,31]}
    data.monthList= ['January','February','March','April','May','June','July','August','September','October','November','December']
    data.pathList={}
    for month in data.monthList:
        path="/Users/anoushkatiwari/TP3deliverable/" + month +'.txt'
        data.pathList[month]=path
    data.button1=Button(data.width//20,data.height//30,data.width//35,"Previous",data,'brown')
    data.button2=Button(data.width-data.width//20,data.height//30,data.width//35,"Next",data,'brown')
    data.button3=Button(data.width-data.width//10,data.height//15,data.width//15,"Add event",data,'brown')
    data.button4=Button(data.width//2,data.height//2 -data.height//4,data.width//10,"Enter the time",data,'blue')
    data.button5=Button(data.width//2,data.height//2,data.width//10,"Enter the name of the event",data,'blue')
    data.button6=Button(data.width//2,data.height//2 + data.height//4,data.width//10,"Enter location",data,'blue')
    data.button7=Button(data.width//2-data.width//4,data.height//30,data.width//35,"Back",data,'green')
    data.button8=Button(data.width//2+data.width//4,data.height//30,data.width//35,"Optimise",data,'brown')
    data.button9=Button(data.width//2-data.width//4,data.height//2-data.height//4,data.height//8,'Enter name',data)
    data.button10=Button(data.width//2+data.width//4,data.height//2-data.height//4,data.height//8,'Enter location',data)
    data.button11=Button(data.width//2-data.width//4,data.height//2+data.height//5,data.height//8,'Enter time',data)
    data.button12=Button(data.width//2+data.width//4,data.height//2+data.height//5,data.height//8,'Done?',data)
    data.button13=Button(data.width//2,data.height//2-data.height//8,data.height//10,"Fixed time,variable day",data)
    data.button14=Button(data.width//2,data.height//2+data.height//8,data.height//10,"Variable time and day",data)
  
    data.button16=Button(data.width//2-data.width//4,data.height//2+data.height//5,data.height//8,"Enter length",data)
    #data.button17=Button(data.width-data.width//4,data.height//8+data.height//2, data.height//10,"Enter date",data)
   

def writeData(data):
    path=data.pathList[data.cal.mode]
    currText=readFile(path)
    toWrite=''
    for i in range(0,len(currText.splitlines())):
        if(i!=data.cal.date-1):
            toWrite=toWrite+currText.splitlines()[i]+'\n'
        else:
            toWrite=toWrite+currText.splitlines()[i]+' '+ data.cal.eventTime[0:6]+'$'+data.cal.eventTime[6:]+'#'+ data.cal.eventName+'%'+data.cal.eventLocationation+'\n'
    writeFile(path,toWrite)
        
    
class calender(object):
    def __init__(self,data):
        self.eventLength=''
        self.solutions=''
        self.eventLocation=''
        self.mode='January'
        self.days= ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
        self.months={'January':[2,31],'February':[5,28],'March':[5,31],'April':[1,31],'May':[3,31],'June':[0,30],'July':[1,31],'August':[4,31],'September':[0,30],'October':[2,31],'November':[5,30],'December':[0,31]}
        self.widthOfEach=math.ceil((data.width-(data.width//8))/7)
        self.heightOfEach=math.ceil((data.height-(data.height//16))//7)
        self.mode='January'
        self.day=''
        i=self.months[self.mode][0]
        self.selected=[0,i]
        self.mode1='Month'
        self.date=1
        self.gettingEvent='False'
        self.currEvent=''
        self.eventName=''
        self.eventTime=''
        self.eventLocationation=''
        self.mode2=''
        self.dayToDraw={}
        self.modeHere=''
        self.type=''
        self.imageLink="https://media.giphy.com/media/uXR9GpSKyj60w/giphy.gif"
        self.imageOptimise=PhotoImageFromLink(self.imageLink, data.width, data.height)
        self.prodLink='https://media.tenor.com/images/422ecc99031d1a05332c2ade5f0259f7/tenor.gif'
        self.prodImage=PhotoImageFromLink(self.prodLink, data.width//4, data.height//4)
        self.eventLimits=''
        self.modeIn=''
       
    def drawAMonth(self,canvas,data):
        data.button7.drawButton(canvas)
        canvas.create_rectangle(data.width//16,data.height//16,data.width-(data.width//16),data.height-(data.height//32),fill='black')
        widthOfEach=(data.width-(data.width//8))//7
        x=data.width//8
        for x in range(data.width//16,data.width-(data.width//16),widthOfEach):
            canvas.create_line(x,data.height//32+20,x,data.height-data.height//32,fill='white',width=5)
        heightOfEach=(data.height-(data.height//16))//7
        for y in range(data.height//32+heightOfEach,data.height-(data.height//32),heightOfEach):
            canvas.create_line(data.width//16,y+20,data.width-(data.width//18),y+20,fill='white',width=5)
    def drawTheDay(self,canvas,data):
        
        canvas.create_text(data.width//2,data.height//10,text= data.cal.mode+' '+str(data.cal.date)+','+str(2019),font='chalkboard 30 bold')
        canvas.create_text(data.width//10,data.height//5,text=self.currEvent,font='chalkboard 30 bold')
        data.button3.drawButton(canvas)
        data.button7.drawButton(canvas)
        length=len(data.cal.dayToDraw)
        y=data.height//4
        dy=data.height//10
       
    
        for time in getCurrData(data):
            
            
            canvas.create_text(data.width//10,y,text=time[0][0:5]+'-' +time[1],font='chalkboard 25 bold')
            canvas.create_text(data.width//4+data.width//2,y,text=data.cal.dayToDraw[time][0]+' at '+data.cal.dayToDraw[time][1],font='chalkboard 25 bold') 
            
            
            y+=dy
        
    
   
    def fillTheDays(self,canvas,data):
        
        x=self.widthOfEach
        for day in self.days:
            canvas.create_text(x,data.height//16+20,text=day,fill='white',font='chalkboard 20 bold')
            x+=self.widthOfEach
    
    def drawTheMonth(self,canvas,data):
        #canvas.create_rectangle(0,0,data.width,data.height,fill='white')
        canvas.create_text(data.width//2 ,data.height//30,text=self.mode,fill='black',font='chalkboard 30 bold')
        canvas.create_rectangle((self.selected[1]*(self.widthOfEach))+data.width//16,data.height//32+20+(2*self.heightOfEach)+self.selected[0]*self.heightOfEach,((self.selected[1]+1)*self.widthOfEach)+self.widthOfEach//2,data.height//32 +(self.selected[0]+1)*self.heightOfEach+20+(2*self.heightOfEach),fill='red')

        data.button8.drawButton(canvas)
        if(data.cal.mode!='January'):
            data.button1.drawButton(canvas)
            
        if(data.cal.mode!='December'):    
            
            data.button2.drawButton(canvas)
        
        self.fillTheDays(canvas,data)
        i=self.months[self.mode][0]
      
        
        
        canvas.create_text((i+1)*self.widthOfEach,data.height//5+20,text=str(1),fill='purple',font='chalkboard 20 bold')
        j=2
        for i in range(i+1,7):
            canvas.create_text((i+1)*self.widthOfEach,data.height//5+20,text=str(j),fill='white',font='chalkboard 20 bold')
            j=j+1
        for i in range(0,7):
            canvas.create_text((i+1)*self.widthOfEach,data.height//5 + self.heightOfEach+20,text=str(j),fill='white',font='chalkboard 20 bold')
            j=j+1
        for i in range(0,7):
            canvas.create_text((i+1)*self.widthOfEach,data.height//5 +(2*self.heightOfEach)+20,text=str(j),fill='white',font='chalkboard 20 bold')
            j=j+1
        for i in range(0,7):
            canvas.create_text((i+1)*self.widthOfEach,data.height//5 +(3*self.heightOfEach)+20,text=str(j),fill='white',font='chalkboard 20 bold')
            j=j+1
        for i in range(0,7):
            canvas.create_text((i+1)*self.widthOfEach,data.height//5 +(4*self.heightOfEach)+20,text=str(j),fill='white',font='chalkboard 20 bold')
            j=j+1
            if(j>self.months[self.mode][1]):
                break
    def drawGettingEvent(self,canvas,data):
        data.button7.drawButton(canvas)
        canvas.create_image(0, 0,
        anchor=NW, image=self.imageOptimise)
        canvas.create_text(data.width//2,data.height//16,text="Enter time as startTime@endTime(24h)",font='chalkboard 10 bold')
        data.button4.drawButton(canvas)
        data.button5.drawButton(canvas)
        data.button6.drawButton(canvas)
    
    def drawOptimisingOptions(self,canvas,data):
        data.button7.drawButton(canvas)
        
        
        canvas.create_text(data.width//2,data.height//8,text='Choose an option',font='chalkboard 40 bold')
        
        data.button13.drawButton(canvas)
        data.button14.drawButton(canvas)
        
    def drawFixedOptimising(self,canvas,data):
       
        canvas.create_image(0, 0,
        anchor=NW, image=self.imageOptimise)
        canvas.create_image(data.width//3,data.height//3,
        anchor=NW, image=self.prodImage)
        canvas.create_text(data.width//2,data.height//16,text="Enter time as startTime@endTime(24h)",font='chalkboard 20 bold')
        data.button7.drawButton(canvas)
            
        data.button12.drawButton(canvas)
        data.button9.drawButton(canvas)
        data.button10.drawButton(canvas)
        data.button11.drawButton(canvas)
    def drawVariableTime(self,canvas,data):
        canvas.create_text(data.width//2,data.height//16,text="Enter time as startTime@endTime(24h)",font='chalkboard 10 bold')
        data.button7.drawButton(canvas)
        data.button12.drawButton(canvas)
        data.button10.drawButton(canvas)
        data.button9.drawButton(canvas)
        data.button16.drawButton(canvas)
    def drawSolutions(self,canvas,data):
        data.button7.drawButton(canvas)
        i=0
        if(type(data.cal.solutions)==str):
            canvas.create_text(data.width//2,data.height//8+data.height//4,text=data.cal.solutions)
       
      
        if(data.cal.mode1=='fixedTime'):
        
            canvas.create_text(data.width//20,data.height//8,text="date",font='chalkboard 20 bold')
            canvas.create_text(data.width//2,data.height//8,text="Things to do",font='chalkboard 20 bold')
            canvas.create_text(data.width//2+data.width//4,data.height//8,text="Score",font='chalkboard 20 bold')
            
            for date in data.cal.solutions:
               
                canvas.create_text(data.width//20,data.height//4+i,text=date,font='chalkboard 20 bold')
                canvas.create_text(data.width//3,data.height//4+i,text=data.cal.solutions[date][0],font='chalkboard 20 bold')
                canvas.create_text(data.width//2+data.width//4,data.height//4+i,text=data.cal.solutions[date][1],font='chalkboard 20 bold')
                i=i+data.height//10
        else:
            canvas.create_text(data.width//20,data.height//8,text="date",font='chalkboard 30 bold')
            canvas.create_text(data.width//2,data.height//8,text="Time",font='chalkboard 30 bold')
            canvas.create_text(data.width//2+data.width//4,data.height//8,text="Things to do",font='chalkboard 30 bold')
            per=data.height//10
            for date in data.cal.solutions:
                canvas.create_text(data.width//8,data.height//4+i,text=date,font='chalkboard 20 bold')
                canvas.create_text(data.width//2,data.height//4+i,text=data.cal.solutions[date][0][0],font='chalkboard 20 bold')
                canvas.create_text(data.width//2+data.width//4,data.height//4+i,text=data.cal.solutions[date][0][1],font='chalkboard 20 bold')
                canvas.create_text(data.width//2,data.height//4+i+per,text=data.cal.solutions[date][1][0],font='chalkboard 20 bold')
                canvas.create_text(data.width//2+data.width//4,data.height//4+i+per,text=data.cal.solutions[date][1][1],font='chalkboard 20 bold')
                
                
                
                
                
                
            
        
        

def keyPressed(event,data):
    if data.modeMain=='Chat':
        data.chatBot1.keyPressed(event.char)

    if(data.modeMain=='Calender'):
        
            
        if(data.cal.mode1=='Month'):
            if(event.keysym=='Up'):
                data.cal.selected[0]-=1
            if(event.keysym=='Down'):
                data.cal.selected[0]+=1
            if(event.keysym=='Right'):
                data.cal.selected[1]+=1
            if(event.keysym=='Left'):
                data.cal.selected[1]-=1
        if( data.cal.gettingEvent=='True'):
            if data.button4.getColor()=='pink':
                data.cal.eventTime= data.cal.eventTime+ event.char
                data.button4.changeText(data.cal.eventTime)
                if(len(data.cal.eventTime)>=11):
                    writeData(data)
            if data.button5.getColor()=='pink':
                data.cal.eventName= data.cal.eventName+ event.char
                data.button5.changeText(data.cal.eventName)
            if data.button6.getColor()=='pink':
                data.cal.eventLocationation= data.cal.eventLocationation+ event.char
                data.button6.changeText(data.cal.eventLocationation)
            if(len(data.cal.eventTime)==11 and data.cal.eventLocationation!=''):
                writeData(data)
        if data.cal.mode1=="fixedTime":
            if data.cal.mode2=='gettingName':
                data.cal.eventName=data.cal.eventName+event.char
                data.button9.changeText(data.cal.eventName)
            if data.cal.mode2=='gettingTime':
            
                data.cal.eventTime=data.cal.eventTime+event.char
                data.button11.changeText(data.cal.eventTime)
            if data.cal.mode2=='gettingLoc':
                data.cal.eventLocation=data.cal.eventLocation+event.char
                data.button10.changeText(data.cal.eventLocation)
        if data.cal.mode1=='variableTime':
            if data.cal.mode2=='gettingLength':
                data.cal.eventLength=data.cal.eventLength+event.char
                data.button16.changeText(data.cal.eventLength)
            elif data.cal.mode2=='gettingName':
                data.cal.eventName=data.cal.eventName+event.char
                data.button9.changeText(data.cal.eventName)
            elif data.cal.mode2=='gettingLoc':
                data.cal.eventLocation=data.cal.eventLocation+event.char
                data.button10.changeText(data.cal.eventLocation)
        

        
def getCurrData(data):        
    path=data.pathList[data.cal.mode]
    reqdDate=int(data.cal.date)
   
 
    currentText=readFile(path).splitlines()[reqdDate-1]
    
    events=currentText.split('-')[1]
    for event in events.split(' '):

        try:    
          
          
            time=event.split('#')[0]
            nameDetails=event.split('#')[1]
            
            start=time.split('$')[0][0:-1]
            end=time.split('$')[1]
            name=nameDetails.split('%')[0]
            
            
            
            location=nameDetails.split('%')[1]
            
           
            data.cal.dayToDraw[(start,end)]=(name,location)
        
        except:
            continue
    
    return(data.cal.dayToDraw)
                
            
            
            
        
def mousePressed(event,data):
    if data.button7.clickedInside(event.x,event.y):
                init(data)
    if(data.modeMain=='startState'):
       
        if data.buttonA.clickedInside(event.x,event.y):
            data.modeMain='menuState'
 
    elif(data.modeMain=='menuState'):
    
        if data.buttonB.clickedInside(event.x,event.y):
            data.modeMain='Chat'
                    
        elif data.buttonC.clickedInside(event.x,event.y):
            data.modeMain='Calender'
                  
        elif data.buttonD.clickedInside(event.x,event.y):
            data.modeMain='Exit'
                   
    elif data.modeMain=='Chat':
        data.chatBot1.mousePressed(event.x,event.y)

    else:
    
    
            
        if(data.cal.mode1=='Month'):
            ind=data.monthList.index(data.cal.mode)
            if(data.cal.mode!='January'):
                if data.button1.clickedInside(event.x,event.y):        
                    data.cal.mode=data.monthList[ind-1]
            if(data.cal.mode!='December'):    
                if data.button2.clickedInside(event.x,event.y):        
                    data.cal.mode=data.monthList[ind+1]
            if( event.x>data.width//16 and event.y>data.height//32+ data.cal.heightOfEach+20 and event.x<data.width-data.width//26 and event.y<data.height-data.height//32):
                data.row=(event.y-data.height//32)//data.cal.heightOfEach
                data.col=(event.x-data.height//16)//data.cal.widthOfEach
                data.cal.date=data.col+(7*(data.row-1))-data.cal.months[data.cal.mode][0]+1
                data.cal.mode1='day'
                data.dayToDraw=getCurrData(data)
               
        
        if(data.cal.mode1=='day' and data.button3.clickedInside(event.x,event.y)==True):
            data.cal.gettingEvent='True'
            
        if(data.cal.gettingEvent=='True'):
            if(data.button4.clickedInside(event.x,event.y)):
                data.cal.mode2='time'
                data.button5.deselect()
                data.button6.deselect()
            
            elif data.button5.clickedInside(event.x,event.y):
                data.cal.mode2='name'
                data.button4.deselect()
                data.button6.deselect()
            
            
            elif data.button6.clickedInside(event.x,event.y):
                data.mode3='location'
                data.button4.deselect()
                data.button5.deselect()
        if(data.cal.mode1=='Month'):
                if data.button8.clickedInside(event.x,event.y):
                    data.cal.mode1='optimising'
        if(data.cal.mode1=='optimising'):
    
            if data.button13.clickedInside(event.x,event.y)==True:
                data.cal.mode1='fixedTime'
                data.cal.type='fixed'
            elif data.button14.clickedInside(event.x,event.y)==True:
                data.cal.mode1='variableTime'
                data.cal.type='variable'
            
        if(data.cal.mode1=='fixedTime'):
            if data.button9.clickedInside(event.x,event.y)==True:
                data.cal.mode2='gettingName'
            if data.button10.clickedInside(event.x,event.y)==True:
                data.cal.mode2='gettingLoc'
            if data.button11.clickedInside(event.x,event.y)==True:
                data.cal.mode2='gettingTime'
            if data.button12.clickedInside(event.x,event.y)==True:
                data.cal.mode2='solutions'
                data.cal.solutions=optimise(data)
            
            
        elif data.cal.mode1=='variableTime':
            if data.button9.clickedInside(event.x,event.y)==True:
                data.cal.mode2='gettingName'
            if data.button10.clickedInside(event.x,event.y)==True:
                data.cal.mode2='gettingLoc'
            if data.button16.clickedInside(event.x,event.y)==True:
                data.cal.mode2='gettingLength'
            if data.button12.clickedInside(event.x,event.y)==True:
                data.cal.mode2='solutions'
                
                data.cal.solutions=optimise(data)
                
        
        
def timerFired(data):
    pass
def redrawAll(canvas,data):
    if data.modeMain== "startState":
        canvas.create_image(data.width//4, data.height//4,
        anchor=NW, image=data.robotImage)
        startStateRedrawAll(canvas,data)
        
    if data.modeMain== "menuState":
        
        chatRedrawAll(canvas,data)
    if data.modeMain=='Chat':
       
        data.chatBot1.jamieRedrawAll(canvas,data)
    if data.modeMain=='Exit':
        endDraw(canvas,data)
    if(data.modeMain=='Calender'):
   
        
        data.button7.drawButton(canvas)
        if data.cal.mode2=='solutions':
          
            data.cal.drawSolutions(canvas,data)
        if data.cal.gettingEvent=='True':
            data.cal.drawGettingEvent(canvas,data)
        
    
        if data.cal.mode1=='fixedTime' and data.cal.mode2!='solutions':
            data.cal.drawFixedOptimising(canvas,data)
    
        if data.cal.mode1=='variableTime' and data.cal.mode2!='solutions':
            data.cal.drawVariableTime(canvas,data)
        if(data.cal.mode1=='optimising'):
            data.cal.drawOptimisingOptions(canvas,data)
    
        if(data.cal.mode1=='Month'):
            data.cal.drawAMonth(canvas,data)
            data.cal.fillTheDays(canvas,data)
            data.cal.drawTheMonth(canvas,data)
        if(data.cal.mode1=='day'):
            data.cal.drawTheDay(canvas,data)
    
            
    
        
 



            
            
        
            
####################################
# use the run function as-is
### run taken from 15112 site
####################################
def run(width=300, height=300):
    def redrawAllWrapper(canvas, data):
        canvas.delete(ALL)
        canvas.create_rectangle(0, 0, data.width, data.height,
                                fill='gold', width=0)
        redrawAll(canvas, data)
        canvas.update()

    def mousePressedWrapper(event, canvas, data):
        mousePressed(event, data)
     
        redrawAllWrapper(canvas, data)

    def keyPressedWrapper(event, canvas, data):
        keyPressed(event, data)
        redrawAllWrapper(canvas, data)

    def timerFiredWrapper(canvas, data):
        
        timerFired(data)
        redrawAllWrapper(canvas, data)
        # pause, then call timerFired again
        canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
    # Create root before calling init (so we can create images in init)
    root = Tk()


    # Set up data and call init
    class Struct(object): pass
    data = Struct()
    data.width = width
    data.height = height
    data.timerDelay = 100# milliseconds
    init(data)
    # create the root and the canvas
    canvas = Canvas(root, width=data.width, height=data.height)
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<Key>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    timerFiredWrapper(canvas, data)
    # and launch the app
    root.mainloop()  # blocks until window is closed
    print("bye!")

run(1000,1000)

        
