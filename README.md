

## About The Project

A test project exploring plotly and the ways we can create a data dashboard.


### Built With

* [Python](https://python.org/)
* [Plotly](https://plotly.com/)
* [Pandas](https://pandas.pydata.org/)
* [Pytest](https://pytest.org/)


### Prerequisites

In order to run the application you will need to install the following.
* python
 Download python at https://python.org/downloads/

* Plotly
```sh
    pip install dash
```
* pandas
  ```sh
    pip install pandas
  ```


### Installation

Clone the repo
   ```sh
   git clone https://github.com/adrianclay/dash-example.git
   ```

## Usage

To run the application and start the server
```sh
  python main.py
```

This will start the server. To see the dashboard go to http//127.0.0.1:8050/ in your browser

To end the session simply type control^ C for Mac 
## Testing

Unit tests are written in Pytest and can be found in the /tests directory. 

To execute the tests
```sh
  python -m pytest
```

## Data

The road casualty statistics were downloaded from [data.gov.uk](https://data.gov.uk/dataset/cb7ae6f0-4be6-4935-9277-47e5ce24a11f/road-safety-data).
