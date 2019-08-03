# Stego-CLI App


#### What is Stegonography?

Steganography is the practice of concealing a file, message, image, or video within another file, message, image, or video (from Wikipedia).
<hr>
This app allows both injecting and extracting text messages into/from a given PNG image (a 'carrier').

#### Build With
* PIL - a Python Imaging Library
* Numpy - a powerful package for scientific computing and working with N-dimensional arrays

## Requirements

* python (2.6.X and later)

## Installing

Using `git clone`:
```
git clone https://github.com/ofir1080/stegonography-cli-app.git
```

## Running App

```
python StegoApp.py
```
![main_menu](https://i.ibb.co/vqQX77s/Screen-Shot-2019-08-02-at-21-25-42.png)

## Project Structure

#### Modules

* inject.py - responsible for injecting a given message into the carrier image represented by a Numpy 3-d array
* extract.py - responsible for extracting the concealed message from a given carrier

#### Class Objects

* Carrier - 3-d Numpy array of shape (height, width, 3) where 3 is for RGB format.
* BitMsg - 1-d Numpy array consisted of zeros and ones representing the message as bits. Before the conversion the character 'ÿ' is concatenated in order to mark where the end of the message is.

#### Project Diagram

![project_diagram](https://i.ibb.co/YkFBN0x/stegoapp-uml-diagram.png)

## How does it work?

![flow_diagram](https://i.ibb.co/qRyxBkh/Untitled-Diagram-2.png)

## Authors

**Ofir Abramovich**
