docker build -t portfolio_optimizer .
docker run --rm -it -p 8888:8888 -v "//c/Users/J-C Borman/Github/":/home/Github/ portfolio_optimizer 
start chrome --new-window "http://localhost:8888"