# Books To Scrape - Check In Stock #
![](https://img.shields.io/badge/Python-3.8-blue.svg)

Script to scrap and check if a book with its topic is in Stock or not


#### Config your Enviroment ####

- Create a virtualenv


- Install the requirements
```
pip install -r requirements.txt
```


#### How to Run ####

Change the tile and topic in function __main__

```
if __name__ == "__main__":
    print(in_stock(title="While You Were Mine", topic="Historical Fiction"))

```

```
python book-store.py
```

#### Credits ####

Paulo Henrique