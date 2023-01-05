stocks_data = {
    'TSLA': {
        "stock_prices":
            {'1-1-2023': {
                "open_price": 402.7,
                "close_price": 430.7,
                "volume": 10000232
            },
            '2-1-2023': {
                "open_price": 401.4,
                "close_price": 423.7,
                "volume": 1034232
            }
        },
        "company_details": {
            "ceo": "Elon Musk",
            "employees_num": 20000,
            "hq_address": "California"
        }
    },
    'AAPL': {
        '1-1-2023': {
            "open_price": 204.7,
            "close_price": 235.7,
            "volume": 374656
        },
        '2-1-2023': {
            "open_price": 239.7,
            "close_price": 213.7,
            "volume": 545768
        }
    }
}

# print(stocks_data['TSLA']['2-1-2023']['volume'])
print(stocks_data['TSLA']['company_details']['ceo'])