# Smart Parking System using Fiware/Orion

This repository contains a Python application for simulating and managing the status of parking spots using Fiware/Orion Context Broker and a Flask web application to display real-time parking data.

## Prerequisites

- Docker
- Docker Compose

## Introduction

This project demonstrates a Smart Parking System built on Fiware technology, utilizing the Orion Context Broker and NGSIv2 protocol. The Context Broker is a key component for managing context information in a scalable and standardized way. NGSIv2 (Next Generation Service Interface) is the API specification used for interactions with the Context Broker.

## Setup

1. **Create Docker Images/Containers for MongoDB and FIWARE Context Broker**

   Open the terminal and run the following commands:

   ```bash
   docker pull mongo
   docker run -d --name mongodb -p 27017:27017 mongo
   docker pull fiware/orion
   docker run -d --name orion -p 1026:1026 --link mongodb:mongodb fiware/orion -dbhost mongodb
   ```

2. **Run the `parking_manager.py` Application**

   `parking_manager.py` is the Python application that interacts with the Context Broker to manage the status of Parking Spots using NGSI-V2. The `ParkingSpot` data model has been implemented to model 10 parking spots and randomly change their status at runtime. In the same directory as `Dockerfile`, `requirements.txt`, and `parking_manager.py` files, open the terminal and run:

   ```bash
   docker build -t parking-manager .
   docker run parking-manager
   ```

3. **Display Real-Time Parking Status**

   Build a new Docker container to extract the outcomes of parking-manager from Orion. To accomplish this, go to the `Display` folder and run:

   ```bash
   docker build -t parking-app .
   docker run -p 5000:5000 parking-app
   ```

   Results are displayed on [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Why Fiware/Orion and NGSIv2?

- **Scalability:** Orion Context Broker provides a scalable solution for managing and processing context information in real-time, making it suitable for applications with varying data volumes.

- **Standardization:** NGSIv2 is a standardized API that allows interoperability between different components and systems, promoting consistency and ease of integration.

- **Real-time Updates:** NGSIv2 enables real-time updates and queries, making it ideal for applications that require up-to-date context information, such as a Smart Parking System.

## Contributing

Feel free to contribute to enhance functionality or fix issues. Create a pull request or open an issue for discussions.
