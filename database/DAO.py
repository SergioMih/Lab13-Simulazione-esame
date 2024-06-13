from database.DB_connect import DBConnect
from model.state import State


class DAO():
    def __init__(self):
        pass

    @staticmethod
    def getShapes(anno):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT DISTINCT s.shape 
FROM sighting s 
where YEAR(s.`datetime`) = %s"""

        cursor.execute(query, (anno,))

        for row in cursor:
            result.append(row["shape"])

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getStates():
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT *
from state s """

        cursor.execute(query)

        for row in cursor:
            result.append(State(**row))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(idMap):
        conn = DBConnect.get_connection()

        result = []

        cursor = conn.cursor(dictionary=True)
        query = """SELECT state1,state2
from neighbor n 
where state1 < state2 """

        cursor.execute(query)

        for row in cursor:
            result.append((idMap[row["state1"]],idMap[row["state2"]]))

        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getWeight(s1,s2,anno,shape):
        conn = DBConnect.get_connection()

        result = 0

        cursor = conn.cursor(dictionary=True)
        query = """SELECT count(*) as num
from sighting s
where (s.state = %s or s.state = %s)
and YEAR(s.`datetime`) = %s
and s.shape = %s  """

        cursor.execute(query,(s1,s2,anno,shape))

        for row in cursor:
            result= row["num"]

        cursor.close()
        conn.close()
        return result