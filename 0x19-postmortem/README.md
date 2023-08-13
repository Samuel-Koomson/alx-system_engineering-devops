POST MORTEM

![Alt text](https://i.pinimg.com/736x/70/85/20/708520d02c57e89488edca18ad6545fc--network-cable-tech-humor.jpg)

Summary
On August 11, 2023 between the hours of 14:05 GMT to 14:23 GMT, requests to https://samuelkoomson.com had issues leading to a “Failure to connect to 0 port 80”. The ripple effect was that applications that relied on these servers returned errors and had their performance reduced.
The root cause of the issue stemmed from an invalid Nginx web server configuration and this completely affected traffic to and from the server.
 

 Timelines
14:05 GMT: Nginx server configuration push started
14:08 GMT: System outage starts
14:09 GMT: Configuration failure alerts are sent to team members
14:15 GMT: Reversal of failed Nginx configuration push
14:20 GMT: Nginx configuration push successful
14:21 GMT: Server restart test run successful
14:22 GMT: Server restarted online successfully
14:23 GMT: Full capacity and functionality restored, 100% online traffic running 


Root Cause
A configuration change was released directly to the production environment at 14:05GMT without going through the testing environment. Upon restarting, the change triggered a failure on the Nginx services in the servers.
As a result, all requests to the server were prevented from being handled properly. Calls to provided routes were permanently blocked by the internal monitoring system leading to the failure of all services.
All traffic to the servers were placed in a queue awaiting the availability of a serving thread. Efforts by the servers to restart failed and resulted in an outage starting at 14:08 GMT.


Resolution
Engineers were alerted at 14:08 GMT by the internal monitoring systems who investigated and escalated the issue for resolution. The incident response team found at 14:15 that the internal monitoring system was escalating the issue which was caused by a bug in the server. Attempts to reverse the Nginx configuration push failed. However, it became successful at 14:20 GMT.
To manage the  recovery, Nginx configuration push was passed through the testing environment to make sure that all requirements and bugs were fixed before pushing to the development environment. Server restart tests were success and full functionality was restored at 14:23 rendering a 100% online  traffic to servers on port 80
Corrective & Preventive measures
Following this incident, review and analysis of the outage was performed to put measures in place that will prevent future occurrences. Below are some of the conclusions from the analysis exercise;
All current configuration release mechanisms should be rendered disabled until the implementation of safe measures.
Reversal processes should be made quicker and robust.
Testing of all releases to identify and fix bugs before pushing to the development environment.
Backup servers should be made available to move services while awaiting the resolution of the problem at hand.


Reported by Samuel Koomson

Advanced task 1
Added humour to the post mortem post by adding a picture image of server wiring connections
