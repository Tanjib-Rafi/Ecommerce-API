
## Setup instructions

First, clone the repository to your local machine:

```bash
git clone https://github.com/Tanjib-Rafi/Ecommerce-API.git
```

Install the requirements:

```bash
pip install -r requirements.txt
```

Apply the migrations:

```bash
python3 manage.py migrate
```

Finally, run the development server:

```bash
python manage.py runserver
```

The API endpoints will be available at:
 http://127.0.0.1:8000/api/


## API Endpoints

### User Endpoints

| Action                | HTTP Method | Endpoint               |
|-----------------------|-------------|------------------------|
| Register for an account | POST        | `/api/users/register/` |
| Login                 | POST        | `/api/users/login/`    |
| Logout                | POST        | `/api/users/logout/`   |

### Product Endpoints

| Action                       | HTTP Method | Endpoint                            |
|------------------------------|-------------|-------------------------------------|
| List and create products     | GET, POST   | `/api/products/products/`           |
| Retrieve, update, delete product | GET, PUT, DELETE | `/api/products/products/<int:pk>/` |
| List and create categories   | GET, POST   | `/api/products/categories/`         |
| Retrieve, update, delete category | GET, PUT, DELETE | `/api/products/categories/<int:pk>/` |
| List and create brands       | GET, POST   | `/api/products/brands/`             |
| Retrieve, update, delete brand | GET, PUT, DELETE | `/api/products/brands/<int:pk>/`   |
| List and create product variations | GET, POST | `/api/products/variations/`       |
| Retrieve, update, delete product variation | GET, PUT, DELETE | `/api/products/variations/<int:pk>/` |
| List and create reviews      | GET, POST   | `/api/products/reviews/`            |
| Retrieve, update, delete review | GET, PUT, DELETE | `/api/products/reviews/<int:pk>/` |
| List and create wishlists    | GET, POST   | `/api/products/wishlists/`          |
| Retrieve, update, delete wishlist | GET, PUT, DELETE | `/api/products/wishlists/<int:pk>/` |

### Order Endpoints

| Action                       | HTTP Method | Endpoint                            |
|------------------------------|-------------|-------------------------------------|
| List and create orders       | GET, POST   | `/api/orders/orders/`               |
| Retrieve, update, delete order | GET, PUT, DELETE | `/api/orders/orders/<int:pk>/`    |
| List and create order items  | GET, POST   | `/api/orders/order-items/`          |
| Retrieve, update, delete order item | GET, PUT, DELETE | `/api/orders/order-items/<int:pk>/` |
| List and create carts        | GET, POST   | `/api/orders/carts/`                |
| Retrieve, update, delete cart | GET, PUT, DELETE | `/api/orders/carts/<int:pk>/`     |
| List and create coupons      | GET, POST   | `/api/orders/coupons/`              |
| Retrieve, update, delete coupon | GET, PUT, DELETE | `/api/orders/coupons/<int:pk>/`  |

### Payment Endpoints

| Action                       | HTTP Method | Endpoint                            |
|------------------------------|-------------|-------------------------------------|
| List and create payments     | GET, POST   | `/api/payments/payments/`           |
| Retrieve, update, delete payment | GET, PUT, DELETE | `/api/payments/payments/<int:pk>/` |

### Address Endpoints

| Action                       | HTTP Method | Endpoint                            |
|------------------------------|-------------|-------------------------------------|
| List and create addresses    | GET, POST   | `/api/addresses/addresses/`         |
| Retrieve, update, delete address | GET, PUT, DELETE | `/api/addresses/addresses/<int:pk>/` |

### Admin Endpoint

| Action       | HTTP Method | Endpoint    |
|--------------|-------------|-------------|
| Admin panel  | GET         | `/admin/`   |

## Example Usage

To register for an account, send a POST request to:

```http
POST /api/users/register/

```JSON
{

}
```

