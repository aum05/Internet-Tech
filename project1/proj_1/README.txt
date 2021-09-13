PROJECT 1
=========

Names and NetIDs
-----------------
Jeffrey Samson (jas1055)
Aum Pathak (aap273)


1. Briefly discuss how you implemented your iterative client functionality.
---------------------------------------------------------------------------
We use a for loop to iterate over each line in PROJI-HNS.txt and send each line as a query to the root server. The root-server then searches for the queried hostname in its DNS_table (implemented using a dictionary), if the queried hostname matches the hostname in the DNS_table of the root server it sends the entry as a string in the format: Hostname IPaddress A. If the hostname is not present it responds with the string: TSHostname - NS. We then check, in the client, if the flag "A" is present or not. If it is, then the string received from the root-server is outputted in the file RESOLVED.txt. But if the flag "NS" is present in the string returned by the root-server, we extract the hostname for the top-level server (TSHostname) to create and open a connection between the top-level server and the client. Once the connection is established, the hostname queried to the root-server is then sent to the top-level server as a query. Then the top level server performs a lookup in the DNS_table. If the hostname is present, the top-level server sends back the hostname along with its IP address and the flag 'A'. But if the hostname is not found the top-level server sends back an error message: Hostname - Error:HOST NOT FOUND. Whatever, the final message by the top-level is, we store that string in the output file RESOLVED.txt. This process is repeated until the loop ends and all the hostnames in PROJI-HNS.txt are resolved.

2. Are there known issues or functions that aren't working currently in your attached code? If so, explain.
-----------------------------------------------------------------------------------------------------------
There are no issues, all the code works as expected.

3. What problems did you face developing code for this project?
---------------------------------------------------------------
We had slight difficulties implementing a method to send all the hostnames in PROJI-HNS.txt as messages in one go.

4. Reflect on what you learned by working on this project. 
----------------------------------------------------------
We learned how to set up connections between the client and servers and how to send and recieve multiple messages/data between the client and server.