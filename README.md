# Notification-module

1- Notification "Templates" management
This software  send different types of "notifications", surely the "content" of the "registration activation mail" is different from the "content" of the "forget password mail", which in turn is different from the "content" of "your booking sms confirmation message", right ? 
The notifications module, manages those different notification "templates", and the languages these templates can be sent in, and of course the "placeholders" within the content of these templates to be replaced with "actual values"

ex: " Dear {x} , your booking of the {y} is confirmed. thanks for using our store :) " 
this would be the template , but when the system "sends" it to the user "hassan" who bought the item "mobile charger" , the actual email would be 
" Dear hassan, your booking of the item mobile charger is confirmed, thanks for using our store :) "

So, the "management" of those notifications templates, their subjects, content, available languages, available channels ( email , sms ) , and placeholders would be the focus of this part.


2- Notification "Queuing"
When your "notifications module" gets invoked to send a "notification" to an email address or phone number(out of scope), it would be a good design decision to  actually send the notification 

3- Notification "sending/ Queue handling"
This part would be the responsible of actual de-queue-ing from the "ready-to-send notifications queue", and send "handle/send" it , as well as handling  the unsuccessfully sent notifications.

4- Notifications Statistics 
The Module should provide some statistics to the overall software. The target of these statistics is to provide a vision about the notifications that are sent successfully, as well as the ones are not handled and the reason why they are NOT handled. These Statistics like
1- Number of successfully sent notifications ( per type, for example , how many successful mails and SMS messages ).
2- Number of unsuccessfully sent notifications, and the failure reason enumerated.
3- The most notified email-address/phone-number.
4- The most sent notification template ( that should give an insight, about what part of our whole software is being used the most, hence the most number of notifications sent out of that module ).
