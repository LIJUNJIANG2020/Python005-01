# SQLAlchemy

> 

## 连接MySQL

> sqlalchemy core 方式

```python
import pymysql
from sqlalchemy import create_engine, Table, Column, Integer, String, ForeignKey, MetaData

# echo=True  开启调试
engine = create_engine('mysql+pymysql://devops:qwe123456@node1:3306/db1', echo=True)
# print(engine) # Out: Engine(mysql+pymysql://devops:***@node1:3306/db1)
```

> sqlalchemy ORM方式

```

```

