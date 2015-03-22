osoby = [{'nazwisko':'Nowak', 'waga':70, 'ulubione_dania':['schabowy', 'pomidorowa'] },         
         {'nazwisko':'Kowalski', 'waga':30, 'ulubione_dania':['lody', 'ciastka'] },  
         {'nazwisko':'Kos', 'waga':40, 'ulubione_dania':['ryz', 'ogorkowa'] },
         {'nazwisko':'Szpak', 'waga':70, 'ulubione_dania':['schabowy', 'pomidorowa'] },
         {'nazwisko':'Osa', 'waga':80, 'ulubione_dania':['frytki', 'ryba'] },
         ]

print osoby
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o:o['nazwisko'])
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o:o['waga'])
print [o['nazwisko'] for o in osoby]

osoby.sort(key=lambda o:o['ulubione_dania'][0],reverse=True)
print [o['nazwisko'] for o in osoby]

print sorted(osoby, key=lambda o:o['ulubione_dania'][0],reverse=True)

print sorted (osoby,
              cmp=lambda x,y: 1 if x<y else -1,
              key=lambda o:o['ulubione_dania'][0],reverse=True)