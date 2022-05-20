import mysql.connector


def execute_select_query(current_query):
    cursor.execute(mySql_select_query)
    record = cursor.fetchall()
    print('\n'.join(str(r) for r in record))


try:
    connection = mysql.connector.connect(host='localhost',
                                         user="root",
                                         passwd="051024",
                                         database="football_db")

    cursor = connection.cursor()

    # TASK 1
    # For players with age over 45 (inclusive)
    # insert records of data into the coaches table, based on the players table.

    mySql_insert_into_coaches_query = """INSERT INTO coaches (first_name, last_name, salary, coach_level)
                                        SELECT first_name, last_name, salary, char_length(first_name)
                                        FROM players
                                        WHERE age >= 45"""

    cursor.execute(mySql_insert_into_coaches_query)
    connection.commit()
    print(cursor.rowcount, "Records inserted successfully into table coaches!")

    # TASK 2
    # Update all coaches, who train one or more players and their first_name starts with ‘A’.
    # Increase their level with 1.

    print("Before updating a record ")
    mySql_select_query = """SELECT * FROM coaches AS c
                            WHERE c.first_name LIKE 'A%' AND c.id IN (SELECT coach_id FROM players_coaches)"""

    execute_select_query(mySql_select_query)

    # Update
    # do it with subquery
    mySql_update_query = """UPDATE coaches AS c
                            SET coach_level = coach_level + 1
                            WHERE c.first_name LIKE 'A%' AND c.id IN (SELECT coach_id FROM players_coaches)"""
    cursor.execute(mySql_update_query)
    connection.commit()
    print("Record Updated successfully!")

    # can do it with JOIN :

    # """UPDATE coaches AS c
    #     JOIN players_coaches AS pc
    #     ON pc.coach_id = c.id
    #     SET coach_level = coach_level + 1
    #     WHERE c.first_name LIKE 'A%'"""

    print("After updating record ")
    execute_select_query(mySql_select_query)

    # TASK 3
    # Delete all players from table players,
    # which are already added in table coaches from TASK 1

    mySql_delete_query = """DELETE FROM players
                            WHERE age >= 45"""
    cursor.execute(mySql_delete_query)
    connection.commit()
    print('number of rows deleted', cursor.rowcount)

    # TASK 4
    # Extract first_name, age, salary info about all the players.
    # Order the results by players` salary descending.

    mySql_select_query = """SELECT first_name, age, salary
                            FROM players
                            ORDER BY salary DESC"""

    print("Select query result:")
    execute_select_query(mySql_select_query)

    # TASK 5
    # One of the coaches wants to know more about all the young players (under age of 23) who can strengthen
    # his team in the offensive (played on position ‘A’). As he is not paying a transfer amount, he is looking only
    # for those who have not signed a contract so far (haven’t hire_date) and have strength of more than 50. Order
    # the results ascending by salary, then by age.

    mySql_select_query = """SELECT
                            p.`id`,
                            concat(p.first_name, ' ', p.last_name) AS `full_name`,
                            p.`age`,
                            p.`position`,
                            p.`hire_date`
                            FROM players AS p
                            JOIN skills_data AS sk
                            ON p.skills_data_id = sk.id
                            WHERE p.`age` < 23 AND p.`position` = 'A' AND  p.`hire_date` IS NULL AND sk.strength > 50
                            ORDER BY p.salary, p.age"""

    print("Select query result:")
    execute_select_query(mySql_select_query)

    # TASK 6
    # Extract from the database all the teams and the count of the players that they have.
    # Order the results descending by count of players, then by fan_base descending.

    mySql_select_query = """SELECT
                            t.`name` AS `team_name`,
                            t.established,
                            t.fan_base,
                            COUNT(p.id) AS `players_count`
                            FROM teams AS t
                            LEFT JOIN players AS p
                            ON t.id = p.team_id
                            GROUP BY t.id
                            ORDER BY COUNT(p.id) DESC, t.fan_base DESC"""

    print("Select query result:")
    execute_select_query(mySql_select_query)

    # TASK 7
    # Extract from the database, the fastest player (having max speed),
    # in terms of towns where their team played.
    # Order players by speed descending, then by town name.
    # Skip players that played in team `Devify`

    mySql_select_query = """SELECT MAX(sk.speed) AS `max_speed`, towns.`name` AS `town_name`
                            FROM players AS p
                            RIGHT JOIN skills_data AS sk
                            ON p.skills_data_id = sk.id
                            RIGHT JOIN teams AS t
                            ON p.team_id = t.id
                            RIGHT JOIN stadiums AS s
                            ON t.stadium_id = s.id
                            RIGHT JOIN towns
                            ON s.town_id = towns.id
                            WHERE t.`name` != 'Devify'
                            GROUP BY towns.`name`
                            ORDER BY MAX(sk.speed) DESC, towns.`name`"""

    print("Select query result:")
    execute_select_query(mySql_select_query)

    # TASK 8
    # Now you need to extract detailed information
    # on the amount of all salaries given to football players
    # by the criteria of the country in which they played.
    # If there are no players in a country, display NULL.
    #  Order the results by total count of players in descending order,
    # then by country name alphabetically.

    mySql_select_query = """SELECT
                                c.`name`,
                                COUNT(p.id) AS `total_count_of_players`,
                                SUM(p.salary) AS `total_sum_of_salaries`
                            FROM players AS p
                            RIGHT JOIN skills_data AS sk
                            ON p.skills_data_id = sk.id
                            RIGHT JOIN teams AS t
                            ON p.team_id = t.id
                            RIGHT JOIN stadiums AS s
                            ON t.stadium_id = s.id
                            RIGHT JOIN towns
                            ON s.town_id = towns.id
                            RIGHT JOIN countries AS c
                            ON towns.country_id = c.id
                            GROUP BY c.id
                            ORDER BY COUNT(p.id) DESC, c.`name`"""

    print("Select query result:")
    execute_select_query(mySql_select_query)

    cursor.close()

except mysql.connector.Error as error:
    print(f"Failed: {error}")

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
