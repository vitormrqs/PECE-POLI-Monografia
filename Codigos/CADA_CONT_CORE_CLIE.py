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
    table_name="cada_cont_core_clie",
    transformation_ctx="AmazonS3_node1700883440212",
)

# Script generated for node Latest partition, Drop duplicated value, Cast Date
SqlQuery0 = """
select distinct
    T0.COD_CHAV_CORO_CLIE as COD_CHAV_CORO_CLIE,
    T0.NUM_AGEN as NUM_AGEN,
    T0.NUM_CONT as NUM_CONT,
    T0.DES_CATE_CONT as DES_CATE_CONT,
    T0.IND_REGU as IND_REGU,
    CAST(CONCAT(SUBSTR(T0.DAT_ABER_CONT,1,4),"-",SUBSTR(T0.DAT_ABER_CONT,5,2),"-",SUBSTR(T0.DAT_ABER_CONT,7,2)) AS DATE) as DAT_ABER_CONT,
    T0.VLR_SALD_DISP as VLR_SALD_DISP,
    T0.VLR_LIMI_CRED as VLR_LIMI_CRED,
    T0.IND_CONT as IND_CONT,
    T0.NOM_MOED_CONT as NOM_MOED_CONT,
    CAST(CONCAT(SUBSTR(T0.DAT_RFRC,1,4),"-",SUBSTR(T0.DAT_RFRC,5,2),"-",SUBSTR(T0.DAT_RFRC,7,2)) AS DATE) as dat_rfrc
from myDataSource T0
inner join (select max(DAT_RFRC) AS DAT_RFRC from myDataSource) T1
ON T0.DAT_RFRC = T1.DAT_RFRC
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
    path="s3://145844710627-silver-layer/CADA_CONT_CORE_CLIE/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=["dat_rfrc"],
    compression="snappy",
    enableUpdateCatalog=True,
    transformation_ctx="AmazonS3_node1700885268419",
)
AmazonS3_node1700885268419.setCatalogInfo(
    catalogDatabase="silver-layer", catalogTableName="CADA_CONT_CORE_CLIE"
)
AmazonS3_node1700885268419.setFormat("glueparquet")
AmazonS3_node1700885268419.writeFrame(
    LatestpartitionDropduplicatedvalueCastDate_node1700883665643
)
job.commit()
