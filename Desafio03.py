''' Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

SP – R$67.836,43
RJ – R$36.678,66
MG – R$29.229,88
ES – R$27.165,48
Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação
que cada estado teve dentro do valor total mensal da distribuidora.'''

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
soma = sp + rj + mg + es + outros
print(soma)
percentsp = (sp/soma)*100
percentrj = (rj/soma)*100
percentmg = (mg/soma)*100
percentes = (es/soma)*100
percentoutros = (outros/soma)*100
print("Percentual de representação que cada estado teve dentro do valor total mensal da distribuidora:")
print(f"SP: {percentsp:.2f}%, RJ: {percentrj:.2f}%, MG:{percentmg:.2f}%, ES:{percentmg:.2f}%, Outros:{percentoutros:.2f}%")
