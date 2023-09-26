# Travel-in-Manhattan: Enhance Your NYC Experience

A collaborative endeavor by a six-person team, this comprehensive app is designed to assist tourists in navigating New York City efficiently with the aid of machine learning predictions. Our team embraced the Scrum methodology to facilitate smooth collaboration, iterative development, and frequent feedback.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Backend Design](#backend-design)
  - [User Flow Design](#user-flow-design)
  - [Server-side Logic](#server-side-logic)
  - [Database Integration](#database-integration)
- [Testing](#testing)
- [Challenges & Solutions](#challenges-&-solutions)
- [Feedback](#feedback)

## Overview

Designed for tourists with limited time, our application leverages machine learning to guide users in making well-informed decisions, maximizing their sightseeing experience within NYC.

## Features

- **User Authentication**: Secure user registration and login system for personalized experiences.
- **Personalized Itinerary**: Effortlessly craft itineraries based on interests and busyness predictions.
- **Busyness Predictions**: 
  - Predicts busyness levels in different areas of Manhattan.
  - Offers insights on anticipated busyness at specific POIs.
- **Heat Map Visualization**: Displaying predicted busyness levels.
- **Bucket List Functionality**: Curate and manage a list of places to visit with prediction insights.

## Tech Stack

- **Backend**: Django and PostgreSQL with a Test Driven Development (TDD) approach.
- **Frontend**: React (Web) and React Native (Mobile).
- **Data & Predictive Modelling**: Random Forest and Linear Regression for accurate predictions.
- **Deployment**: AWS 

## Backend Design

### User Flow Design
<p align="center">
  <img src="https://github.com/ZRQ-rikkie/Travel-in-Manhaton/assets/74203373/e96dde02-7a30-499b-aa34-618f4bc620fc" width="50%" />
</p>

### Server-side Logic
- **Receive Requests**: Capturing user actions from the frontend.
- **User Verification**:
  - **Registration**: Check for uniqueness and save data.
  - **Login**: Validate credentials and return a session ID or token.
  - **Authentication**: Validate user credentials for specific actions (e.g., bucket list additions).
- **Data Processing**:
  - **POI**: Extract relevant data from POI table.
  - **Weather**: Obtain relevant weather information.
  - **Traffic Forecast**: Use PredictZone & PredictPOI based on the user's location.
- **Response**: Return data/results to the frontend.
  
<p align="center">
  <img src="https://github.com/ZRQ-rikkie/Travel-in-Manhaton/assets/74203373/3c906df6-6f65-484a-87b6-4887aecc4f7c" width="50%" />
</p>


### Database Integration
<p align="center">
  <img src="https://github.com/ZRQ-rikkie/Travel-in-Manhaton/assets/74203373/84721198-01ba-4b9a-b4b7-cbebb4bbd6e4" width="50%" />
</p>

- **Reasons for Choosing PostgreSQL**: Geospatial support with PostGIS and a rich set of data types.
- **Django ORM Integration**: Model definitions and simplified queries.
- **Data Sources and Updates**: Weather forecasts, crowd flow predictions, POI info, and the mechanism to keep data up-to-date.

## Testing

- **Test-Driven Development (TDD)**: Ensures robustness from the start.
- **Unit Testing with Pytest**: Validates individual components/functions.
- **Integration Testing**: Ensures seamless interaction between integrated components.
- **Test Reports**: Comprehensive reports for visualization of test results.

## Challenges & Solutions

- **Handling Massive Geographic Coordinate Data**: Solutions include optimized storage, spatial indexing, and data simplification.
- **Managing API Load with Over 200 POIs**: Solutions include time-based pagination, database query optimization, and using Redis for faster response times.

## Feedback

Our product achieved a CSAT score of 8.75/10. 75% of users would recommend our application to others.
