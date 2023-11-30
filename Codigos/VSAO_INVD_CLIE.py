import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsgluedq.transforms import EvaluateDataQuality
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

# Script generated for node Amazon S3
AmazonS3_node1700883440212 = glueContext.create_dynamic_frame.from_catalog(
    database="bronze-layer",
    table_name="vsao_invd_clie",
    transformation_ctx="AmazonS3_node1700883440212",
)

# Script generated for node Latest partition, Drop duplicated value, Cast Date
SqlQuery0 = """
select distinct
t0.cod_chav_coro_clie as cod_chav_coro_clie,
t0.num_agen as num_agen,
t0.num_cont as num_cont,
t0.nom_invd as nom_invd,
cast(concat(substr(t0.dat_cmpr,1,4),"-",substr(t0.dat_cmpr,5,2),"-",substr(t0.dat_cmpr,7,2)) as date) as dat_cmpr,
cast(concat(substr(t0.dat_venc,1,4),"-",substr(t0.dat_venc,5,2),"-",substr(t0.dat_venc,7,2)) as date) as dat_venc,
t0.vlr_invd as vlr_invd,
t0.qtd_unid as qtd_unid,
t0.vlr_unid as vlr_unid,
t0.vlr_atua as vlr_atua,
t0.pct_rend/100 as pct_rend,
t0.cat_rend as cat_rend,
t0.nom_corr as nom_corr,
t0.vlr_taxa as vlr_taxa,
t0.nom_esta_invd as nom_esta_invd,
cast(concat(substr(t0.dat_rfrc,1,4),"-",substr(t0.dat_rfrc,5,2),"-",substr(t0.dat_rfrc,7,2)) as date) as dat_rfrc
from myDataSource t0
inner join (select max(dat_rfrc) as dat_rfrc from myDataSource) t1
on t0.dat_rfrc = t1.dat_rfrc
"""
LatestpartitionDropduplicatedvalueCastDate_node1700883665643 = sparkSqlQuery(
    glueContext,
    query=SqlQuery0,
    mapping={"myDataSource": AmazonS3_node1700883440212},
    transformation_ctx="LatestpartitionDropduplicatedvalueCastDate_node1700883665643",
)

# Script generated for node Evaluate Data Quality
EvaluateDataQuality_node1701054555388_ruleset = """
    # Example rules: Completeness "colA" between 0.4 and 0.8, ColumnCount > 10
    Rules = [
        ColumnExists "cod_chav_coro_clie",
        ColumnExists "num_agen",
        ColumnExists "num_cont",
        ColumnExists "nom_invd",
        Completeness "cod_chav_coro_clie" = 1
    ]
"""

EvaluateDataQuality_node1701054555388 = EvaluateDataQuality().process_rows(
    frame=AmazonS3_node1700883440212,
    ruleset=EvaluateDataQuality_node1701054555388_ruleset,
    publishing_options={
        "dataQualityEvaluationContext": "EvaluateDataQuality_node1701054555388",
        "enableDataQualityResultsPublishing": True,
        "resultsS3Prefix": "s3://145844710627-silver-layer/ETL-RUNS/",
    },
    additional_options={
        "observations.scope": "ALL",
        "performanceTuning.caching": "CACHE_NOTHING",
    },
)

assert (
    EvaluateDataQuality_node1701054555388[
        EvaluateDataQuality.DATA_QUALITY_RULE_OUTCOMES_KEY
    ]
    .filter(lambda x: x["Outcome"] == "Failed")
    .count()
    == 0
), "The job failed due to failing DQ rules for node: AmazonS3_node1700883440212"

# Script generated for node ruleOutcomes
ruleOutcomes_node1701054598102 = SelectFromCollection.apply(
    dfc=EvaluateDataQuality_node1701054555388,
    key="ruleOutcomes",
    transformation_ctx="ruleOutcomes_node1701054598102",
)

# Script generated for node Amazon S3
AmazonS3_node1700885268419 = glueContext.getSink(
    path="s3://145844710627-silver-layer/VSAO_INVD_CLIE/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["dat_rfrc"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1700885268419",
)
AmazonS3_node1700885268419.setCatalogInfo(
    catalogDatabase="silver-layer", catalogTableName="VSAO_INVD_CLIE"
)
AmazonS3_node1700885268419.setFormat("glueparquet")
AmazonS3_node1700885268419.writeFrame(
    LatestpartitionDropduplicatedvalueCastDate_node1700883665643
)
job.commit()
