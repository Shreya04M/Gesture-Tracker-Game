# Gesture Builder

## Overview

Gesture Builder is a computer-vision-based interactive application that allows users to create structures using hand gestures. Instead of traditional mouse and keyboard input, the system uses real-time hand tracking to let users select, move, and place geometric shapes on a digital canvas.

The project demonstrates the integration of Computer Vision, Human-Computer Interaction (HCI), and Game Development concepts using Python.

---

## Features

* Real-time hand tracking using MediaPipe
* Gesture-based shape selection
* Interactive shape placement
* Live shape preview
* Multiple geometric shapes

  * Square
  * Rectangle
  * Triangle
  * Circle
* Undo functionality
* Clear canvas functionality
* Minimalistic gesture-controlled interface

---

## How It Works

### Shape Selection

The left hand is used to select shapes.

| Gesture     | Shape     |
| ----------- | --------- |
| Fist        | Square    |
| One Finger  | Rectangle |
| Two Fingers | Triangle  |
| Open Palm   | Circle    |

### Shape Placement

The right hand controls the position of the selected shape.

* Move the right index finger to move the preview shape.
* Make a fist with the right hand to place the shape on the canvas.

### Keyboard Controls

| Key | Function               |
| --- | ---------------------- |
| Z   | Undo last placed shape |
| R   | Clear canvas           |
| ESC | Exit application       |

---

## Technology Stack

### Programming Language

* Python

### Libraries Used

* OpenCV
* MediaPipe
* Pygame
* NumPy

---

## Project Structure

```text
gesture_builder/
│
├── main.py
│
├── vision/
│   ├── camera.py
│   ├── hand_tracker.py
│   └── gesture_detector.py
│
├── game/
│   ├── renderer.py
│   └── shape_manager.py
│
├── models/
│   ├── shape.py
│   └── placed_shape.py
│
└── requirements.txt
```

---

## Installation

### Clone the Repository

```bash
git clone <repository-link>
cd gesture_builder
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
python -m pip install -r requirements.txt
```

---

## Running the Project

```bash
python main.py
```

---

## Applications

* Human-Computer Interaction (HCI)
* Gesture-Based Interfaces
* Interactive Learning Systems
* Computer Vision Projects
* Educational Demonstrations
* Creative Design Tools

---

## Future Enhancements

* Additional gesture commands
* Shape resizing and rotation
* 2.5D visual effects
* Object grouping
* Save and load creations
* Custom shape libraries
* AI-assisted shape recognition

---

## Learning Outcomes

This project helped explore:

* Computer Vision fundamentals
* Hand landmark detection
* Gesture recognition
* Real-time interactive systems
* Event-driven programming
* Pygame rendering
* Python project structuring
* Human-Computer Interaction design

---

## Author

Shreya Mattimadu

PES University, Bengaluru

Computer Science and Engineering
