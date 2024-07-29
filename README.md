# URL Shortener & Rate Limiter

## Introduction
This project implements a URL shortening service similar to TinyURL, with a rate limiter that processes up to 10 URLs per minute. The project is built in Python using the `pyshorteners` library for URL shortening and includes rate limiting to control the number of requests.

## Prerequisites
Before running this project, ensure you have the following installed:

- **Python 3.6+: This project requires Python 3.6 or higher.
- **pyshorteners library: A Python library for shortening URLs.

You can install the required library using pip:

```sh
pip install pyshorteners
```

## Steps to Run the Project
Follow these steps to run the URL shortener with rate limiting:

### Clone the Repository:
Clone the project repository from GitHub to your local machine.

```sh
git clone https://github.com/shubhampatil212/Tiny-URL.git
```

## Navigate to the Project Directory:
Change to the directory where the project files are located.

```sh
cd shubhampatil212/Tiny-URL
```

### Run the Script:
Execute the Python script to start the URL shortening process.

```sh
python main.py
```

The script will prompt you to enter a list of URLs. It processes up to 10 URLs per minute, shortening each URL and printing the original and shortened URLs.

## Conclusion
This project demonstrates a simple URL shortening service with rate limiting using Python. It can be easily expanded with more features, such as a web interface, database storage, or additional URL shortening providers. Feel free to contribute to the project by submitting issues or pull requests on GitHub.
```
