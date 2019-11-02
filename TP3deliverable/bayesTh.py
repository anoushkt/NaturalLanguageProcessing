import math
from viterbi import*
training={ 
'greetings':["Hi","Hello","Hey","I want to talk"],'weather':["How cold will it get?","How cold is it today?","What is the weather today?","How hot will it get today?","What is the weather like?","How is the weather today","weather","cold","How hot is the weather","Is it cold today"],
'restaurant':["Italian food",
"I want food",
"I need food",
"Asian food",
"Asian restaurant","Russian food","egyptian food","I want indian food","I want food","Find me some italian restaurants","I am hungry"],
'news':["International news",
"news about the world",
"national news","I want news","world news","US news","technology","tech news","world","I need news"],
'genQues':['How are you','What is new','What are you doing','Who are you',"How are you doing?","How are you doing","What's new in your life","What is your job","How do you do this?"]
    }

def probOfClass():
    totalNoOfSent=0
    prob={}
    for item in training:
        length=len(training[item])
        totalNoOfSent+=length
    for item in training:
        prob[item]=len(training[item])/totalNoOfSent
    return prob

def totalV():
    setOfWords=set()
    for item in training:
        for sent in training[item]:
            for word in sent:
                if word not in setOfWords:
                    setOfWords.add(word)
    return len(setOfWords)

def noOfWordsClass(className):
    noOfWords=0
    for sent in training[className]:
        for word in sent:
            noOfWords+=1        
    return noOfWords

def noOfOccurences(className,wordNeeded):
    noOfWords=0
    for sent in training[className]:
        for word in sent:
            if word==wordNeeded:
                noOfWords+=1        
    return noOfWords
    
        

def classifier(sent):
    prob=probOfClass()
  
    probClassesSent={}
    for classes in training:
        probClassSent=1
        for word in sent:
            p_c=prob[classes]
           
            noOfTimes=noOfOccurences(classes,word)
          
    
            totalNo=noOfWordsClass(classes)
            p_word_c=((noOfTimes+1)/(totalNo+totalV()))
            p_c_word=((p_word_c)*(p_c))
            probClassSent*=p_c_word
        
        probClassesSent[classes]=probClassSent
        
    max=0
    classProb=''
    for classes in probClassesSent:
        if probClassesSent[classes]>max:
            classProb=classes
            max=probClassesSent[classes]
    return classProb
def getValueOfEntity(sent):
    entity=classifier(sent)
    viterbi = ViterbiDecode()
    viterbi.load()
    taggedSent=viterbi.viterbi_algorithm('* * '+ sent)
    print(taggedSent)
    print(entity)
    quesType=''
    cuisineType=''
    newsType=''
    greet=False
    wanted=''

    if(entity=='news'):
        taggedSent=taggedSent.split()
        print(taggedSent)
        if(len(taggedSent)==2):
            newsType=taggedSent[-2].split('/')[0]
        else:
        
            if(taggedSent[-1].split('/')[1]=='n'):
                newsType=taggedSent[-2].split('/')[0]
        return (entity,newsType)


    elif(entity=='restaurant'):
        taggedSent=taggedSent.split()
        print(taggedSent)
        if(len(taggedSent)==2):
            cuisineType=taggedSent[-2].split('/')[0]
        else:
        
            if(taggedSent[-1].split('/')[1]=='n'):
                cuisineType=taggedSent[-2].split('/')[0]
        return(entity,cuisineType)
    elif entity=='greetings':
        return True
        
    
    elif(entity=='genQues'):
        print('ok')
        taggedSent=taggedSent.split()
        if taggedSent[0].split('/')[1]=='qt':
            qType='What'
            thing=taggedSent[1:]
            return (qType,thing)
        else:
            print('here')
            qType='How'
            thing=taggedSent[1:]
            return (qType,thing)
    elif(entity=='weather'):
        taggedSent=taggedSent.split()
        for i in range(0,len(taggedSent)-1):
                if taggedSent[i].split('/')[1]=='wt' and taggedSent[i+1].split('/')[1]=='v' :
                    wanted=taggedSent[i].split('/')[0]
                    
        return(wanted)

print(getValueOfEntity("How hot is it today"))

        
            

            
        
    
    
                
        
        
    
        
    
    
    

