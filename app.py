from flask import Flask, render_template
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc

server = Flask(__name__)

app = dash.Dash(server=server, routes_pathname_prefix="/skills_viz/")

df = pd.read_excel('madison_skills.xlsx')

fig = px.bar_polar(df, r="professional experience (years)", theta="skill",
                   color="relative strength", template="ggplot2", color_continuous_scale='delta_r', title="Madison\'s Top Skills")

app.layout = dcc.Graph(figure=fig, style={"width": "100%"})

nds = [('Computer Vision Nanodegree', 'Facebook Secure and Private AI Nanodegree Scholar', 'December 2019'), ('Deep Reinforcement Learning Nanodegree', 'Facebook PyTorch Nanodegree Scholar', 'November 2019'),
('Deep Learning Nanodegree', 'Facebook PyTorch Nanodegree Scholar', 'May 2019'), ('Front-End Web Development Nanodegree','Grow with Google Nanodegree Scholar', 'November 2018')]
certs = [('Dataquest Data Scientist in Python', 'August 2019 Diversity Scholarship'), ('Dataquest Data Analyst with Python', 'July 2019 Diversity Scholarship'),
('Fundamentals of Scalable Data Science', 'February 2019 IBM’s Applied AI Scholarship'), ('DataCamp Python Programmer', 'February 2019 Women and Gender Minorities Scholarship')]
sps = [('Multi-Agent Reinforcement Learning','trained a pair of agents to play tennis using Unityagents, NumPy, and PyTorch. Completed December 2019'), 
('Automatic Image Captioning', 'combined a PyTorch CNN and a PyTorch RNN to build a computer vision network that automatically produces captions, given an input image. Completed November 2019'), 
('AWS Sentiment Analysis Model', 'deployed a PyTorch sentiment analysis model. Created a gateway for accessing the model from a website using AWS. Completed May 2019')]

prjs = [('Kaggle NLP', 'https://github.com/madisonestabrook/kaggle_nlp', 'For this project, I completed Kaggle\'s Natural Language Processing course. Completed May 2020', 'Madison_Kaggle_NLP.png', 'My Kaggle NLP course certificate'), 
('Computer Vision Nanodegree Project 3 - SLAM', 'https://github.com/madisonestabrook/CVND_P3_SLAM', 'For this project, I implemented SLAM for robot that moves and senses in a 2-dimensional grid world. Completed December 2019', 'SLAM.png', 'A graph of the robot\'s poses'),
('Computer Vision Nanodegree - Image Capationing', 'https://github.com/madisonestabrook/CVND_Image_Captioning', 'For this project, I used a PyTorch RNN and a PyTorch CNN to build an automatic image captioner. Completed December 2019', 'Image_with_Capation.png', 'An example image with capation'), 
('Deep Reinforcement Learning Nanodegree - Collaboration and Competition', 'https://github.com/madisonestabrook/P3_Collaboration_Competition', 'For this project, I used Deep Deterministic Policy Gradients (DDPG) Network to teach a pair (2) agents to play tennis. Completed November 2019', 'collab_and_competion.png', 'A graph of how well the agents scored over time'),
('Deep Reinforcement Learning Nanodegree - Continuous Control', 'https://github.com/madisonestabrook/DRL_Continuous_Control', 'For this project, I used a a Deep Deterministic Policy Gradients (DDPG) Network to train a double-jointed arm to move to target locations. Completed November 2019', 'cont_control.png', 'A graph of how well the arm scored over time'),
('Computer Vision Nanodegree - Facial Keypoint Detection', 'https://github.com/madisonestabrook/cv_facial_keypoint_detection', 'For this project, I used a PyTorch CNN to detect facial keypoints of a given input image. Completed October 2019', 'facail_keypoints.png', 'A photo of the Obamas with their facial keypoints visable.'),
('Deep Reinforcement Learning Nanodegree - Navigation', 'https://github.com/madisonestabrook/DRLND_Navigation', 'For this project, I used a Deep Q-Network (DQN) to train an agent that navigates a virtual world from sensory data. Completed September 2019', 'navigation.png', 'A graph of how well the agent scored over time'),
('AWS Sentiment Analysis Model', 'https://github.com/madisonestabrook/sagemaker-deployment', 'For this project, I deployed a PyTorch sentiment analysis model and created a gateway for accessing the model from a website using AWS. Completed May 2019', 'example_review.png', 'A screenshot of the model\'s website with an example review'),
('Deep Learning Nanodegree - TV Script Generation', 'https://github.com/madisonestabrook/dlnd_tv_script_generation', 'For this project, I used a PyToch RNN to generate a Seinfield TV script. Completed May 2019', 'sienfield_script.png', 'A screenshot of the output script'),
('Deep Learning Nanodegree - Face Generation', 'https://github.com/madisonestabrook/dlnd_face_generation', 'For this project, I defined and traind a PyTorch DCGAN on a dataset of faces to generate new faces. Completed May 2019', 'example_faces.png', 'A screenshot showing example faces'),
('Deep Learning Nanodegree - Dog Project', 'https://github.com/madisonestabrook/udacity-dog-project', 'For this project, I used a PyTorch Convolutional Neural Network (CNN) to classify dog breeds. Completed March 2019', 'example_dog.png', 'A screenshot showing an example dog with predicted breed'),
('Front End Nanodegree - Restaurant Reviews', 'https://madisonestabrook.github.io/mws-restaurant-stage-1-ryan/', 'For this project, I used a JavaScipt Service Worker to implement a mobile-first Progressive Web App (PWA). Completed Novemeber 2018', 'example_restaurant.png', 'A screenshot of the final project, showing an example restaurant'),
('Front End Nanodegree - Memory Game', 'https://madisonestabrook.github.io/fend-project-memory-game/', 'For this project, I used HTML, CSS, and vanilla (base) JavaScript to build a memory game. Completed August 2018', 'memory_game.png', 'A screenshot of the final project, showing the User Interface (UI)')]

@server.route("/")
def index():
    return render_template("index.html", Nanodegrees=nds, Certifications=certs, SelectedProjects=sps)

@server.route("/projects")
def projects():
    return render_template("projects.html", Projects=prjs)

if __name__ == '__main__':
    server.run(host="http://madisonestabrook.herokuapp.com/", debug=False)