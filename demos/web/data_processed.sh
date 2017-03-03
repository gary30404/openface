#!/bin/bash
python extractFrame.py
echo 'Extract Frames Done'
cd ../../
echo 'Preprocess Raw Images'
./util/align-dlib.py demos/web/data/training_data align outerEyesAndNose demos/web/data/aligned-data --size 96
echo 'Generate Representations'
./batch-represent/main.lua -outDir demos/web/data/feature_directory -data demos/web/data/aligned_data
echo 'Create the Classification Model'
./demos/classifier.py train demos/web/data/feature_directory
