import random

# for item in zip(bajeti, domenii):
# 	print(*item, sep=" - ")


# R1: 20Q exact answers
# R2: 20Q closest answers
# R3: 10Q quess the player?

R1 = {
"Fewest PL home defeats in a season": 									"0 - Manchester United (1995/96, 1999/00 & 2010/11) Arsenal (1998/99, 2003/04 & 2007/08) Chelsea (2004/05, 2005/06, 2006/07, 2007/08 & 2014/15) Liverpool (2008/09, 2017/18 & 2018/19)",
"Ever present PL clubs":												"Arsenal Chelsea Everton Liverpool Manchester United Tottenham Hotspur ",
"Clubs avoiding relegation from PL after being bottom at Christmas":	"West Bromwich Albion (2004/05) Sunderland (2013/14) Leicester City (2014/15)",
"Highest PL scoring draw": 												"5-5 - West Bromwich Albion v Manchester United (19 May 2013)",
"Manager of the Month Awards": 											"Alex Ferguson:27 Arsène Wenger:15 David Moyes:10",
">30 goals Highest Scorer > 2010":										"2011-12:30 Goals:Robin van Persie; 2013-14:31 Goals:Luis Suárez; 2017-18:32 Goals:Mohamed Salah",
"Last Top Flight Championship Won: earliest":							"PRESTON NORTH END	1890",
"Most PL points": 														"2,119	Manchester United; 1,907	Arsenal FC; 1,883	Chelsea FC; 1,778	Liverpool FC; 1,545	Tottenham Hotspur",
"All-Time Premier League Top Scorers foreign":							"Sergio Agüero 180; Thierry Henry 175; Robin Van Persie 144",
"Fewest goals scored, consecutive seasons":								"Sunderland, 01-02 29g, 02-03 21g",
"spent longer at the bottom of the table without being relegated than any side in Premier League history":		"In 2014/15, Leicester City (140 days).",
"Only two players have ever scored a hat-trick of headers in a Premier League match":							"Duncan Ferguson for Everton (vs Bolton in December 1997) and Salomon Rondon for West Brom (vs Swansea in December 2016).",
"Only five players have scored five goals in a game in EPL.":			"Alan Shearer, Andy Cole, Jermain Defoe, Dimitar Berbatov and Sergio Aguero",
"Two teams that have both won the EPL and been relegated from it":		"Manchester City and Blackburn Rovers",
"Goalkeepers scoring goals has happened on five occasions in EPL":		"Peter Schmeichel, Brad Friedel, Paul Robinson, Tim Howard, Asmir Begovic",
"the record for quickest Premier League hat-trick":						"Robbie Fowler, Sadio Mane",
"Liverpool’s original kit colors was":									"The club’s original kit was blue and white until 1896",
"‘You’ll Never Walk Alone’ can be heard singing which song": 			"Pink Floyd’s Fearless song",
"Liverpool’s biggest ever win in the Premier League":					"home victory against Southampton in 1999: 7-1",
"Most World Cup goals while a Liverpool player":						"Michael Owen, 4 for England in 1998 and 2002."
}


R2 = {
	"Smallest PL title-winning margin":																						"0 points, +8 goal difference - Manchester City (2011/12)",
	"Most PL defeats in a season*":																							"29 Sunderland (2005/06 - 38 matches)",
	"Most yellow cards in a single PL match":																				"2016 Chelsea - Spurs: 12 ycs",
	"Most consecutive PL defeats":																							"15 - Sunderland (2002/03)",
	"Fewest PL goals scored at home in a season":																			"10 - Manchester City (2006/07), 10 - Huddersfield Town (2018/19)",
	"Worst PL goal difference in a season":																					"-69 - Derby County (2007/08)",
	"Most PL points in a season for a club to be relegated":																"42 - West Ham United (2002/03 - 38 matches)",
	"Fewest goals scored, total":																							"2006-07: 931",
	"You have to go as far back as March 22, 2003 for the last time there was a Premier League game with no substitutes":	"(Man United’s 3-0 victory over Fulham)",
	"Fewest PL goals conceded at home in a season":																			"4 - Manchester United (1994/95)",
	"Fewest PL goals conceded away in a season":																			"9 - Chelsea (2004/05)",
	"Fewest PL points in a season for a club avoiding relegation":															"34 - West Bromwich Albion (2004/05)",
	"Total Premier League Clubs’ Red Cards from 1992-93 to 2019-20":														"Everton	94",
	"Total Premier League Clubs’ Yellow Cards from 1992-93 to 2019-20":														"Chelsea	1640",
	"most appearances in a Liverpool shirt":																				"Ian Callaghan: 857 matches during his 19 years at Anfield",
	"Liverpool FC’s youngest ever starting line-up":																		"19 years and 182 days – Aston Villa in December 2019",
	"Liverpool’s Liver Bird badge has become a symbol":																		"in 1901",
	"Longest-serving player":																								"Elisha Scott, 21 years and 52 days (from 1913 to 1934).",
	"Liverpool Matches played in PL":																						"1,068",
	"Most goals in a debut season:":																						"Mohamed Salah, 44 (during the 2017–18 season)"
}


R3 = {
	"Of all the players to take ten or more spot kicks in the Premier League, only one is to have a 100% success rate.":			"Yaya Toure 11/11",
	"2015/16 was the first time when this team had recorded a positive goal difference in a top-flight season since 1985/86.":		"West Ham",
	"first player to score hat trick in epl.":																						"Eric Cantonna 1992: leeds vs Spurs",
	"Which player took more corners (often badly) than he had shots in the Premier League.":										"Iago Aspas",
	"Which player has missed the most Premier League penalties":																	"Alan Shearer 11",
	"Which player has played the most Premier League games of any player to be substituted off in all of their PL appearances":		"Nuri Sahin (formerly at Liverpool) : 7",
	"Substituted more times than any other player":																					"Ryan Giggs (134).",
	"The only PL players to score a hat-trick entirely from set pieces":															"Wayne Rooney and Matt Le Tissier",
	"Two players have scored Premier League penalties with both feet":																"Bobby Zamora and Obafemi Martins.",
	"There are 3 players to score, assist and score an own goal in a single Premier League game.":									"Wayne Rooney, Gareth Bale and Kevin Davies"
}

L1 = list(R1.items())
random.shuffle(L1)


L2 = list(R2.items())
random.shuffle(L2)


L3 = list(R3.items())
random.shuffle(L3)

i = 0
for Q, A in L1:
	i += 1
	print(f"{i}. {Q}:")
	print(f"\t\t\t\t{A}")

