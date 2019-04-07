import MySQLdb

#*******************************************************************************
def check_pilot(in_ed_name):

#    cnx = mysql.connector.connect(user='uca', password='7014258',
#                                  host='127.0.0.1',
#                                  database='uca')

    cnx = MySQLdb.connect(user='uca', password='7014258',
                                  host='127.0.0.1',
                                  database='uca')
                                  
    cursor = cnx.cursor()
    query = """select count(1) from discord_registers where ed_name = %(ed_name)s and user_id is null"""
    
    cursor.execute(query, {'ed_name': in_ed_name})

    for(count) in cursor:
       print(count[0])

    cursor.close()
    cnx.close()
    
    return count[0]

#*******************************************************************************
def check_discord_id(in_discord_id):
    cnx = MySQLdb.connect(user='uca', password='7014258',
                                  host='127.0.0.1',
                                  database='uca')
#    cnx = mysql.connector.connect(user='uca', password='7014258',
#                                  host='127.0.0.1',
#                                  database='uca')
                                  
    cursor = cnx.cursor()
    query = """select count(1) from discord_registers where discord_id = %(discord_id)s"""
    
    cursor.execute(query, {'discord_id': in_discord_id})

    for(count) in cursor:
       print(count[0])

    cursor.close()
    cnx.close()
    
    return count[0]

#*******************************************************************************
def get_uid_by_pilot(in_ed_name):
    cnx = MySQLdb.connect(user='uca', password='7014258',
                                  host='127.0.0.1',
                                  database='uca')
#    cnx = mysql.connector.connect(user='uca', password='7014258',
#                                  host='127.0.0.1',
#                                  database='uca')
                                  
    cursor = cnx.cursor()
    query = """select registry_uid from discord_registers where ed_name = %(ed_name)s limit 1"""
    
    cursor.execute(query, {'ed_name': in_ed_name})

    for(registry_uid) in cursor:
       print(registry_uid[0])

    cursor.close()
    cnx.close()
    
    return registry_uid[0]

#*******************************************************************************
def registry_pilot(in_ed_name, in_discord_id, in_uid):
    cnx = MySQLdb.connect(user='uca', password='7014258',
                                  host='127.0.0.1',
                                  database='uca')
#    cnx = mysql.connector.connect(user='uca', password='7014258',
#                                  host='127.0.0.1',
#                                  database='uca')
                                  
    cursor = cnx.cursor()
    
    add_user = ("INSERT INTO discord_registers "
                  "(ed_name, discord_id, registry_uid) "
                  "VALUES (%(ed_name)s, %(discord_id)s, %(registry_uid)s)")
                  
    data_user = {
      'ed_name': in_ed_name,
      'discord_id': in_discord_id,
      'registry_uid': in_uid,
    }
    
    cursor.execute(add_user, data_user)
    
    cnx.commit()
    
    cursor.close()
    cnx.close()
    