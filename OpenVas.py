from asyncio.windows_events import NULL
from fileinput import close
from re import sub
from telnetlib import IP
import pandas as pd
import time
import numpy as np

import pandas as pd
portUse=[]
data = pd.read_csv('OneNetScan.csv') 
df = pd.DataFrame(data, columns= ['IP','Port'])
M = df['Port'].to_numpy()
M = (M.astype(int))
26
for x in M:
    if x == 21:
        portUse.append("FILE TRANSFER PROTOCOL")
    elif x == 22:
        portUse.append("SSH")
    elif x == 23:
        portUse.append("Telnet")
    elif x == 25:
        portUse.append("SMTP")
    elif x == 80:
        portUse.append("HTTP/ Web Server")
    elif x == 135:
        portUse.append("RPC Client-Server Communication")
    elif x == 389:
        portUse.append("LDAP/Locate Files/Com w/ Directories")
    elif x == 443:
        portUse.append("HTTPS")
    elif x == 444:
        portUse.append("SNPP Servers")
    elif x == 445:
        portUse.append("Active Directory")
    elif x == 465:
        portUse.append("OLD SMTP Port")
    elif x == 475:
        portUse.append("Datagram Protocol")
    elif x == 476:
        portUse.append("TCP")
    elif x == 477:
        portUse.append("IPSec encrypted data streams")
    elif x == 587:
        portUse.append ("encrypt SMTP messages using STARTTLS")
    elif x == 631:
        portUse.append("Internet Printing/Sharing Printers")
    elif x == 636:
        portUse.append("LDAPS/ allows Encryption of LDAP")
    elif x == 1000:
        portUse.append("Network Data Management/Backup of Network Storage")
    elif x == 1163:
        portUse.append("sun cacao rmi registry access point")
    elif x == 1164:
        portUse.append("QSM Proxy Service")
    elif x == 1311:
        portUse.append("Datagram Transmissions")
    elif x == 2022:
        portUse.append("Datagram Transmissions")
    elif x == 3269:
        portUse.append("Global Catalog Port")
    elif x == 2525:
        portUse.append("secure submission of emails for delivery by modern ESPs")
    elif x == 3389:
        portUse.append("RDP/ Remote Desktop Protocol")
    elif x == 3998:
        portUse.append("DNX/ Distributed workload to remote hosts")
    elif x == 3999:
        portUse.append("Norman distributes scanning service")
    elif x == 4353:
        portUse.append("BIG-IP GTM Systems")
    elif x == 5134:
        portUse.append("TCP")
    elif x == 5556:
        portUse.append("Oracle WebLogic Server Node Manager Port")
    elif x == 5580:
        portUse.append("Offline Authentication Service")
    elif x == 5671:
        portUse.append("Azure Service Bus")
    elif x == 5986:
        portUse.append("Powershell Ports")
    elif x == 5989:
        portUse.append("TCP")
    elif x == 6789:
        portUse.append("GSS-API Oracle Remote Administration Daemon")
    elif x == 6788:
        portUse.append("UDP")
    elif x == 7569:
        portUse.append("Dell EqualLogic Host Group Management")
    elif x == 8000:
        portUse.append("Alternative HTTP")
    elif x == 8006:
        portUse.append("Symantec Critical System Protection")
    elif x == 8009:
        portUse.append("Apache Jserv Protocol")
    elif x == 8080:
        portUse.append("HTTP Alternate (see 80)")
    elif x == 8084:
        portUse.append("Audio Video Calls")
    elif x == 8086:
        portUse.append("InfluxDB HTTP Service")
    elif x == 8181:
        portUse.append("HTTPS Port")
    elif x == 8183:
        portUse.append("Time Sensititve Applications")
    elif x == 8184:
        portUse.append("Time Sensititve Applications")
    elif x == 8383:
        portUse.append("Desktop Central Server")
    elif x == 8443:
        portUse.append("Alternative HTTPS")
    elif x == 8444:
        portUse.append("Agents to upload logs to the DSM")
    elif x == 8445:
        portUse.append("SEPM for Reporting Data")
    elif x == 8686:
        portUse.append("JMX Port")
    elif x == 8888:
        portUse.append("NewsEDGE server TCP 1)")
    elif x == 8889:
        portUse.append("VxWorks WDB debug service")
    elif x == 8899:
        portUse.append("OracleVM")
    elif x == 8989:
        portUse.append("TCP")
    elif x == 8999:
        portUse.append("Host On-Demand Clients")
    elif x == 9022:
        portUse.append("TCP")
    elif x == 9080:
        portUse.append("Websphere Liberty Application Server")
    elif x == 9089:
        portUse.append("Converter Standalone versions")
    elif x == 9163:
        portUse.append("TCP")
    elif x == 9164:
        portUse.append("TCP")
    elif x == 9443:
        portUse.append("Alternate SSL Port")
    elif x == 9955:
        portUse.append("TCP")
    elif x == 10000:
        portUse.append("backup of network-attached storage (NAS) devices")
    elif x == 11163:
        portUse.append("sun cacao")
    elif x == 11164:
        portUse.append("computer networking represent communication endpoints")
    elif x == 27017:
        portUse.append("MongoDB Server")
    else:
        portUse.append(NULL)

df = pd.DataFrame({'Port Uuse':portUse})
df.to_csv('test.csv',index=False, encoding='utf-8')


        
        
