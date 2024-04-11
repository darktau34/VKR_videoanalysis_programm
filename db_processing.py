import logging
import psycopg2 as ps
import pandas as pd

logger = logging.getLogger(__name__)


def select_from_items(person_id):
    df_items = None
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        df_items = pd.DataFrame()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT item_name, confidence, item_photo " +
            "FROM item " +
            f"WHERE person_id = {person_id}")

        for item in cursor.fetchall():
            df_item_row = pd.DataFrame({
                'item_name': item[0],
                'confidence': int(item[1]),
                'item_photo': item[2]
            }, index=[0])
            df_items = pd.concat([df_items, df_item_row], ignore_index=True)

        connection.commit()

        cursor.close()
        connection.close()

    return df_items


def select_from_persons(video_id):
    df_persons = None
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        df_persons = pd.DataFrame()
        cursor = connection.cursor()
        cursor.execute(
            "SELECT person_id, tracker_id, photobox, appear_time, video_id, ui_tracker_id " +
            "FROM person " +
            f"WHERE video_id = {video_id}")

        for person in cursor.fetchall():
            df_person_row = pd.DataFrame({
                'person_id': int(person[0]),
                'tracker_id': int(person[1]),
                'photobox': person[2],
                'appear_time': person[3],
                'video_id': int(person[4]),
                'ui_tracker_id': int(person[5])
            }, index=[int(person[5])])
            df_persons = pd.concat([df_persons, df_person_row], ignore_index=True)

        df_persons.sort_values('ui_tracker_id', inplace=True)
        df_persons.reset_index(drop=True, inplace=True)

        connection.commit()

        cursor.close()
        connection.close()

    return df_persons


def insert_to_items_table(items_list, video_path):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()

        items = []

        # Выборка video_id
        cursor.execute(f"SELECT video_id FROM video WHERE video_path = '{video_path}'")
        if cursor.rowcount != 0:
            video_id, = cursor.fetchone()
            # Выборка person_id
            for item in items_list:
                cursor.execute(f"SELECT person_id FROM person WHERE video_id = {video_id} AND tracker_id = {item[0]}")
                if cursor.rowcount != 0:
                    person_id, = cursor.fetchone()
                    items.append((
                        person_id,
                        item[1],
                        item[2],
                        item[3]
                    ))

        cursor.executemany(
            "INSERT INTO item (person_id, item_name, confidence, item_photo)" +
            "VALUES (%s, %s, %s, %s)",
            items
        )

        connection.commit()

        cursor.close()
        connection.close()


def insert_to_video_table(video_path):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()
        cursor.execute(f"INSERT INTO video (video_path) VALUES ('{video_path}')")
        connection.commit()

        cursor.close()
        connection.close()


def insert_to_person_table(video_path, photoboxes_paths, time_list, tracker_list, ui_tracker_list):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()

        cursor.execute(f"SELECT video_id FROM video WHERE video_path = '{video_path}'")
        video_id, = cursor.fetchone()
        persons = []
        for i in range(len(photoboxes_paths)):
            persons.append((
                photoboxes_paths[i],
                time_list[i],
                video_id,
                int(tracker_list[i]),
                ui_tracker_list[i]
            ))

        cursor.executemany(
            "INSERT INTO person (" +
            "photobox, appear_time, video_id, tracker_id, ui_tracker_id" +
            ") " +
            "VALUES (%s, %s, %s, %s, %s)",
            persons
        )

        connection.commit()

        cursor.close()
        connection.close()

def check_items_exists(person_id):
    value = False
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()
        cursor.execute(f"SELECT item_id FROM item WHERE person_id = '{person_id}'")
        if cursor.rowcount != 0:
            video_id, = cursor.fetchone()
            logger.info("Items with person id %s exists id DataBase", str(person_id))
            value = True
        else:
            logger.info("Items with person id %s doesn't exists in DataBase", str(person_id))

        connection.commit()

        cursor.close()
        connection.close()

    return value

def check_video_db_exists_bypath(video_path):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        value = False
        cursor = connection.cursor()
        cursor.execute(f"SELECT video_id FROM video WHERE video_path = '{video_path}'")
        if cursor.rowcount != 0:
            video_id, = cursor.fetchone()
            logger.info("Video with path %s exists in DataBase with id:%s", video_path, str(video_id))
            value = video_id
        else:
            logger.info("Video with path %s doesn't exists in DataBase", video_path)

        connection.commit()

        cursor.close()
        connection.close()
        return value
    return None


def delete_rows_about_video(video_id):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()

        cursor.execute(f"SELECT person_id FROM person WHERE video_id = {video_id}")
        if cursor.rowcount != 0:
            for person_id in cursor.fetchall():
                cursor.execute(f"DELETE FROM item WHERE person_id = {person_id[0]}")

        cursor.execute(f"DELETE FROM person WHERE video_id = {video_id}")
        cursor.execute(f"DELETE FROM video WHERE video_id = {video_id}")
        connection.commit()

        logger.info("Raws in DataBase with video_id = %s was deleted", str(video_id))

        cursor.close()
        connection.close()
