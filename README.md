# Monografia

Trabalho de conclusão de curso realizado no decorrer do ano de 2023, orientado pela professora:
* Profª. MSc. Ana Claudia Rossi

A monografia "Aplicação da arquitetura Data Mesh com a estratégia de classificação Medalhão em área financeira de gestão de relacionamento com o cliente" consiste em gerar uma visão agregada  para o time de negócios com a aplicação de arquiteturas e classificação de dados.

O objetivo deste trabalho é aplicar um método de especificação de uma arquitetura de software, hospedada em nuvem, utilizando arquitetura baseada em Data Mesh, arquitetura de referência NBDRA e a classificação Medalhão para um sistema financeiro na área de CRM.

## 🚀 Etapas do projeto
Foram definidos os seguintes passos:
1. Construção da introdução e problemática
2. Objetivo
3. Metodologia
4. Aplicação da arquitetura Data Mesh
5. Resultados
6. Considerações finais 

## 📋 Arquitetura do projeto

O de referência para a arquitetura do projeto está localizado em `Imagens\2-NIST.png`.
![Arquitetura_Fluxo_NIST](/Imagens/2-NIST.png)

## 🔧 Projeto

<!-- ### 1. Dados

Foram utilizados os dados mais recentes do repositório Okla, sendo eles: 2022 e 2023 (1º quadrimestre).
Os dados estão disponíveis por redes fixas e móveis, por ano e por extensão de arquivo (parquet / shapefile).

### 2. Fluxo de leitura

Através do repositório inicial, foi lido os arquivos em script construído para ingestão.
> O código que lê os arquivos iniciais e realiza os primeiros tratamentos está em: `ETL/gluejobs_trusted.py`.

Após inserido os dados na camada raw e feito os tratamentos iniciais como a revisão de dimensões de:
1. Completude
2. Validade
3. Integridade
4. Exclusividade

os dados são validados através do script `validacao\gluejobs_validacoes.py`.

Finalmente, são avaliados e filtrados para serem disponibilizados na camada delivery. Nessa etapa, é criada a tabela fato e suas dimenões como será explicada no capítulo a seguir. Os dados são construídos através do script `ETL\gluejobs_delivery.py`.

### 3. Modelagem Star Schema

A tabela fato contém cada evento realizado de teste e possui dimensões de: `dim_Localizacao`, `dim_Tipo`, `dim_Periodo`. Foi escolhido esse modelo a fim de disponibilizarmos informações visuais dos dados.

![Star Schema](/modelagem.jpeg)

| Tabela          | Atributos            | Descrição                                                            |
|-----------------|----------------------|----------------------------------------------------------------------|
| Fato            | FK_Id_Tipo           | Chave estrangeira para a tabela dim_Tipo (Id_Tipo)                   |
| Fato            | FK_Id_Localizacao    | Chave estrangeira para a tabela dim_Localizacao (Id_Geo)             |
| Fato            | FK_Id_Periodo        | Chave estrangeira para a tabela dim_Periodo (Id_Temp)                |
| Fato            | avg_d_kbps           | Velocidade média de download em kilobits por segundo                 |
| Fato            | avg_u_kbps           | Velocidade média de upload em kilobits por segundo                   |
| Fato            | avg_lat_ms           | Latência média em milissegundos                                      |
| Fato            | tests                | Número de testes realizados no bloco                                 |
| Fato            | devices              | Número de dispositivos exclusivos que contribuem com testes no bloco |
| dim_Tipo        | PK_Id_Tipo           | Chave primária da tabela dim_Tipo                                    |
| dim_Tipo        | tipo                 | Tipo de dispositivo (móvel ou fixo)                                  |
| dim_Localizacao | PK_Id_Geo            | Chave primária da tabela dim_Localizacao                             |
| dim_Localizacao | quadkey              | Quadrante que representa o espaço/bloco dos testes                   |
| dim_Localizacao | latitude             | Latitude da localização dos testes                                   |
| dim_Localizacao | longitude            | Longitude da localização dos testes                                  |
| dim_Periodo     | PK_Id_Temp           | Chave primária da tabela dim_Periodo                                 |
| dim_Periodo     | year                 | Ano da realização dos testes                                         |
| dim_Periodo     | quad                 | Quadrimestre da realização dos testes                                |

Os códigos utilizados para criação da tabela estão diponíveis em `ETL\gluejobs_delivery.py`.

### 4. *Dashboards*

Por meio do Power BI foi possível acessar as tabelas montadas pelo Crawler da AWS e criar o relatório que é utilizado na área de negócios.

![Dashboard](/relatorio/dashboard.jpeg)

O arquivo está localizado em `relatorio\ProjetoIntegrador.pbix`. -->

## 🛠️ Construído com

* [AWS](https://us-east-1.console.aws.amazon.com/) - Plataforma utilizada para construção do pipeline dos dados;
* [Draw.io](https://app.diagrams.net/) - Programa para desenvolvimento de esquemas de tabelas e modelagem dos dados;
* [Lucidchart](https://lucid.app/) - Interface para construção de diagramações;
<!-- * [Power BI](https://powerbi.microsoft.com/pt-br/) - Programa para desenvolvimento de relatórios;  -->

## ✒️ Autor

* [Vitor Marques](https://github.com/vitormrqs)