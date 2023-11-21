# Monografia

Trabalho de conclusão de curso realizado no decorrer do ano de 2023, orientado pela professora:
* Profª. MSc. Ana Claudia Rossi

A monografia "Roteiro para Migração de Dados de CRM na área financeira: Integrando a Arquitetura Data Mesh com a Estratégia de Classificação Medalhão" consiste em trabalhar com dados utilizando arquitetura Data Mesh, classificação medalhão e arquitetura de referência NBDRA (NIST Big Data Reference Architecture)
<!-- O projeto consiste em responder 3 questões de negócios por meio de análise de um BI construído através de ETL. Para tal, deve-se ingerir dados do repostório público [Speedtest by Ookla Global Fixed and Mobile Network Performance Map Tiles](https://github.com/teamookla/ookla-open-data#speedtest-by-ookla-global-fixed-and-mobile-network-performance-map-tiles), tratá-los, automatizá-los e disponibilizá-los em camada de BI para análise.
Foi utilizada a arquitetura medalhão para o projeto, sendo os dados divididos em camada raw (camada dos dados iniciais), trusted (camada tratada) e delivery (camada com modelagem aplicada). -->

## 🚀 Etapas do projeto
<!-- 
Foi definido os seguintes passos:
1. Ingestão de Dados
2. Processamento de Dados
3. Armazenamento de Dados
4. Orquestração de ferramentas
5. Qualidade dos dados
6. Visualização -->

## 📋 Arquitetura do projeto

<!-- O arquivo para arquitetura do projeto está localizado em `arquitetura\Arquitetura Projeto Integrador.drawio`.
![Arquitetura_Fluxo](/arquitetura/Arquitetura.png) -->

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

* [AWS](https://us-east-1.console.aws.amazon.com/) - Plataforma utilizada para construção do pipeline dos dados
* [Draw.io](https://app.diagrams.net/) - Programa para desenvolvimento do modelo estrela;
* [Power BI](https://powerbi.microsoft.com/pt-br/) - Programa para desenvolvimento de relatórios; 

## ✒️ Autor

* [Vitor Marques](https://github.com/vitormrqs)