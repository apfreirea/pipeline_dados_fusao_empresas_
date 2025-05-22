# Projeto pipeline de dados fusão de empresas
(Data Engineering)

## Objetivo 

Este projeto visa criar um pipeline para condensar dados de duas empresas após o processo de fusão (bigdata) para que sejam utilizados posteriormente pelo time de PI (inteligência de produto). 

## Atividades desenvolvidas (Extração, transformação e carregamento (ETL))
- Extração dos dados das empresas (.json e .csv)</br>
- Foram realizadas transformações na formatação dos dados, diferenças na descrição dos bancos de dados, tratamento dos dados faltantes, etc.</br>
- Refatoração do código usando POO para facilitar reutilização do código.</br>
- Load dos dados em csv para que o time de PI possa consultá-los através de queries SQL.</br>
- As decisões tomadas sobre o formato de dados final e tratamento de dados faltantes foi tomando em conjunto com a equipe de PI.</br>
 
## Estrutura do repositório

README.md: Este arquivo, que vocês estão lendo agora :) ;
data_raw: dados brutos extraídos das empresas;
data_processed: dados após o processados;
notebooks: Diretório com o notebook de exploração de dados;
scripts: scripts pipeline e processamento de dados;
LINCESE: arquivo com a licença do projeto;

### Ferramentas: 
- Linguagem pyhton
- Software VSCode
