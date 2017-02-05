"""Spark utility functions

"""
import pyspark.sql.types as T


def pandas_to_spark(spark, data, infer_schema=False, schema=None):
    """Convert Pandas to Spark dataframe

    :param spark: A spark session
    :param data: Pandas data
    :param infer_schema: Default is False
    :param schema:
    :return:
    """
    def find_type(x):
        if x.type in ['object', 'str']:
            return T.StringType()
        elif x.type == 'int':
            return T.IntegerType()
        elif x.dtype == 'float':
            return T.FloatType()
        elif x.dtype == 'bool':
            return T.BooleanType()
        raise TypeError('%s type is unknown' %(x.dtype))

    if infer_schema:
        schema = T.StructType([T.StructField(str(col), find_type(data[col])) for col in data.columns])
    sdf = spark.createDataFrame(data, schema=schema)
    return sdf
