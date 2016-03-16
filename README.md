
Tournament Results  Version 1.0 03/14/2016

=============================================================

# DESCRIPTION
 Tournament Results is a python module using PostgreSQL database to record player information, including number of matches, times of wins. Based on their record, the program can automatically pair the players based on their score to do the following matches.

=============================================================

# WHAT’S INCLUDED
* tournament.sql
* tournament.py
* tournament_test.py
* README.txt

=============================================================

# FILE DESCRIPTION
* tournament.sql is where we save the program for creating initial tables and views in tournament database. Once running this by using \i tournament.sql under the tournament database, all the tables and views are stored in the database. Thus we only need to add the tables and views once.
* tournament.py is where we generate queries.
* tournament_test.py is where we put some fake data to test if we have the correct result through tournament.py
* README.txt gives you a guide on this tournament result program

=============================================================

# INSTRUCTIONS
1. If necessary, install Vagrant and VirtualBox. Thus the program have the right environment to run on.
2. Open terminal, go to vagrant virtual machine by 'vagrant up' and 'vagrant ssh'.
3. open tournament database in psql by using 'psql tournament' in the terminal.
4. Run \i tournament.psql
5. Quit PostgreSQL by using'\q' in the terminal
6. Run tournament_test.py by using 'python tournament_test.py', you will see the result of swisspairing.
7. If you want to see the result of tournament result again, simply run tournament_test.py again. You do not need to do the procedure 3,4,5.

=============================================================

# CREATOR
Jingjing----http://github.com/jingjingshao