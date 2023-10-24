pessoas = list()
pessoas.append('ze')
pessoas.append('toijnho')
empresa = dict()
empresa['funcionarios'] = pessoas

print(empresa)

#empresa['funcionarios'].append('maria')
novalista = empresa['funcionarios']
novalista.append('maria')

novalista.append({empresa['funcionarios'][0]:12345})
print(empresa)
