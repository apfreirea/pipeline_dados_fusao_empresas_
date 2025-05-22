# Importando métodos da classe criada 'Dados'
from processamento_dados import Dados

# Caminho dos dados

path_csv = 'data_raw/dados_empresaB.csv'
path_json = 'data_raw/dados_empresaA.json'

# Extração de dados

dados_empresaA = Dados(path_json,'json')
print(f'\nNome das coluna da EmpresaA:{dados_empresaA.nome_colunas}')
print(f'Quantidade de dados da EmpresaA: {dados_empresaA.qtd_linhas}\n')

dados_empresaB = Dados(path_csv,'csv')
print(f'Nome das coluna da EmpresaB: {dados_empresaB.nome_colunas}')
print(f'Quantidade de dados da EmpresaB: {dados_empresaB.qtd_linhas}\n')

# Transformação dos dados 

key_mapping = {'Nome do Item':'Nome do Produto',
               'Classificação do Produto':'Categoria do Produto',
               'Valor em Reais (R$)':'Preço do Produto (R$)',
               'Quantidade em Estoque':'Quantidade em Estoque',
               'Nome da Loja':'Filial',
               'Data da Venda':'Data da Venda'}


dados_empresaB.rename_columns(key_mapping)
print(f"Novos nomes de colunas da empresaB: {dados_empresaB.nome_colunas}\n")

# Juntando os dados da Empresa A e B

dados_fusao = Dados.join(dados_empresaA,dados_empresaB)
print(f"As colunas de dados da fusão são: {dados_fusao.nome_colunas}")
print(f'Quantidade de dados da fusão: {dados_fusao.qtd_linhas}\n')

# Load de dados

path_dados_combinados = 'data_processed/dados_combinados.csv'
dados_fusao.salvando_dados(path_dados_combinados)
print(f'Dados combinados salvo em: {path_dados_combinados}')