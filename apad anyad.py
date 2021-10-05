import random
when = ['Par evvel ezelott', 'Tegnap', 'Elozo nap', 'Long idejexd','Januar 20ikan']
who = ['a nyuszi', 'a elefant', 'a eger', 'a kutya','a cica']
name = ['Ali', 'Miriam','daniel', 'Hoouk', 'Starwalker']
residence = ['Barcelona','India', 'Germany', 'Venice', 'England']
went = ['mozi', 'kollegium','etterem', 'suli', 'mosoda']
happened = ['sok baratot szereztem','Burgert ettem', 'titkos kulcsot szereztem', 'titkot talaltam ki', 'konyvet irtam']
print(random.choice(when) + ', ' + random.choice(who) + ' aki a lakott ' + random.choice(residence) + ', elment a' + random.choice(went) + ' es ' + random.choice(happened))