
appname=flask_app
testname=test_api.py

build:
	docker build -t $(appname) .
run:
	docker run -d -p 5000:5000 $(appname)
kill: 
	docker stop $(appname)
	docker container prune -f
	docker rmi -f $(appname)

test:
	pytest $(testname)  