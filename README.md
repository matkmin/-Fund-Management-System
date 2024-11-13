# Fund Management System

This is a web application built with Django for managing investment funds. The system allows users to add, list, and view details about investment funds.

## Features

- Add new investment funds
- View details of investment funds
- Manage fund information, including performance, assets, and managers

## Technologies Used

- Django (Python web framework)
- SQLite (Database)

## Setup and Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/matkmin/-Fund-Management-System.git

   cd Fund-Management-System

   python3 -m myENV env

   source myENV/bin/activate

   python manage.py migrate

   python manage.py createsuperuser

   python manage.py runserver
   ```

### 2. **Database Schema**

This section provides details about the database schema, which can help developers understand the structure of the data.

````markdown
## Database Schema

The system uses an SQLite database with the following table schema:

### InvestmentFund

| Field                  | Type                                      | Description                        |
| ---------------------- | ----------------------------------------- | ---------------------------------- |
| `fund_id`              | Integer (Primary Key)                     | Unique identifier for the fund     |
| `fund_name`            | String (max_length=100)                   | Name of the investment fund        |
| `fund_manager_name`    | String (max_length=100)                   | Name of the manager of the fund    |
| `fund_desc`            | Text                                      | Description of the fund            |
| `fund_net_asset_value` | Decimal (max_digits=10, decimal_places=2) | Net Asset Value of the fund        |
| `fund_created_date`    | Date (auto_now_add=True)                  | Date when the fund was created     |
| `fund_performance`     | Decimal (max_digits=10, decimal_places=2) | Performance percentage of the fund |

## Sample Requests and Responses

### 1. Get List of Funds (GET `/funds/`)

#### Request:

```bash
GET http://127.0.0.1:8000/funds/

[
  {
    "fund_id": 1,
    "fund_name": "Sample Fund",
    "fund_manager_name": "John Doe",
    "fund_desc": "A sample investment fund for testing purposes",
    "fund_net_asset_value": "1000000.00",
    "fund_created_date": "2024-11-13",
    "fund_performance": "5.00"
  },
  {
    "fund_id": 2,
    "fund_name": "Aham Management Berhad",
    "fund_manager_name": "Versa",
    "fund_desc": "Versa Wallet",
    "fund_net_asset_value": "100.00",
    "fund_created_date": "2024-11-13",
    "fund_performance": "2.00"
  },
  {
    "fund_id": 3,
    "fund_name": "Sample Fund",
    "fund_manager_name": "John Doe",
    "fund_desc": "A sample investment fund for testing purposes",
    "fund_net_asset_value": "1000000.00",
    "fund_created_date": "2024-11-13",
    "fund_performance": "5.00"
  }
]

POST http://127.0.0.1:8000/funds/
Content-Type: application/json

{
    "fund_name": "Fund C",
    "fund_manager_name": "Manager C",
    "fund_desc": "A new investment opportunity.",
    "fund_net_asset_value": 2000000.00,
    "fund_performance": 12.00
}
Response:
{
    "fund_id": 3,
    "fund_name": "Fund C",
    "fund_manager_name": "Manager C",
    "fund_desc": "A new investment opportunity.",
    "fund_net_asset_value": 2000000.00,
    "fund_created_date": "2024-11-01",
    "fund_performance": 12.00
}

GET http://127.0.0.1:8000/funds/1/
Response:
{
    "fund_id": 1,
    "fund_name": "Sample Fund",
    "fund_manager_name": "John Doe",
    "fund_desc": "A sample investment fund for testing purposes",
    "fund_net_asset_value": "1000000.00",
    "fund_created_date": "2024-11-13",
    "fund_performance": "5.00"
  },

PUT http://127.0.0.1:8000/funds/1/update-performance/
Content-Type: application/json

{
    "fund_performance": 12.00
}
Response:
{
    "fund_id": 1,
    "fund_name": "Sample Fund",
    "fund_manager_name": "John Doe",
    "fund_desc": "A sample investment fund for testing purposes",
    "fund_net_asset_value": "1000000.00",
    "fund_created_date": "2024-11-13",
    "fund_performance": "12.00"
  },

DELETE http://127.0.0.1:8000/funds/1/
Response:
{
    "message": "Fund deleted successfully."
}

### 4. **Testing**

You can also mention how users can run tests to ensure everything is functioning properly. You can provide an example of how to run tests for the API and database.

```markdown
## Testing

To run the tests, use the following command:

```bash
python manage.py test

### 5. **Error Handling**

It's good to explain the error handling mechanism for invalid requests, missing resources, etc.

```markdown
## Error Handling

If an invalid request is made, such as a missing required field, the system will return an error response. Here are some example responses:

- **400 Bad Request**: When the request is missing required data.
- **404 Not Found**: When a fund with the given ID does not exist.
- **500 Internal Server Error**: When there is an unexpected issue with the server.

Example error response for a missing fund:

```json
{
    "error": "Fund with the specified ID does not exist."
}

```
````
