# Collision Mathematics
This section holds the Collision Mathematics system of the AR Billiards project. The code is divided into a C-like system of files. One is labelled as a header, the other as a script. The header contains all the general form functions used to calculate the trajectory and impact path of whatever ball is requested based on a set of input variables. The script file calls the functions written in the header and inputs the required information into each called function. The script will run as long as there is data being fed.

## Prerequisites
* Python3 installed

## Setup
1. Open project in command line
2. Run `pip install virtualenv`
3. Run `python -m venv env`
4. Run `env\Scripts\activate`
5. Run `pip install -r requirements.txt`

## Collision Mathematics Basic Usage

This is to be used in unison with the Hololens and Image Processing portions of the project. Running them outside of these confitions will run through some calculations once and return the trajectory and location values according to whatever inputs you gave it, assuming you actually inserted values. Otherwise, it's gonna get mad without data to chew on.
