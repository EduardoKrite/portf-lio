import pandas as pd
import matplotlib.pyplot as plt

tabela = pd.read_csv('premier.csv')

tabela = tabela.dropna(how='all')

print(tabela.head())
#total de partida
partida_casa = tabela.groupby('HomeTeam').size()

partida_fora = tabela.groupby('AwayTeam').size()

partida_total=partida_casa.add(partida_fora, fill_value=0)

partida=partida_total.idxmax()
quantidade = partida_total.max()
print(f"\n Total de partida: {partida} ({quantidade:.0f})")

#Qual time marcou mais gols na temporada 2018–2019
gols_casa = tabela.groupby('HomeTeam')['FTHG'].sum()

gols_fora = tabela.groupby('AwayTeam')['FTAG'].sum()


total_gols = gols_casa.add(gols_fora, fill_value=0)


time_mais_gols = total_gols.idxmax()
quantidade = total_gols.max()


print(f"\n Time com mais gols: {time_mais_gols} ({quantidade:.0f}) gols")

#Qual time sofreu mais gols
sofrido_casa = tabela.groupby('HomeTeam')['FTAG'].sum()

sofrido_fora = tabela.groupby('AwayTeam')['FTHG'].sum()


total_gols_sofrido = sofrido_casa.add(sofrido_fora, fill_value=0)


time_gols_sofrido = total_gols_sofrido.idxmax()
quantidade = total_gols_sofrido.max()


print(f"\n Time com mais gols sofrido: {time_gols_sofrido} ({quantidade:.0f}) gols")

#Qual time teve mais vitórias
casa = tabela[tabela['FTR']=='H'].groupby('HomeTeam').size()

vistante = tabela[tabela['FTR']=='A'].groupby('AwayTeam').size()

vitoria_total=casa.add(vistante, fill_value=0)

vitoria=vitoria_total.idxmax()
quantidade = vitoria_total.max()
print(f"\n Time com mais vitorias: {vitoria} ({quantidade:.0f}) Vitoria")

#Qual time teve mais derrotas
derrota_vistante= tabela[tabela['FTR']=='A'].groupby('HomeTeam').size()

derrota_casa = tabela[tabela['FTR']=='H'].groupby('AwayTeam').size()

derrota_total = derrota_vistante.add(derrota_casa, fill_value=0)

derrota = derrota_total.idxmax()
quantidade = derrota_total.max()

print(f"\n Time com mais derrota: {derrota} ({quantidade:.0f}) Derrotas")

#Quantos gols foram marcados durante toda a temporada

tabela['gols_da_temporada'] = tabela['FTAG']+ tabela['FTHG']
total_da_temporada= tabela['gols_da_temporada'].sum()

print(f'\n total de gols da temporada: {total_da_temporada}')

#Os times venceram mais partidas jogando em casa ou fora?
vitoria_casa = tabela[tabela['FTR']=='H'].shape[0]
vitoria_visitante = tabela[tabela['FTR']=='A'].shape[0]

if vitoria_casa > vitoria_visitante:
    print(f'\ncasa venceu: {vitoria_casa} gols')
    print(f'Fora venceu: {vitoria_visitante} gols')

elif vitoria_casa < vitoria_visitante:
     print(f'Fora venceu: {vitoria_visitante}') 
     print(f'casa venceu: {vitoria_casa} ')

else:
    print('empate')

#qual time teve mais vitórias jogando em casa
vitoria_casa = tabela[tabela['FTR']=='H'].groupby('HomeTeam').size()

nome_time = vitoria_casa.idxmax()
quantidade = vitoria_casa.max()
print(f"\n Time com mais vitorias em casa : {nome_time} ({quantidade:.0f}) Vitoria")

#Qual time teve mais vitórias jogando fora de casa
vitoria_fora =  tabela[tabela['FTR']=='A'].groupby('AwayTeam').size()

nome_time = vitoria_fora.idxmax()
quantidade = vitoria_fora.max()
print(f"\n Time com mais vitorias fora de  casa : {nome_time} ({quantidade:.0f}) Vitoria")

#Qual time teve mais chutes durante a temporada
chute_casa = tabela.groupby('HomeTeam')['HS'].sum()
chute_fora = tabela.groupby('AwayTeam')['AS'].sum()

total_de_chute = chute_casa.add(chute_fora, fill_value=0)

chute = total_de_chute.idxmax()
quantidade = total_de_chute.max()

print(f"\n Time com mais chute  : {chute} ({quantidade:.0f}) Chutes")

#Qual time teve mais chutes no alvo durante a temporada

chute_no_alvo_casa = tabela.groupby('HomeTeam')['HST'].sum()
chute_no_alvo_fora= tabela.groupby('AwayTeam')['AST'].sum()

total_de_chute_no_alvo = chute_no_alvo_casa.add(chute_no_alvo_fora, fill_value=0)

chute_no_alvo = total_de_chute_no_alvo.idxmax()
quantidade = total_de_chute_no_alvo.max()

print(f"\n Time com mais chute no alvo : {chute_no_alvo} ({quantidade:.0f}) Chutes")

#Qual time teve mais cartões amarelos durante a temporada
cartao_amarelo= tabela.groupby('HomeTeam')['HY'].sum()
cartao_amarelo_fora= tabela.groupby('AwayTeam')['AY'].sum()

total_de_cartao = cartao_amarelo.add(cartao_amarelo_fora, fill_value=0)

amarelo = total_de_cartao.idxmax()
quantidade = total_de_cartao.max()

print(f"\n Time com mais cartão amarelo : {amarelo} ({quantidade:.0f}) Cartão")

#Qual foi a partida com mais gols na temporada
tabela['partida'] = tabela['FTAG']+ tabela['FTHG']


indice = tabela['partida'].idxmax()
goleada = tabela.loc[indice]

print(f'\n A partida com mais gol na temporada: {goleada}')

#Qual foi a partida com a maior diferença de gols entre os times

tabela['diferencia'] = (tabela['FTAG'] - tabela['FTHG']).abs()


indice1 = tabela['diferencia'].idxmax()
dife = tabela.loc[indice1]

print(f'\n A partida com maior diferença: {dife}')

#Qual time teve a maior média de chutes por partida
media_casa = tabela.groupby('HomeTeam')['HS'].sum()
media_fora = tabela.groupby('AwayTeam')['AS'].sum()

total_da_media = media_casa.add(media_fora, fill_value=0)

total = total_da_media / partida_total

media = total.idxmax()
quantidade = total.max()


print(f"\n Time com a maior media chutes  : {media} ({quantidade:.0f}) media")

#Grafico de gols 

total_gols_ordenado= total_gols.sort_values(ascending=False)

plt.figure(figsize=(14, 6))
plt.bar(total_gols_ordenado.index, total_gols_ordenado.values, color='blue')
plt.xlabel('Time')
plt.ylabel('Gols marcados')
plt.title('Gols da temporada ')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#Gols sofridos por time
total_sofrido = total_gols_sofrido.sort_values(ascending=False)
plt.figure(figsize=(14, 6))
plt.pie(total_sofrido.values, labels=total_sofrido.index, autopct='%1.1f%%')
plt.xlabel('Time')
plt.ylabel('Gols sofridos')
plt.title('Gols sofridos por time')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

#Vitórias em casa × Vitórias fora
vitorias_comparativo = pd.DataFrame({
    'Vitórias em casa': vitoria_casa,
    'Vitórias fora': vitoria_fora
}).fillna(0)

vitorias_comparativo = vitorias_comparativo.sort_values('Vitórias em casa', ascending=False)

vitorias_comparativo.plot(kind='bar', figsize=(14, 6))
plt.xlabel('Time')
plt.ylabel('Número de vitórias')
plt.title('Vitórias em casa x Vitórias fora - Temporada 2018/19')
plt.xticks(rotation=90)
plt.legend(['Vitórias em casa', 'Vitórias fora'])
plt.tight_layout()
plt.show()

#Chutes × Gols
plt.scatter(total_de_chute, total_gols, c=total_gols, cmap='viridis')
plt.colorbar(label='Gols')

for time, x, y in zip(total_gols.index, total_de_chute, total_gols):
    plt.annotate(time, (x, y), fontsize=8)

plt.xlabel('Chutes')
plt.ylabel('Gols')
plt.title('Chutes x Gols por time')
plt.tight_layout()
plt.show()