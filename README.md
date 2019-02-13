# ch2api
Politico API(ADC CHALLENGE 2)

[![Coverage Status](https://coveralls.io/repos/github/Egunza-dev/ch2api/badge.svg?branch=develop)](https://coveralls.io/github/Egunza-dev/ch2api?branch=develop)
[![Build Status](https://travis-ci.com/Egunza-dev/ch2api.svg?branch=develop)](https://travis-ci.com/Egunza-dev/ch2api)

## Politico API Features


1. The API can create a political office
2. The API can get all political offices
3. The API can get a specific political office.
4. The API can get all political parties.
5. The API can get a specific political party.
6. The API can edit name of a specific political party.
7. The API can delete a particular political party.
8. The API can create a political party.

## Installation

### Step 1

1. Clone the repository [```HERE```](https://github.com/Egunza-dev/ch2api.git)

2. Open terminal application on your local machine

3. On the terminal, run ``` git clone https://github.com/Egunza-dev/ch2api.git ``` command

```$ cd ch2api```

3. Create and activate virtual environment

```$ virtualenv api-env```

```$ source .env```

4. Install project dependencies 

```$ pip install -r requirements.txt```


### Step 2

#### Running the application

```$ flask run```

### Step 3

#### Testing

```$ pytest ```


### API Endpoints
#### Offices Endpoints : 

Method | Endpoint | Functionality
--- | --- | ---
```POST``` | ```/api/v1/offices``` | Create a political office
```GET``` | ```/api/v1/offices``` | Get all political offices
```GET``` | ```/api/v1/offices/int:office-id``` | Get a specific political party


#### Parties Endpoints : 

Method | Endpoint | Functionality
--- | --- | ---
```POST``` | ```/api/v1/parties``` | Create a political party
```GET``` | ```/api/v1/parties``` | Get all political parties
```GET ```| ```/api/v1/parties/int:party-id``` | Get a specific political party
```PATCH``` | ```/api/v1/parties/int:party-id/name``` | Edit name of a political party
```DELETE``` | ```/api/v1/parties/int:party-id``` | Delete a particular political party



