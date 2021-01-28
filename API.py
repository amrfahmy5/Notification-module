from flask import Flask,session,jsonify, request,render_template,redirect,url_for,request



app = Flask(__name__)
app.config['SECRET_KEY'] = 'oh_so_secret'


from main import Main
from config import likeDB
import sys


main = Main()

t = likeDB.loadObject("notifySign")
main.notfiySign.templates=t if t!=None else []


t = likeDB.loadObject("notfiyBooking")
main.notfiyBooking.templates=t if t!=None else []


t = likeDB.loadObject("readyMessage")
main.Messages=t if t!=None else []

'''
main.notfiySign.templates= likeDB.loadObject("notifySign");
main.notfiyBooking.templates= likeDB.loadObject("notfiyBooking");
main.Messages=likeDB.loadObject("readyMessage")

'''







@app.route('/', methods=['GET'])
def loginGet():
    
    print("login render  ", file=sys.stderr)
    return render_template("logins_signup.html")

@app.route('/book', methods=['GET'])
def bookGet():
    return render_template("rooms.html")

@app.route('/login', methods=['POST'])
def loginPost():
    try :
        requestD = request.get_json()
        email = requestD['recieverMail'] ;
        userName = requestD['userName']
        phone = requestD['recieverMobile'] ;
        password = requestD['password']  
        
        session['email'] =  email
        session['userName'] = userName
        session['phone'] = phone
        session['password'] = password
        NotifyUser(requestD['T_Notfication'],requestD['tID'],email,
                   phone,requestD['Parameter'])
        
        response = jsonify(200)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response


@app.route('/book', methods=['POST'])
def bookPost():
    try:
        print("booking post  ", file=sys.stderr)
        print(session['email'], file=sys.stderr)
        print(session['userName'], file=sys.stderr)
        requestD = request.get_json()
        productName = requestD['productName']
        print(productName, file=sys.stderr)
        productID = requestD['productID'] ;
        T_Notfication = requestD['T_Notfication']
        tID = requestD['tID']
        
        email = session['email'] ;
        print(email, file=sys.stderr)
        userName= session['userName'] 
        phone= session['phone'] 
    
        
        NotifyUser(T_Notfication,tID,email,phone,
                   [userName,productName,productID,phone,email])
        
        
        print("-----------------------------------", file=sys.stderr)
        response = jsonify(200)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response




'''
1-make a template
2- save in array of its notify type
3- save object
'''

@app.route('/notification/add', methods=['POST'])
def add_template():
    try:
        requestD = request.get_json()
        Notification_Type= requestD['T_Notfication']
        #requestD['template'] 
        template= main.makeTemplate(requestD['tID'],
                                    requestD['subject'], 
                                    requestD['content'], 
                                    requestD['languageNum'])
        
        if Notification_Type == 1:
            main.notfiySign.addTemplate(template)
            likeDB.saveObject("notifySign", main.notfiySign.templates);
        elif Notification_Type == 2 :
            main.notfiyBooking.addTemplate(template)
            likeDB.saveObject("notfiyBooking", main.notfiyBooking.templates);
            
        response = jsonify(200)
        response.status_code = 200
        
        
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response

@app.route('/notification/delete', methods=['POST'])
def delete_template():
    try:
        requestD = request.get_json()
        Notification_Type= requestD['T_Notfication']
        tID= requestD['tID']
        if Notification_Type == 1:
            main.notfiySign.deleteTemplate(tID)
            likeDB.saveObject("notifySign", main.notfiySign.templates);
        elif Notification_Type == 2 :
            main.notfiyBooking.deleteTemplate(tID)
            likeDB.saveObject("notfiyBooking", main.notfiyBooking.templates);
        response = jsonify(200)
        response.status_code = 200
        
        
    except Exception as e:
        response = jsonify(str("no template with this id or some error happend"))
        response.status_code = 500
    return response

@app.route('/notification/update', methods=['POST'])
def update_template():
    try:
        requestD = request.get_json()
        Notification_Type= requestD['T_Notfication']
        tID= requestD['tID'] 
        template= main.makeTemplate(tID,
                            requestD['subject'], 
                            requestD['content'], 
                            requestD['languageNum'])
        if Notification_Type == 1:
            main.notfiySign.updateTemplate(tID,template)
            likeDB.saveObject("notifySign", main.notfiySign.templates);
        elif Notification_Type == 2 :
            main.notfiyBooking.updateTemplate(tID,template)
        response = jsonify(200)
        response.status_code = 200
        
        
    except Exception as e:
        response = jsonify(str("no template with this id or some error happend"))
        response.status_code = 500
    return response

@app.route('/notification/get', methods=['POST'])
def get_template():
    try:
        requestD = request.get_json()
        tID= requestD['tID']
        Notification_Type= requestD['T_Notfication']
        if Notification_Type == 1:
            Template = main.notfiySign.getTemplate(tID)
        elif Notification_Type == 2 :
            Template = main.notfiyBooking.getTemplate(tID)
        response = jsonify({'subject':Template.subject,
                            'content':Template.content,
                            'id':Template.id
                            
                            
                            })
        response.status_code = 200
    except Exception as e:
        response = jsonify(str("no template with this id or some error happend"))
        response.status_code = 500
    return response




def NotifyUser(Notification_Type,tID,recieverMail,recieverMobile,Parameter):
    if Notification_Type == 1:
            resultTemp = main.notfiySign.getTemplate(tID)
    elif Notification_Type == 2 :
            resultTemp = main.notfiyBooking.getTemplate(tID)

    main.intilaizeMessage(resultTemp,Parameter,recieverMail,recieverMobile)
    
@app.route('/notification/Notfiy', methods=['POST'])
def Notify():
    try:
        requestD = request.get_json()
        tID= requestD['tID']
        Notification_Type= requestD['T_Notfication']
        NotifyUser(Notification_Type, tID, requestD['recieverMail'], 
                   requestD['recieverMobile'], requestD['Parameter'])
        response = jsonify(200)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response


@app.route('/readyMessage', methods=['GET'])
def readyMessage():
    try:
        messageReady = []
        for i in main.Messages:
            Template = {'content':i['temp'].content,
                        'subject':i['temp'].subject,
                        'id':i['temp'].id}
            messageReady.append({'temp':Template,'mail':i['mail'],'mobile':i['mobile']})
        response = jsonify(messageReady)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response



@app.route('/sendActualMessage', methods=['GET'])
def AM():
    try:
        main.sendMessage('Testeee999yyy@gmail.com', '12345678m*')
        response = jsonify(200)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response

@app.route('/sucuessFail', methods=['GET'])
def SF():
    try:
        e = 'befor this step you shoud send actual message'
        e+= '      number of sucuess message : '+str(main.sucuessMessage)
        e+= '      number of faild message : '+str(main.faildMessage)
        response = jsonify(e)
        response.status_code = 200
    except Exception as e:
        response = jsonify(str(e))
        response.status_code = 500
    return response




from console import consoleProject 


if __name__ == '__main__':
     app.run(host="localhost", port=8001, debug = True)
     
     
     #consoleRun = consoleProject()
     #main = consoleRun.consoleRun(main)
     

   