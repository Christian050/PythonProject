# from imageai.Classification import ImageClassification
# import os
# execution_path = os.getcwd()
# prediction = ImageClassification()
# prediction.setModelTypeAsResNet50()
# prediction.setModelPath(execution_path + "resnet50_imagenet_tf.2.20.h5")
# prediction.loadModel()
#
# predictions, percentage_probabilities = prediction.classifyImage("aero.jpg ", result_count=5)
# for index in range(len(predictions)):
#     print(predictions[index], ':', percentage_probabilities[index])

i = 1
while True:
    if i%3 == 0:
        break
        print(i)
i += 1