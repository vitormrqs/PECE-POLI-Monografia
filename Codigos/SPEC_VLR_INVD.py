import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue import DynamicFrame


def sparkSqlQuery(glueContext, query, mapping, transformation_ctx) -> DynamicFrame:
    for alias, frame in mapping.items():
        frame.toDF().createOrReplaceTempView(alias)
    result = spark.sql(query)
    return DynamicFrame.fromDF(result, glueContext, transformation_ctx)


args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node vsao_invd_clie
vsao_invd_clie_node1701311845740 = glueContext.create_dynamic_frame.from_catalog(
    database="silver-layer",
    table_name="vsao_invd_clie",
    transformation_ctx="vsao_invd_clie_node1701311845740",
)

# Script generated for node cada_cont_core_clie
cada_cont_core_clie_node1701311882387 = glueContext.create_dynamic_frame.from_catalog(
    database="silver-layer",
    table_name="cada_cont_core_clie",
    transformation_ctx="cada_cont_core_clie_node1701311882387",
)

# Script generated for node SQL Query
SqlQuery0 = """
SELECT 
    T3.cod_chav_coro_clie,
    SUM(T3.vlr_invd_rend_fixa) AS sum_vlr_invd_rend_fixa,
    SUM(T3.vlr_invd_rend_vari) AS sum_vlr_invd_rend_vari,
    CURRENT_DATE AS dat_rfrc
FROM (SELECT T1.cod_chav_coro_clie,
    CASE 
        WHEN UPPER(T1.NOM_INVD) LIKE '%RENDA FIXA%' 
             OR UPPER(T1.NOM_INVD) LIKE '%CDB%' 
             OR UPPER(T1.NOM_INVD) LIKE '%TESOURO DIRETO%' 
             OR UPPER(T1.NOM_INVD) LIKE '%IPCA%' 
             OR UPPER(T1.NOM_INVD) LIKE '%LCI%' 
             OR UPPER(T1.NOM_INVD) LIKE '%LCA%' 
            THEN vlr_invd
        ELSE 0
    END AS vlr_invd_rend_fixa,
    CASE 
        WHEN UPPER(T1.NOM_INVD) LIKE '%AÇÕES%' 
             OR UPPER(T1.NOM_INVD) LIKE '%FUNDO IMOBILIÁRIO%' 
             OR UPPER(T1.NOM_INVD) LIKE '%DEBÊNTURES%' THEN vlr_invd
        ELSE 0
    END AS vlr_invd_rend_vari
    FROM VSAO_INVD_CLIE AS T1
    LEFT JOIN CADA_CONT_CORE_CLIE AS T2 
    ON T1.cod_chav_coro_clie = T2.cod_chav_coro_clie
    WHERE T2.DES_CATE_CONT in ('PREMIUM', 'INTERMEDIARIA')
          AND T2.NOM_MOED_CONT = 'REAL') T3
GROUP BY T3.cod_chav_coro_clie
"""
SQLQuery_node1701311874284 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={
        "vsao_invd_clie": vsao_invd_clie_node1701311845740,
        "cada_cont_core_clie": cada_cont_core_clie_node1701311882387,
    },
    transformation_ctx="SQLQuery_node1701311874284",
)

# Script generated for node Amazon S3
AmazonS3_node1701313018521 = glueContext.getSink(
    path="s3://145844710627-gold-layer/SPEC_VLR_INVD/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["dat_rfrc"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1701313018521",
)
AmazonS3_node1701313018521.setCatalogInfo(
    catalogDatabase="gold-layer", catalogTableName="SPEC_VLR_INVD"
)
AmazonS3_node1701313018521.setFormat("glueparquet")
AmazonS3_node1701313018521.writeFrame(SQLQuery_node1701311874284)
job.commit()
