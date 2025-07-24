# Face Recognition Attendance System

This project is a **Face Recognition Attendance System** built using Python. It captures faces using a webcam, compares them against known images, and records attendance in a CSV file. It's designed to be simple, minimal, and effective for small-scale use cases such as classrooms or small organizations.

## 📁 Project Structure

Face-Recognition-Attendance-System-master/
├── data/
│   └── attendance.csv          # Stores attendance logs  
├── known_faces/
│   └── addPicHere/             # Place images of known faces here  
└── src/
    └── main.py                 # Main script to run the application

## 🚀 Features

- Real-time face recognition through webcam  
- Attendance logging with date and time  
- Easy management of known face images  
- CSV-based attendance records  
- No external database required  

## 🛠 Requirements

- Python 3.x  
- OpenCV (`opencv-python`)  
- face_recognition  
- numpy  

Install dependencies using:

pip install opencv-python face_recognition numpy

## 🧑‍🏫 How to Use

1. **Add Face Images**  
   - Go to: `known_faces/addPicHere/`  
   - Add one image per person  
   - Name the file with the person's name (e.g., `Talal.jpg`, `Imad.png`)  

2. **Run the Application**  
   Navigate to the `src` directory and run the script:  

   python main.py

3. **Marking Attendance**  
   - Webcam will detect faces.  
   - If a face matches, the system logs name, date, and time to `data/attendance.csv`.

4. **View Attendance**  
   - Open `data/attendance.csv` to see the records.

## ✅ Tips for Best Accuracy

- Use clear, front-facing images  
- Good lighting improves recognition  
- Only one image per person is recommended  

## 📌 Limitations

- Must restart program after adding new images  
- Built for small-scale usage  
