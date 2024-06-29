# advanced-testing-techniques
This is a repo for doing advanced testing

## setup project

1. Create and source virtualenv

```bash
virtualenv ~/.advanced-testing
source ~/.advanced-testing/bin/activate
```

2. create scaffold 

```bash
touch Makefile && touch test_hello.py && touch hello.py && touch requirements.txt
```

3. populate `Makefile`

```bash
install:
    pip install --upgrade pip &&\
        pip install -r requirements.txt

test:
    python -m pytest -vv --cov=hello --cov=hellocli test_hello.py

lint:
    pylint --disable=R,C hello.py hellocli.py

all: install lint test
```
