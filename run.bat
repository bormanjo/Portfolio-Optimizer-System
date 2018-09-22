docker build -t portfolio_optimizer .
docker run -it -p 8888:8888 -v %cd%:/home/Github/ portfolio_optimizer 
start chrome --new-window "http://localhost:8888"