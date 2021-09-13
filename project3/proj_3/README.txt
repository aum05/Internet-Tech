Project 3: Can you set up your own IP network?
==============================================

Question 0 - Please write down the full names and netIDs of all your team members.
----------------------------------------------------------------------------------
Jeffrey Samson - jas1055
Aum Pathak - aap273

Question 1 - Briefly discuss how you implemented each functionality: setting up interfaces, setting up default routes, and setting upper-destination routes.
----------------------------------------------------------------------------------------------------

We used the *ip addr add* command to set up the interfaces. For instance:
`h1 ip addr add 10.0.0.2 dev h1-eth0`

To set up default routes we used the *ip route add* command. For instance:
`h1 ip route add default via 10.0.0.2 dev h1-eth0`

To set up per destination routes we used the r1 *ip route add* command like this:
`r1 ip route add 10.0.0.2 dev r1-eth1`

Question 2 - Are there known issues or functions that aren't working currently in your attached code? If so, explain.
----------------------------------------------------------------------------------------------------
No known issues

Question 3 - What problems did you face developing code for this project?
----------------------------------------------------------------------------------------------------
Only issue was discerning the correct format for the commands that were needed to get the desired output.

Question 4 - What did you learn by working on this project?
----------------------------------------------------------------------------------------------------
We learned how to use ip commands to examine our own networks in a linux based environment. We also learned how to setup a virtual linux based environment in our personal computer systems. 