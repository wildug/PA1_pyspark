from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.regression import StreamingLinearRegressionWithSGD
from pyspark import SparkContext
from pyspark.streaming import StreamingContext

sc = SparkContext(appName="Normal Text Stream")
ssc = StreamingContext(sc, 1)

eingaben = ssc.textFileStream("training/")

eingaben.pprint()

ssc.start()
ssc.awaitTermination(30)
ssc.stop()