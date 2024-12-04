## Environment:
- Java version: 11
- Gradle version: 7.3.3
- Spring Boot version: 2.6.3

## Instructions:
- You only have to finish up the files inside the controller and the service folder.
- When modifying the code, navigate to the IDE's Run tab and click on the BUILD button to compile the project.
- Check the terminal logs for any code or build errors.
- The PostgreSQL environment can be accessed through the terminal.
- To start the server, go to the IDE's Run tab and click on the "Start Server" button. You can monitor the progress in the terminal logs.
- Once the server is started, navigate to the Thunder Client's tab  ![Thunder client's tab](https://github.com/sumati95/ThunderClient/blob/main/Screenshot%20from%202024-02-01%2014-12-22.png?raw=true) and make a new request.
- Test the API endpoints by visiting http://localhost:8001/{endpoints}. You can view the JSON response in the "Response" tab.
- Thoroughly test your APIs before clicking the SUBMIT button in the IDE.

## Project Structure:
1. src/main/java/com/example/shoe: 

    a. **model package**: Contains the Shoes entity class with attributes, contructors, getters and setters. 

    The Shoes entity should have the following attributes:
    
    - **id**       : the unique id of the shoes(`Integer`)
    - **name**     : the name of the shoes (`String`)(`Not Null or Empty`)
    - **brand**    : the brand name of the shoes (`String`)(`Not Null or Empty`)
    - **color**    : the color of the shoes (`String`)(`Not Null or Empty`)
    - **quantity** : the quantity of the shoes (`Integer`)(`should be greater than or equal to zero`)
    - **material** : the material of the shoes (`String`)(`Not Null or Empty`)
    - **price**    : the price of the product (`Double`)(`should be greater than zero`)

    b. **repository package**: Contains the interface ShoesRepository extending JpaRepository. 

    c. **service package**: Contains ShoesService interface with incomplete methods. 

    d. **controller package**: Contains ShoesController with skeleton CRUD API endpoints. 

2. src/main/resources: 
    
    a. application.properties: Configuration for database connection.

## Read-Only Files:
- src/main/java/com/example/Shoe: All the files except controller/ShoesController.java and service/ShoesService.java are read-only
- src/test/*
- All the envrionment related files are read-only

## Requirements

A Local Shoes Company wants to expand its business to a digital system. Implement REST APIs to facilitate the operations that can add the new Shoes details and retrieve the Shoes based on the shoesId.

Here is an example of a Shoes JSON object:
```
{ 
   "name" :"Women's walking shoes",
   "brand":"Sparx",
   "color":"Grey",
   "quantity":5,
   "material":"Mesh",
   "price":891.0
}

```

 Your task is to implement a set of REST services that exposes the endpoints, save the provided Shoes information and retrieve the Shoes order data based on the requested shoesId.

| API Route               | Methods  | Success Response Code  | Validation Error Code  |
|-------------------------|----------|------------------------|------------------------|
| /shoes                  | POST     | 201                    | 400                    |
| /shoes/{shoesId}        | GET      | 200                    | 404                    |

### Task 1: Service Layer Implementation in ShoesService
Implement the business logic in the service layer using ShoesRepository

**Method Details**:

- **saveShoes()**: Implement the POST method which should save a Shoes data
- **getShoesById()**: Implement the GET method which should get a Shoes data based on the shoesId

### Task 2: REST API Endpoints in ShoesController

**POST request to /shoes**

- save the Shoes details based on the requested information.
- **Response Body**: JSON object representing the Shoes details.
- **HTTP Status Code**: 
  - 201 - If the Shoes data gets saved 
  - 400 - If requested data contains incorrect values or any of the field is invalid

**GET request to /shoes/{shoesId}**

- Get the Shoes details by shoesId.
- **Response Body**: should display the Shoes Object in JSON based on the requested shoesId
- **HTTP Status Code**: 
  - 200 - if the specified shoes details are found
  - 404 - if the specified shoes details are not found


Complete the given project so that it passes all the test cases when running the provided unit tests. 
    
**Example Requests and Responses:**

`POST` request to `/shoes`:

Request Body
```
  { 
   "name" :"Women's walking shoes",
   "brand":"Sparx",
   "color":"Grey",
   "quantity":5,
   "material":"Mesh",
   "price":891.0
}
```
The response code is 200 and the response body, when converted to JSON, is as follows:
```
  {
   "id": 6,
   "name": "Women's walking shoes",
   "brand": "Sparx",
   "color": "Grey",
   "quantity": 5,
   "material": "Mesh",
   "price": 891.0
 }
```
This adds a new object to the collection with the given properties having id 1.

`GET` request to `/shoes/{shoesId}`

The response code is 200 and the response body for requested { shoesId : 6 } should return a message as follows:
```
  {
    "id": 6,
    "name": "Women's walking shoes",
    "brand": "Sparx",
    "color": "Grey",
    "quantity": 5,
    "material": "Mesh",
    "price": 891.0
  }
```

**Note:**
- The endpoints for GET method have been provided in the ShoesController.java file