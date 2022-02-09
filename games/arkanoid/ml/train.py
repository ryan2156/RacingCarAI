import os
import pickle
from platform import platform
from posixpath import split
from turtle import position
import numpy as np
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split


path = "../log"
allFile = os.listdir(path)
data_set = []
for file in allFile:
    with open(os.path.join(path, file), "rb") as f:
        data_set.append(pickle.load(f))

ball_x = []
ball_y = []
Speed_x = []
Speed_y = []
Direction = []

for data in data_set:
    for i, sceneInfo in enumerate(data['1P']["scene_info"][2:-3]):
        ball_x.append(data['1P']['scene_info'][i+1]["ball"][0])
        ball_y.append(data['1P']['scene_info'][i+1]["ball"][1])
        Speed_x.append(data['1P']['scene_info'][i+1]["ball"][0] - data['1P']['scene_info'][i+1]["ball"][0])
        Speed_x.append(data['1P']['scene_info'][i+1]["ball"][1] - data['1P']['scene_info'][i+1]["ball"][1])
        if Speed_x[-1] > 0:
            if Speed_y[-1] > 0: Direction.append(0)
            else: Direction.append(1)
        else:
            if Speed_y[-1] > 0: Direction.append(2)
            else: Direction.append(3)

X = np.array([0,0,0,0,0])
for i in range(len(ball_x)):
    X = np.vstack((X, [ball_x[i], ball_y[i], Speed_x[i], Speed_y[i]]))
X = X[1::]

Position_pred = []
platform_position_y = 400
ball_speed_y = 7
platform_width = 200
for i in range(len(ball_x)):
    pred = ball_x[i] + ((platform_position_y-ball_y[i])//ball_speed_y) * Speed_x

    section = (pred // platform_width)
    if(section % 2 == 0):
        pred = abs(pred - platform_width*section)
    else:
        pred = platform_width - abs(pred - platform_width)
    
    Position_pred.append(pred)

Position_pred = np.array(Position_pred)
Y = Position_pred

x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.2)

model = DecisionTreeRegressor(criterion='mse', max_dpth=2, splitter="best")