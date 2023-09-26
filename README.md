## Overview 

**Background**:
Tourists often have limited time to explore their destination cities. Recognizing this challenge, our 6-person team embarked on a project to assist tourists in navigating New York City more efficiently.

**Objective**:
To develop a comprehensive mobile and web application that leverages machine learning predictions to guide users in making well-informed decisions, maximizing their sightseeing experience within the city's constraints.

**Key Features**:

- **User Authentication**: Our application integrates a secure user registration and login system, ensuring personalized experiences and security for user data.

- **Personalized Itinerary**: Users can effortlessly craft their own itinerary based on their interests and our busyness predictions, ensuring a tailored travel experience for each individual.

- **Busyness Predictions**: The core of our application integrates two machine learning models: 
  1. Predicting the busyness levels across different areas in Manhattan.
  2. Offering insights on the anticipated busyness of specific Points of Interest (POIs).
  
- **Heat Map Visualization**: A user-friendly heat map showcases the predicted busyness levels, granting users a bird's-eye view of where crowds are expected.

- **Bucket List Functionality**: Users can curate and manage a list of places they'd like to visit, aided by our prediction insights.

**Tech Stack**:

- **Backend**: Developed with a Test Driven Development (TDD) approach using Django and PostgreSQL, ensuring the delivery of robust and scalable features.
  
- **Frontend**: Designed for both mobile and desktop devices, we used industry-standard technologies like React and React Native to ensure a responsive and adaptive user experience.

- **Data & Predictive Modelling**: We employed Random Forest and Linear Regression techniques to build our two distinct prediction models, allowing for versatile and accurate predictions.
  
- **Deployment**: Leveraged AWS for hosting and deploying our applications to reach a wide audience.

**Feedback**:
Upon evaluation, our product achieved an average CSAT (Customer Satisfaction Score) of 8.75/10. Additionally, 75% of users indicated they would likely recommend our application to others.

## Backend Design
### Basic User Flow Design
* User login
* view map
* select tags
* view related pois
* Add pois to bucketlist
* view itinerary in own bucketlist
<div align="center">
    <img src="https://github.com/ZRQ-rikkie/Travel-in-Manhaton/assets/74203373/e96dde02-7a30-499b-aa34-618f4bc620fc" width="70%"/>
</div>

### Server-side Logic
* Receive Requests: Capture user actions from frontend.  
* User Verification:
  * Registration: Check if new, save data if unique.
  * Login: Validate email & password, return token/session ID.
  * Authentication: Validate user credentials for
  * certain  actions (e.g., bucket list additions).
* Data Processing:
  * POI: Query relevant data from POI table.
  * Weather: Access WeatherData for relevant info.
  * Traffic Forecast: Use PredictZone & PredictPOI based on  the user's location.
* Response:
  * Send data/results back to frontend.
<div align="center">
    <img src="https://github.com/ZRQ-rikkie/Travel-in-Manhaton/assets/74203373/3c906df6-6f65-484a-87b6-4887aecc4f7c" width="70%"/>
</div>


### Database Integration
<div align="center">
    <img src="https://github.com/ZRQ-rikkie/Travel-in-Manhaton/assets/74203373/84721198-01ba-4b9a-b4b7-cbebb4bbd6e4" width="70%"/>
</div>

**Reasons for Choosing PostgreSQL**
* Geospatial support with PostGIS
* Rich set of data types
  
**Django ORM Integration**
* Model Definitions
* Simplified Queries
  
**Data Sources and Updates**
* Data Sources: Weather forecasts, crowd flow  predictions, POI info.
* Regular Data Updates: How data is kept current and accurate.


### Testing

**Test-Driven Development (TDD):**
* Began coding with TDD to ensure robustness from the start.
* Benefits: Clear requirements, early bug detection, and efficient code  structure.
**Unit Testing with Pytest:**
* Validated individual components/functions for expected behavior.
* Isolated testing ensures core functionalities are solid.
**Integration Testing:**
* Tested interactions between integrated components.
* Ensured seamless and error-free data flow and processes.
**Test Reports:**
* Generated comprehensive test reports.
* Allowed easy visualization of test results, failures, and coverage.

### Key Challenges  & Our Solutions

**Handling Massive Geographic Coordinate Data**
* Optimized Storage
* Spatial Indexing:
* Data Simplification
  
**Managing API Load with Over 200 POIs**
* Time-based Pagination
* Database Query Optimization
* Redis to optimize the response time







