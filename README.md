# fast_api_sample

```
docker run --name mariadb-container -e MYSQL_ROOT_PASSWORD=root -p 3306:3306 -d mariadb
```

```
brew install k6
```

```
k6 run k6_test_scenario.js
```

mariadb 파라미터 확인

```

show variables like '%max_connect%';
show variables like 'wait_timeout';
set global max_connections=500;
set wait_timeout=60;

```

* 참고
-----

* [Python과 FastAPI로 지속 성장 가능한 웹서비스 개발하기 - 1. 의존성 주입](https://binaryflavor.com/python%EA%B3%BC-fastapi%EB%A1%9C-%EC%A7%80%EC%86%8D-%EC%84%B1%EC%9E%A5-%EA%B0%80%EB%8A%A5%ED%95%9C-%EC%9B%B9%EC%84%9C%EB%B9%84%EC%8A%A4-%EA%B0%9C%EB%B0%9C%ED%95%98%EA%B8%B0-1.-%EC%9D%98%EC%A1%B4%EC%84%B1-%EC%A3%BC%EC%9E%85/)
* [python-dependency-injector github](https://github.com/ets-labs/python-dependency-injector/blob/master/examples/miniapps/fastapi-sqlalchemy/webapp/containers.py)
* [Poetry를 이용한 멀티 프로젝트 Python 애플리케이션 개발 방법](https://techblog.lycorp.co.jp/ko/python-multi-project-application-with-poetry)
