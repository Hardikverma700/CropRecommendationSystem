
import pandas as pd  # Importing pandas library
from sklearn import  preprocessing  # Importing sklearn library. This is a very powerfull library for machine learning. Scikit-learn is probably the most useful library for machine learning in Python. The sklearn library contains a lot of efficient tools for machine learning and statistical modeling including classification, regression, clustering and dimensionality reduction.
from sklearn.neighbors import KNeighborsClassifier  # Importing Knn Classifier from sklearn library.
import numpy as np  # Importing numpy to do stuffs related to arrays
import PySimpleGUI as sg  # Importing pysimplegui to make a Graphical User Interface.

excel = pd.read_excel('D:\minor_project\crop (1).xlsx', header=0)  # Importing our excel data from a specific file.
print(excel)  # Printing our excel file data.
print(excel.shape)  # Checking out the shape of our data.





le = preprocessing.LabelEncoder()  # Various machine learning algorithms require numerical input data, so you need to represent categorical columns in a numerical column. In order to encode this data, you could map each value to a number. This process is known as label encoding, and sklearn conveniently will do this for you using Label Encoder.
crop = le.fit_transform(list(excel["CROP"]))  # Mapping the values in weather into numerical form.

NITROGEN = list(excel["NITROGEN"])  # Making the whole row consisting of nitrogen values to come into nitrogen.
PHOSPHORUS = list(excel["PHOSPHORUS"])  # Making the whole row consisting of phosphorus values to come into phosphorus.
POTASSIUM = list(excel["POTASSIUM"])  # Making the whole row consisting of potassium values to come into potassium.
TEMPERATURE = list(
    excel["TEMPERATURE"])  # Making the whole row consisting of temperature values to come into temperature.
HUMIDITY = list(excel["HUMIDITY"])  # Making the whole row consisting of humidity values to come into humidity.
PH = list(excel["PH"])  # Making the whole row consisting of ph values to come into ph.
RAINFALL = list(excel["RAINFALL"])  # Making the whole row consisting of rainfall values to come into rainfall.

features = list(
    zip(NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH, RAINFALL))  # Zipping all the features together
features = np.array([NITROGEN, PHOSPHORUS, POTASSIUM, TEMPERATURE, HUMIDITY, PH,
                     RAINFALL],dtype=float)  # Converting all the features into a array form

features = features.transpose()  # Making transpose of the features
print(features.shape)  # Printing the shape of the features after getting transposed.
print(
    crop.shape)  # Printing the shape of crop. Please note that the shape of the features and crop should match each other to make predictions.

model = KNeighborsClassifier(
    n_neighbors=3)  # The number of neighbors is the core deciding factor. K is generally an odd number if the number of classes is 2. When K=1, then the algorithm is known as the nearest neighbor algorithm.
model.fit(features,
          crop)  # fit your model on the train set using fit() and perform prediction on the test set using predict().
layout = [[sg.Text('                      Crop Recommendation Assistant', font=("Helvetica", 30), text_color='yellow')],
          # Defining the layout of the Graphical User Interface. It consist of some text, Buttons, and blanks to take Input.
          [sg.Text('Please enter the following details :-', font=("Helvetica", 20))],
          # We have defined the text size, font type, font size, blank size, colour of the text in the GUI.
          [sg.Text('Enter ratio of Nitrogen in the soil                                  :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('Enter ratio of Phosphorous in the soil                           :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('Enter ratio of Potassium in the soil                               :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('Enter average Temperature value around the field        :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('*C', font=("Helvetica", 20))],
          [sg.Text('Enter average percentage of Humidity around the field :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('%', font=("Helvetica", 20))],
          [sg.Text('Enter PH value of the soil                                            :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1))],
          [sg.Text('Enter average amount of Rainfall around the field        :', font=("Helvetica", 20)),
           sg.Input(font=("Helvetica", 20), size=(20, 1)), sg.Text('mm', font=("Helvetica", 20))],
          [sg.Text(size=(50, 1), font=("Helvetica", 20), text_color='yellow', key='-OUTPUT1-')],
          [sg.Button('Submit', font=("Helvetica", 20)), sg.Button('Quit', font=("Helvetica", 20))]]
window = sg.Window('Crop Recommendation Assistant', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Quit':  # If the user will press the quit button then the program will end up.
        break
    print(values[0])
    nitrogen_content = values[0]  # Taking input from the user about nitrogen content in the soil.
    phosphorus_content = values[1]  # Taking input from the user about phosphorus content in the soil.
    potassium_content = values[2]  # Taking input from the user about potassium content in the soil.
    temperature_content = values[3]  # Taking input from the user about the surrounding temperature.
    humidity_content = values[4]  # Taking input from the user about the surrounding humidity.
    ph_content = values[5]  # Taking input from the user about the ph level of the soil.
    rainfall = values[6]  # Taking input from the user about the rainfall.
    predict1 = np.array(
        [nitrogen_content, phosphorus_content, potassium_content, temperature_content, humidity_content, ph_content,
         rainfall],dtype=float)  # Converting all the data that we collected from the user into a array form to make further predictions.
    print(predict1)  # Printing the data after being converted into a array form.
    predict1 = predict1.reshape(1,
                                -1)  # Reshaping the input data so that it can be applied in the model for getting accurate results.
    print(predict1)  # Printing the input data value after being reshaped.
    predict1 = model.predict(predict1)  # Applying the user input data into the model.
    print(predict1)  # Finally printing out the results.
    crop_name = str()
    if predict1 == 0:  # Above we have converted the crop names into numerical form, so that we can apply the machine learning model easily. Now we have to again change the numerical values into names of crop so that we can print it when required.
        crop_name = 'Apple(सेब)'
    elif predict1 == 1:
        crop_name = 'Banana(केला)'
    elif predict1 == 2:
        crop_name = 'Blackgram(काला चना)'
    elif predict1 == 3:
        crop_name = 'Chickpea(काबुली चना)'
    elif predict1 == 4:
        crop_name = 'Coconut(नारियल)'
    elif predict1 == 5:
        crop_name = 'Coffee(कॉफ़ी)'
    elif predict1 == 6:
        crop_name = 'Cotton(कपास)'
    elif predict1 == 7:
        crop_name = 'Grapes(अंगूर)'
    elif predict1 == 8:
        crop_name = 'Jute(जूट)'
    elif predict1 == 9:
        crop_name = 'Kidneybeans(राज़में)'
    elif predict1 == 10:
        crop_name = 'Lentil(मसूर की दाल)'
    elif predict1 == 11:
        crop_name = 'Maize(मक्का)'
    elif predict1 == 12:
        crop_name = 'Mango(आम)'
    elif predict1 == 13:
        crop_name = 'Mothbeans(मोठबीन)'
    elif predict1 == 14:
        crop_name = 'Mungbeans(मूंग)'
    elif predict1 == 15:
        crop_name = 'Muskmelon(खरबूजा)'
    elif predict1 == 16:
        crop_name = 'Orange(संतरा)'
    elif predict1 == 17:
        crop_name = 'Papaya(पपीता)'
    elif predict1 == 18:
        crop_name = 'Pigeonpeas(कबूतर के मटर)'
    elif predict1 == 19:
        crop_name = 'Pomegranate(अनार)'
    elif predict1 == 20:
        crop_name = 'Rice(चावल)'
    elif predict1 == 21:
        crop_name = 'Watermelon(तरबूज)'

    if int(humidity_content) >= 1 and int(
            humidity_content) <= 33:  # Here I have divided the humidity values into three categories i.e low humid, medium humid, high humid.
        humidity_level = 'low humid'
    elif int(humidity_content) >= 34 and int(humidity_content) <= 66:
        humidity_level = 'medium humid'
    else:
        humidity_level = 'high humid'

    if int(temperature_content) >= 0 and int(
            temperature_content) <= 6:  # Here I have divided the temperature values into three categories i.e cool, warm, hot.
        temperature_level = 'cool'
    elif int(temperature_content) >= 7 and int(temperature_content) <= 25:
        temperature_level = 'warm'
    else:
        temperature_level = 'hot'

    if int(rainfall) >= 1 and int(
            rainfall) <= 100:  # Here I have divided the humidity values into three categories i.e less, moderate, heavy rain.
        rainfall_level = 'less'
    elif int(rainfall) >= 101 and int(rainfall) <= 200:
        rainfall_level = 'moderate'
    elif int(rainfall) >= 201:
        rainfall_level = 'heavy rain'

    if int(nitrogen_content) >= 1 and int(
            nitrogen_content) <= 50:  # Here I have divided the nitrogen values into three categories.
        nitrogen_level = 'less'
    elif int(nitrogen_content) >= 51 and int(nitrogen_content) <= 100:
        nitrogen_level = 'not to less but also not to high'
    elif int(nitrogen_content) >= 101:
        nitrogen_level = 'high'

    if int(phosphorus_content) >= 1 and int(
            phosphorus_content) <= 50:  # Here I have divided the phosphorus values into three categories.
        phosphorus_level = 'less'
    elif int(phosphorus_content) >= 51 and int(phosphorus_content) <= 100:
        phosphorus_level = 'not to less but also not to high'
    elif int(phosphorus_content) >= 101:
        phosphorus_level = 'high'

    if int(potassium_content) >= 1 and int(
            potassium_content) <= 50:  # Here I have divided the potassium values into three categories.
        potassium_level = 'less'
    elif int(potassium_content) >= 51 and int(potassium_content) <= 100:
        potassium_level = 'not to less but also not to high'
    elif int(potassium_content) >= 101:
        potassium_level = 'high'

    if float(ph_content) >= 0 and float(ph_content) <= 5:  # Here I have divided the ph values into three categories.
        phlevel = 'acidic'
    elif float(ph_content) >= 6 and float(ph_content) <= 8:
        phlevel = 'neutral'
    elif float(ph_content) >= 9 and float(ph_content) <= 14:
        phlevel = 'alkaline'

    print("Recommended Crop: " + crop_name)
    print(humidity_level)
    print( "Temperature: " + temperature_level)
    print("RainFall: " + rainfall_level)
    print("Nitrogen Level: " + nitrogen_level)
    print("Phosphorus Level: " + phosphorus_level)
    print("Potassium Level: " +  potassium_level)
    print("PH Level: " + phlevel)


    window['-OUTPUT1-'].update(
        'The best crop that you can grow : ' + crop_name)  # Suggesting the best crop after prediction.


window.close()
