import mysql.connector

# TASK
# Create a stored procedure udp_find_playmaker which accepts the following parameters:
# •	min_dribble_points
# •	team_name (with max length 45)
# And extracts data about the players with the given skill stats (more than
# min_dribble_points), played for given team (team_name) and have more than average speed for all players. Order
# players by speed descending. Select only the best one. Show all needed info for this player: full_name, age,
# salary, dribbling, speed, team name.

try:
    connection = mysql.connector.connect(host='localhost',
                                         user="root",
                                         passwd="051024",
                                         database="football_db")
    cursor = connection.cursor()

    # create
    mySql_create_procedure_query = """CREATE PROCEDURE udp_find_playmaker (min_dribble_points INT, team_name VARCHAR(45))
                                        BEGIN
                                        SELECT
                                            concat(p.first_name, ' ', p.last_name) AS `full_name`,
                                            p.age,
                                            p.salary,
                                            sd.dribbling,
                                            sd.speed,
                                            t.name
                                        FROM players AS p
                                        JOIN skills_data AS sd
                                        ON p.skills_data_id = sd.id
                                        JOIN teams AS t
                                        ON p.team_id = t.id
                                        WHERE sd.dribbling > min_dribble_points
                                            AND t.`name` = team_name
                                            AND sd.speed > (SELECT AVG(speed)
                                            FROM skills_data)
                                        ORDER BY sd.speed DESC
                                        LIMIT 1;
                                        END"""

    cursor.execute(mySql_create_procedure_query)
    connection.commit()
    print("Procedure created successfully!")

    # execute
    cursor.callproc('udp_find_playmaker', (20, 'Skyble'))
    result = cursor.fetchall()

    for result in cursor.stored_results():
        print(result.fetchall())


except mysql.connector.Error as error:
    print(f"Failed to execute procedure: {error}")
finally:
    if (connection.is_connected()):
        cursor.close()
        connection.close()
        print("MySQL connection is closed")