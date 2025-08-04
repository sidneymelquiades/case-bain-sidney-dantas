# Predict Chilean Property Price API - Bain & Company Case

## Author: Sidney Dantas

This API was developed as a solution for a case proposed by **Bain & Company**, with the objective of predicting the price of real estate — houses and apartments — in the metropolitan region of Santiago, Chile, based on physical characteristics and geographic location.

The solution was implemented in a practical manner, adopting a simple and introductory approach. However, it is important to note that for use in a real-world scenario, several architectural and process improvements would be necessary.

---

## Objective

Receive information about a property (such as type, sector, area, number of rooms, latitude, and longitude) and return a price prediction based on a pre-trained machine learning model.

---

## How to run the API

### Prerequisites

- Python 3.9 or higher  
- Docker  

### 1. Clone the repository

```bash
git clone https://github.com/sidneymelquiades/case-bain-sidney-dantas.git
cd case-bain-sidney-dantas
```

### 2. Build the application

```bash
docker build -t case-bain .
```

### 3. Run the application via Docker

```bash
docker run -p 8000:8000 case-bain
```

---

## Authentication

To use the API endpoints, a valid `API Key` must be provided in the request header:

```
Key: api_key
Value: supersecretkey
```

Available keys (defined via the `config.yaml` file):

```yaml
api_keys:
  - key: "supersecretkey"
  - key: "outrachave123"
```

---

## Input - `PropertyInput` Schema

```json
{
  "type": "casa",
  "sector": "nunoa",
  "net_usable_area": 80.0,
  "net_area": 100.0,
  "n_rooms": 3,
  "n_bathroom": 2,
  "latitude": -33.45,
  "longitude": -70.65
}
```

### Validations and Assumptions

Certain assumptions were adopted to ensure a minimum level of reliability in the model's predictions. They are:

The `type` field must contain only the values "departamento" or "casa", limiting the analysis to these two property types (as defined in the provided dataset).  
The `sector` field must match one of the following neighborhoods: Vitacura, La Reina, Las Condes, Lo Barnechea, Providencia, or Ñuñoa — ensuring the model only works with well-defined regions within the project scope.  
The `net_usable_area` and `net_area` fields, representing the usable and total property areas respectively, must be greater than zero to avoid invalid or inconsistent records.  
The `latitude` must be between -34 and -30.  
The `longitude` must be between -73 and -68, restricting the data to a coherent urban geographic range.

- `type`: only "departamento" or "casa"
- `sector`: one of the following neighborhoods:
  - vitacura, la reina, las condes, lo barnechea, providencia, nunoa
- `net_usable_area` and `net_area`: must be > 0
- `latitude`: between -34 and -30
- `longitude`: between -73 and -68

---

## Output - `PredictionOutput` Schema

```json
{
  "price": 123456789.0
}
```

---

## Swagger Documentation

Access the interactive API interface:

- [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Machine Learning Model

The model was trained using a pipeline composed of the following steps:

First, data preprocessing is performed, which includes encoding categorical variables and cleaning the data to ensure quality and consistency.

Next, a Gradient Boosting regressor is applied — a machine learning algorithm for regression that combines multiple weak learners to form a strong predictive model.

To evaluate model performance, metrics such as Root Mean Squared Error (RMSE), Mean Absolute Error (MAE), and Mean Absolute Percentage Error (MAPE) are used to assess the accuracy and quality of the predictions.

This entire process is organized in scripts located at `pipeline/train.py` and configured through the `pipeline/config.yaml` file.

---

## Future Improvements

While the case required a simple and introductory solution, it would be highly advisable to evolve the project’s architecture by incorporating a CI/CD pipeline using tools such as Jenkins and Spinnaker. This would allow the model retraining process to be performed in a less bureaucratic and more efficient manner.

---

## Author

- **Sidney Melquiades Dantas**  
- [sidneymelquiadesdantas@gmail.com](mailto:sidneymelquiadesdantas@gmail.com)  
- [github.com/sidneymelquiades](https://github.com/sidneymelquiades)  
- [LinkedIn](https://www.linkedin.com/in/sidneymelquiadedantas/)

---