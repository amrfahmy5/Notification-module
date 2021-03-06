from collections import deque
from  SignNotification import signNotification
from  BookingNotification import bookingNotification
from copy import copy
import sys

from config import likeDB



class Main:
    sucuessMessage,faildMessage= 0,0
    Messages = deque()
    notfiyBooking = bookingNotification()
    notfiySign = signNotification()

    #build queue
    def intilaizeMessage(self,templateMessage,parameter,recieverMail,recieverMobile):
        Temp = copy(templateMessage)
        for i in parameter:
            Temp.content = Temp.content.replace("{a}", i,1)
        self.Messages.append({'temp':Temp,'mail':recieverMail,'mobile':recieverMobile})
        likeDB.saveObject("readyMessage", self.Messages)
        
        
        
        
        
    # Removing elements from a queue
    def sendMessage(self,senderMail,senderPassword):
        from  SendActualMessage import ActualMessage
        AM = ActualMessage(senderMail,senderPassword)
        while self.Messages :
            try:
                AM.SendMessage(self.Messages[0]['mail'],
                               self.Messages[0]['temp'].subject,
                               self.Messages[0]['temp'].content)
                self.sucuessMessage+=1
            except:
                self.faildMessage+=1
                break   
            self.Messages.pop(0) 
        likeDB.saveObject("readyMessage", self.Messages)
        del AM
        
    def makeTemplate(self,idTemp,subject,content,languageNum):
        from  template import template
        from  template import languageEnum
        templateLogin = template()
        templateLogin.id = idTemp
        templateLogin.subject = subject
        templateLogin.content = content
        templateLogin.language = languageEnum(languageNum)
        return templateLogin

#problem in parameter


