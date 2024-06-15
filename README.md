# ForwarderAPI

ForwarderAPI is a simple Flask application that acts as a proxy to forward HTTP requests to another URL and returns the response. It provides a lightweight and easy-to-use interface for fetching data from external sources.

## Usage

1. Ensure you have Python installed on your system.
2. Install the required dependencies by running:
   ```bash
   pip install Flask requests
   ```
3. Run the Flask app by executing the following command:
   ```bash
   python app.py
   ```
4. The app will start running on `http://localhost:5000/`.
5. To forward a request to a specific URL, append the URL as a query parameter named `url` to the base URL. For example:
   ```
   http://fwd.achux.me/?url=https://api.example.com/data
   ```
6. The app will forward the request to the specified URL and return the response.

## Endpoint

### GET /

- **Parameters:**
  - `url`: The URL to which the request should be forwarded.
- **Response:**
  - If the request is successful (status code 200), the response will be in JSON format.
  - If the request fails, an error message along with the status code and error text will be returned.

## Example

To fetch data from an external API (e.g., `https://api.example.com/data`), you can send a GET request to:

```
http://localhost:5000/?url=https://api.example.com/data
```

## Notes

- This app is intended for development and testing purposes and may not be suitable for production use without additional security measures.
- Ensure that the external URLs you are forwarding requests to are trusted and secure to prevent potential security risks.
