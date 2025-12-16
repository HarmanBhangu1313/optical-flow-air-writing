# Optical Flow–Based Air Writing and Motion Tracking

##  Overview
This project implements a **motion tracking and air-writing system** using **Optical Flow**, a classical computer vision technique for estimating motion between consecutive video frames.

The goal is to track **hand movement in free space** and visualize the trajectory as text or drawings, demonstrating how motion information alone can be used for interaction without explicit object detection or deep learning models.

---

##  Key Concepts Covered
- Optical Flow (motion estimation)
- Sparse feature tracking
- Temporal motion consistency
- Hand movement analysis
- Classical computer vision pipelines

---

##  Tech Stack
- **Python**
- **OpenCV**
- **NumPy**

---

##  Project Structure
optical-flow-air-writing/
├── optical_flow.py
├── requirements.txt
└── README.md

---

## Pipeline Overview
1. Capture frames from webcam or video
2. Convert frames to grayscale
3. Detect good feature points to track
4. Compute optical flow between consecutive frames
5. Track motion vectors over time
6. Visualize trajectories as air-written patterns

---

##  Mathematical Intuition (Optical Flow)
Optical Flow estimates pixel motion by assuming **brightness constancy**:

I(x,y,t) = I( x+Δx, y +Δy, z+Δz)

Using a first-order Taylor expansion, this leads to the **Optical Flow Constraint Equation**:

I u + I v + I  = 0
 x     y     t

 
where:

-  I ,I  are spatial intensity gradients  
    x  y

- I  is the temporal gradient  
   t

- u,v represent horizontal and vertical motion  

Since this equation is underdetermined, additional constraints (e.g., local smoothness) are applied, as done in methods like **Lucas–Kanade Optical Flow**.

---

##  Results
- Successfully tracks hand motion in real time
- Produces smooth air-written trajectories
- Demonstrates motion-based interaction without deep learning

---

##  Notes
- This is a **classical computer vision project**
- No deep learning models are used
- Sensitive to lighting conditions and camera noise
- Intended for learning motion estimation concepts

---

##  Future Improvements
- Noise filtering for smoother trajectories
- Gesture classification on top of motion paths
- Integrating deep learning–based hand detection
- Using dense optical flow for richer motion capture