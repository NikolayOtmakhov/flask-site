def birthday_data(sql_login, running_local):

    if running_local == False:

        import mysql.connector as mysql

        db = mysql.connect(
        host = sql_login.host,
        user = sql_login.user,
        passwd = sql_login.passwd,
        database = sql_login.database)

        cursor = db.cursor()

        cursor.execute("SELECT \
            name,  \
            /*Days Till Bday*/ IF(DATEDIFF(DATE(CONCAT(YEAR(CURDATE()), RIGHT(birth, 6))), CURDATE())>0, \
                                DATEDIFF(DATE(CONCAT(YEAR(CURDATE()), RIGHT(birth, 6))), CURDATE()), \
                                DATEDIFF(DATE(CONCAT(YEAR(CURDATE())+1, RIGHT(birth, 6))), CURDATE())), \
            /*Years Old*/ TIMESTAMPDIFF(YEAR, birth, CURDATE()) \
            FROM friends \
            ORDER BY \
            /*Days Till Bday*/ IF(DATEDIFF(DATE(CONCAT(YEAR(CURDATE()), RIGHT(birth, 6))), CURDATE())>0, \
                                DATEDIFF(DATE(CONCAT(YEAR(CURDATE()), RIGHT(birth, 6))), CURDATE()), \
                                DATEDIFF(DATE(CONCAT(YEAR(CURDATE())+1, RIGHT(birth, 6))), CURDATE()))")

        return cursor.fetchall()
    else:
        return [["Cant connect to sql server from local host","-","-"]]