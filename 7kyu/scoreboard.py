# You are the judge at a competitive eating competition and you need to choose a winner!
#
# There are three foods at the competition and each type of food is worth a different amount of points. Points are as follows:
#
# Chickenwings: 5 points
#
# Hamburgers: 3 points
#
# Hotdogs: 2 points
#
# Write a function that helps you create a scoreboard. It takes as a parameter a list of objects representing the participants, for example:
#
# [
#   {name: "Habanero Hillary", chickenwings: 5 , hamburgers: 17, hotdogs: 11},
#   {name: "Big Bob" , chickenwings: 20, hamburgers: 4, hotdogs: 11}
# ]
# It should return "name" and "score" properties sorted by score; if scores are equals, sort alphabetically by name.
#
# [
#   {name: "Big Bob", score: 134},
#   {name: "Habanero Hillary", score: 98}
# ]
who_ate_what =  [{"name": "Billy The Beast", "chickenwings": 17 , "hamburgers": 7, "hotdogs": 8},
                                       {"name": "Habanero Hillary", "chickenwings": 5 , "hamburgers": 17, "hotdogs": 11},
                                       {"name": "Joey Jaws", "chickenwings": 8, "hamburgers": 8, "hotdogs": 15},
                                       {"name": "Big Bob" , "chickenwings": 20, "hamburgers": 4, "hotdogs": 11}]

competition = []
for i in range(len(who_ate_what)):
    score = (who_ate_what[i].get("chickenwings", 0)*5) + (who_ate_what[i].get("hamburgers", 0)*3) + (who_ate_what[i].get("hotdogs", 0)*2)
    competition.append({"name": who_ate_what[i]['name'], "score": score})

newlist = sorted(competition, key=lambda d: (-d['score'], d['name']))
print(newlist)

