import face_recognition
import cv2
import numpy as np
import os
import pandas as pd
from datetime import datetime

KnownFacesPath = 'known_faces'  
Picture = []
List = os.listdir(KnownFacesPath)
NamesOfClass = []

for FileName in List:
    CurrentImage = cv2.imread(f'{KnownFacesPath}/{FileName}')
    if CurrentImage is not None:
        Picture.append(CurrentImage)
        NamesOfClass.append(os.path.splitext(FileName)[0])  

def encodings_search(Picture):
    list_encoding = []
    for pic in Picture:
        pic = cv2.cvtColor(pic, cv2.COLOR_BGR2RGB)
        encodings = face_recognition.face_encodings(pic)
        if encodings:
            list_encoding.append(encodings[0])
    return list_encoding

encodeKnownFacesList = encodings_search(Picture)

attendancePath = 'data\\attendance.csv'

def markingAttendance(name):
    CurrentTime = datetime.now()
    ReadableString = CurrentTime.strftime('%Y-%m-%d %H:%M:%S')
    if os.path.exists(attendancePath):
        FrameData = pd.read_csv(attendancePath)
    else:
        FrameData = pd.DataFrame(columns=['Name', 'Time'])

    TodaysTime = CurrentTime.strftime('%Y-%m-%d')
    if not ((FrameData['Name'] == name) & (FrameData['Time'].str.contains(TodaysTime))).any():
        FrameData = pd.concat([FrameData, pd.DataFrame({'Name': [name], 'Time': [ReadableString]})], ignore_index=True)
        FrameData.to_csv(attendancePath, index=False)

Capture = cv2.VideoCapture(0)

while True:
    passed, Pic = Capture.read()
    if not passed:
        break

    PicS = cv2.resize(Pic, (0, 0), fx=0.25, fy=0.25)  
    PicS = cv2.cvtColor(PicS, cv2.COLOR_BGR2RGB)

    FacesLocation = face_recognition.face_locations(PicS)
    encodesFaceLocation = face_recognition.face_encodings(PicS, FacesLocation)

    for encodeFace, faceLoc in zip(encodesFaceLocation, FacesLocation):
        ComparingResult = face_recognition.compare_faces(encodeKnownFacesList, encodeFace)
        differentiation = face_recognition.face_distance(encodeKnownFacesList, encodeFace)

        ComparingResultIndex = np.argmin(differentiation)

        if ComparingResult[ComparingResultIndex]:
            Name = NamesOfClass[ComparingResultIndex].upper()
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4  
            cv2.rectangle(Pic, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(Pic, Name, (x1 + 6, y2 + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            markingAttendance(Name)

    cv2.imshow('Smart Attendance System - Please Press q to Quit', Pic)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

Capture.release()
cv2.destroyAllWindows()

