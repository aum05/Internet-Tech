Project 2: Load-balancing across DNS servers
============================================

Group Members
-------------
Aum Pathak (aap273)
Jeffrey Samson (jas1055)

1. Briefly discuss how you implemented the LS functionality of tracking which TS responded to the query and timing out if neither TS responded.
-----------------------------------------------------------------------------------------------------------------------------------------------
We opened a connection between the client and the LS and then the LS and the two TS. We first have the client send a query to the LS and then the LS uses a while loop to continually get queries from the client and forward them to both of the TS. Each TS uses a loop to check its local DNS table and responds with a response. If either of the server responds, the LS forwards the response (hostname IP A) back to the client. If there is no response from either server, then the timeout error is caught using try-except. Once timed-out, the connections between the LS and both the TS are not closed, and the LS sends back a response (Hostname - Error:HOST NOT FOUND) to the client for that particular query. All the processes are run simultaneously using threading, and to track which TS responded to the query, the LS simply waits for a response from both TS. When one TS responds first, it forwards the response to the client and stops looking for an answer from the other TS for that particular query.

2. Are there known issues or functions that aren't working currently in your attached code? If so, explain.
--------------------------------------------------------------------------------------------------------------
All the functions work as intended. We tried to shut the ls, but it doesn't shut down at the moment. However, that doesn't hinder the results.

3. What problems did you face developing code for this project?
------------------------------------------------------------------
Running all three connections simultaneously while processing the queries was an issue, since there was a minor time gap between receiving data from the client and then forwarding it to both the TS. This problem was resolved using threading, however the only issue remaining was to act upon the timeout error, which was resolved by implementing a separate try-except block for each TS.

4. What did you learn by working on this project?
----------------------------------------------------
We learned how to have one server communicate to 2 or more servers at the same time and how to look for responses from multiple servers as opposed to only communicating with one server at a time. We also learned how useful threading can be when we need multiple processes to run simultaneously.
