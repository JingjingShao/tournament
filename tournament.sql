-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

CREATE TABLE player (id SERIAL PRIMARY KEY, name TEXT);

CREATE TABLE matches (winner serial REFERENCES player(id), loser serial REFERENCES player(id));

CREATE VIEW wins AS SELECT id, name, count(winner) AS wins 
                 FROM player LEFT OUTER JOIN matches ON winner = id 
                 GROUP BY id 
                 ORDER BY wins;
                 
CREATE VIEW matches_num AS SELECT id, COUNT(winner) AS matches 
                        FROM player LEFT OUTER JOIN matches 
                        ON winner = id OR loser = id GROUP BY id;

CREATE VIEW standings AS SELECT wins.id, name, wins, matches 
                      FROM matches_num, wins WHERE matches_num.id = wins.id 
                      ORDER BY wins DESC;