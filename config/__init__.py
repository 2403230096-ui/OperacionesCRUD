try:
    import pymysql
    pymysql.install_as_MySQLdb()
except ImportError:  # solo necesario al usar MySQL
    pass
