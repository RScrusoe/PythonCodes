###
#   4 IS UNIVERSAL
#   EVERY NUMBER TO WORD ENDS UP AT 4
###

def numToWords(num,join=True):
    '''words = {} convert an integer number into words'''
    units = ['','one','two','three','four','five','six','seven','eight','nine']
    teens = ['','eleven','twelve','thirteen','fourteen','fifteen','sixteen', \
             'seventeen','eighteen','nineteen']
    tens = ['','ten','twenty','thirty','forty','fifty','sixty','seventy', \
            'eighty','ninety']
    thousands = ['','thousand','million','billion','trillion','quadrillion', \
                 'quintillion','sextillion','septillion','octillion', \
                 'nonillion','decillion','undecillion','duodecillion', \
                 'tredecillion','quattuordecillion','sexdecillion', \
                 'septendecillion','octodecillion','novemdecillion', \
                 'vigintillion']
    words = []
    if num==0: words.append('zero')
    else:
        numStr = '%d'%num
        numStrLen = len(numStr)
        groups = int((numStrLen+2)/3)
        numStr = numStr.zfill(groups*3)
        for i in range(0,groups*3,3):
            h,t,u = int(numStr[i]),int(numStr[i+1]),int(numStr[i+2])
            g = int(groups-(i/3+1))
            if h>=1:
                words.append(units[h])
                words.append('hundred')
            if t>1:
                words.append(tens[t])
                if u>=1: words.append(units[u])
            elif t==1:
                if u>=1: words.append(teens[u])
                else: words.append(tens[t])
            else:
                if u>=1: words.append(units[u])
            if (g>=1) and ((h+t+u)>0): words.append(thousands[g]+',')
    if join: return ' '.join(words)
    return words



n = 984648664444384219830980986855667678
while(1):
    if n==4:
        print(4)
        break
    print(str(n) + "  =>  ",end="")
    s = numToWords(n).replace(",","").replace(" ","")
    no_of_words_in_s  = len(s)
    n = no_of_words_in_s
    



def maximum_no_steps(n):
    mx = 0 
    for i in range(1,n):
        ct = 0
        n=i
        while(1):
            if n==4:
                break
            #print(str(n) + "  =>  ",end="")
            s = numToWords(n).replace(",","").replace(" ","")
            no_of_words_in_s  = len(s)
            n = no_of_words_in_s
            ct+=1
        if mx < ct:
            mx = ct
        #print(str(i) + " @@@ " + str(ct))
    print(mx)
        

####  
#    ALTERNATIVE WAY USING INFLECT MODULE
####

import inflect
p = inflect.engine()

p.number_to_words(99)
n = 984648664444384219830980986855667678
while(1):
    if n==4:
        print(4)
        break
    print(str(n) + "  =>  ",end="")
    s = p.number_to_words(n).replace(",","").replace(" ","").replace('-',"")
    no_of_words_in_s  = len(s)
    n = no_of_words_in_s
    