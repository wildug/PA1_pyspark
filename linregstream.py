from pyspark.mllib.linalg import Vectors
from pyspark.mllib.regression import LabeledPoint
from pyspark.mllib.regression import StreamingLinearRegressionWithSGD
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
import time

sc = SparkContext(appName="Linearer Regress")
ssc = StreamingContext(sc, 1)

def parse(lp):
    label = float(lp[lp.find('(') + 1: lp.find(',')])
    vec = Vectors.dense(lp[lp.find('[') + 1: lp.find(']')].split(','))
    return LabeledPoint(label, vec)

trainingData = ssc.textFileStream("training/").map(parse).cache()
testData = ssc.textFileStream("testing/").map(parse)
numFeatures = 1
model = StreamingLinearRegressionWithSGD()
model.setInitialWeights([1.0])

model.trainOn(trainingData)

print(model.predictOnValues(testData.map(lambda lp: (lp.label, lp.features))))

ssc.start()

ssc.awaitTermination(60)


ssc.stop()
