#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    conn = connect()
    c = conn.cursor()
    query = c.execute("DELETE FROM matches;")
    conn.commit()
    conn.close()
    


def deletePlayers():
    """Remove all the player records from the database."""
    conn = connect()
    c = conn.cursor()
    query = c.execute("DELETE FROM matches;")
    query = c.execute("DELETE FROM player;")
    conn.commit()
    conn.close()


def countPlayers():
    """Returns the number of players currently registered."""
    conn = connect()
    c = conn.cursor()
    query = c.execute("SELECT count(*) AS num FROM player;")
    count = c.fetchall()   # fetchall() returns a list of your results
    conn.close()
    return count[0][0]
    

def registerPlayer(name):
    """Adds a player to the tournament database.
  
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).
    """
    conn = connect()
    c = conn.cursor()
    query = c.execute("INSERT INTO player (name) VALUES (%s);", (name,))
    conn.commit()
    conn.close()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    conn = connect()
    c = conn.cursor()
    query = c.execute("SELECT * FROM standings")
    count = c.fetchall()
    conn.close()
    return count


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    conn = connect()
    c = conn.cursor()
    query = c.execute("INSERT INTO matches (winner, loser) VALUES (%s, %s);", (winner, loser,))
    conn.commit()
    conn.close()

 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
  
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    conn = connect()
    c = conn.cursor()
    query = c.execute("DROP VIEW IF EXISTS even CASCADE;")
    query = c.execute("DROP VIEW IF EXISTS odd CASCADE;")
    query = c.execute("CREATE VIEW odd AS SELECT * FROM (SELECT ROW_NUMBER() OVER () AS num, * FROM wins) as number  WHERE num % 2 = 1;")
    query = c.execute("CREATE VIEW even AS SELECT * FROM (SELECT ROW_NUMBER() OVER () AS num, * FROM wins) as number  WHERE num % 2 = 0;")
    query = c.execute("SELECT odd.id as id1, odd.name as name1, even.id as id2, even.name as name2 FROM odd, even WHERE odd.num + 1 = even.num;")    
    count = c.fetchall()   # fetchall() returns a list of your results
    conn.close()
    return count

