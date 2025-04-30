# Studentenwohnheim Virtual Agent (Pepper Robot)

This project implements a virtual agent inspired by the Pepper robot, designed to assist students in finding accommodation (Studentenwohnheim) using face recognition and conversational AI.

## Project Overview

- The agent uses a camera to detect and recognize faces.
- It remembers users by their faces and associates them with their names.
- The system helps students search for and get information about student housing.
- The conversational logic is tailored for the Studentenwohnheim context.

## Features

- Face recognition: Remembers and identifies users.
- Personalized interaction: Greets users by name and recalls previous interactions.
- Accommodation search: Assists students in finding suitable housing options.
- Conversational interface: Interact via text or speech.

## Project Structure

- `face.py`: Face detection and recognition logic.
- `camera.py`: Camera integration for real-time face capture.
- `behavior_realizer.py`, `bml.py`: Behavior and interaction logic.
- `actions/`: Custom actions for the conversational agent.
- `data/`: NLU, stories, and rules for the agent.
- `audio.mp3`: Audio output sample.
- `config.yml`, `domain.yml`, etc.: Configuration files.

## Setup

1. Clone the repository.
2. Create and activate a Python 3.8 virtual environment.
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Train the conversational model (if using Rasa):
   ```
   rasa train
   ```
5. Run the agent and supporting modules as needed.

## Usage

- Start the camera and face recognition modules.
- Interact with the agent to search for student accommodation.
- The agent will remember returning users and personalize responses.

