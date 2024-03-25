[API-DEV](https://www.youtube.com/watch?v=0sOvCWFmrtA&t=2329s)


1- Fastapi
2 - Define schema for data validation with pydantic
4 - Make sure patha parameters follow top to bottom priorities
5 - Primary key does not have to be id, for users it can be email for example
6 - Unique constraints ie for name. will throw an error if duplicate
7 - Constraint ie not null



### created a vm instance in digital ocean and deployed-0324
[Digital Ocean ](https://cloud.digitalocean.com/projects/a421873e-7bea-401c-a85a-05f5eee7cf7e/resources?i=2cde91)
### TODO - 03-24-24
1 - Wait for domain to be acitve
[Google Domains](https://domains.google.com/registrar/?_gl=1*skzyk*_ga*OTk2NzQ5MjQ5LjE3MTEzMDA5MzE.*_ga_9YWT2H669H*MTcxMTMwMDkzMS4xLjEuMTcxMTMwMDkzMS4wLjAuMA..)
2 - Get SSL Certificate [certbot](https://certbot.eff.org/)
3 - Firewall config sudo ufw enable

##### REF
[Docker-Python](https://hub.docker.com/_/python)

### Docker Compose for with file
 ```
 docker-compose -f docker-compose-prod.yml up -d
 ```
 ```
 docker-compose -f docker-compose-prod.yml down
 ```

 ### To Pull from Hub
 ```
 docker pull togai/fastapi-dev
```
 ### To Push New
 ```
 docker push togai/fastapi-dev:tagname
 ```


### Verbose Test
```
pytest -v
```
```
pytest -v -s
```
```output
tests/test_calculations.py::test_add testing add function
PASSED
```