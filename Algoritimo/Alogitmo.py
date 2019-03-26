import json
from repustate import Client
with open('tickets.json', encoding='utf-8') as f:
    data = json.load(f)
client = Client(api_key='e25264f83d8d4ac8ca82afc701164ad5fd600fb7')
comp =0;
salva2=0;
salva=""
salva3=""
salva4=0
for element in data:
    texto = str(element)+"\n"
    aux=0
    for obj in element["Interactions"]:
        com = str(obj["Sender"])
        #print(com)
        if(com == "Customer"):
            texto +='{} \n'.format(str(obj["Message"]))
        if('procon' in str(obj["Message"]).lower() or 'reclame aqui' in  str(obj["Message"]).lower()):
            salva4=1
        if('reclamação' in str(obj["Subject"]).lower()):
            salva4=1
        aux+=1
    salva = client.sentiment(text=texto, lang="pt")
    salva2 = salva["score"]
    if(salva2<0 or salva4==1):
        data[comp]["Prioridade"] = "Alta"
        data[comp]["Pontuacao"] = salva2
    else:
        data[comp]["Prioridade"] = "Normal"
        data[comp]["Pontucao"] = salva2
    #print(comp)
    comp+=1
#print (data)
with open('ticket.json','w', encoding='utf-8') as f:
    json.dump(data,f)


