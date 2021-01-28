# Notification-module Description

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

# Notification-module Requirements backlog

1- Develop the CRUD ( create, read, update and delete) operations of the "notification templates" and its associated entities.
There are many "ways" to persist these, you can persist them in database or you can persist them in memory ( arrays, lists ,,, etc ). Now you are required to develop At least one of these options or both of them, however you should remember that should NOT affect the interface of CRUD-ing these entities ---meaning--> if you developed one of these options, or the two of them, or switched between the two, this should NOT affect the rest of the module, nor the way the rest of the module is interacting with this specific part.
---- principles to consider/search---> dependency inversion, dependency injection, ORM ( database tables to objects AND objects to database tables ) 

2- Develop a web service to expose the CRUD operations implemented in story 1. MINIMUM 4 endpoints.
this should NOT affect in anyway, the design of the story 1. the code you delivered for story 1 should be the same, you should only expose it through a web service API endpoints.

3- Develop a web service to send a notification mail/SMS.
As discussed in part 2 above, this should not be ACTUALLY sending the notification, but rather preparing the content of the notification and QUEUEING it in some sort of a queue, making it ready to be sent. You should note that Mails and SMS queues should be different from each other, to separate their concerns. ---meaning--> you queue-writing snippet of code, can either write to MAIL queue or SMS queue, based on what the request  demands.
As you can see in the next user story #3, the actual dequeueing of these notifications will be handled by a separate console application!!!! So, your queues must be persisted NOT in memory.
---- principles to consider/search---> creational design patterns, dependency inversion, dependency injection, polymorphism.

4- Develop a console application to de-queue from queues and actually send those notifications.
We won't ask you to actually use a library/3rd-party mail-gatway/SMS-gateway, to send emails or SMS, but you ARE required to MOCK these gateways. ---meaning--> you can replace your mocking, with actual gateway that sends emails or SMS, WITHOUT affecting the rest of the module, nor the way the rest of the module is interacting with this specific part. 
You also may want to log the status ( success / failure ) of these handled dequeued notifications

5- Develop a web service to expose the statistics mentioned in part 4 above. your endpoint should be accepting a date range ( from and to ), and calculate the requested statistics accordingly, along with other parameters ( sms or email ,,,, etc ).
Sprint 3 story

4- Develop a console application to de-queue from queues and actually send those notifications.
We won't ask you to actually use a library/3rd-party mail-gatway/SMS-gateway, to send emails or SMS, but you ARE required to MOCK these gateways. ---meaning--> you can replace your mocking, with actual gateway that sends emails or SMS, WITHOUT affecting the rest of the module, nor the way the rest of the module is interacting with this specific part. 
You also may want to log the status ( success / failure ) of these handled dequeued notifications



