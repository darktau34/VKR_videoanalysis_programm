import logging
import psycopg2 as ps
import pandas as pd
from psycopg2.extras import Json, DictCursor

logger = logging.getLogger(__name__)


def select_from_diagramm_table(person_id):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT diagramm_path " +
            "FROM diagramm " +
            f"WHERE person_id = {person_id}")

        row = cursor.fetchone()

        diagramm_path = row[0]

        connection.commit()

        cursor.close()
        connection.close()

        return diagramm_path


def check_diagramm_exists(person_id):
    value = False
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()
        cursor.execute(f"SELECT diagramm_id FROM diagramm WHERE person_id = '{person_id}'")
        if cursor.rowcount != 0:
            diagramm_id, = cursor.fetchone()
            logger.info("Diagramm of person id %s exists id DataBase", str(person_id))
            value = True
        else:
            logger.info("Diagramm of person id %s doesn't exists in DataBase", str(person_id))

        connection.commit()

        cursor.close()
        connection.close()

    return value


def insert_to_diagramm_table(person_id, diag_path):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()

        cursor.execute("INSERT INTO diagramm (person_id, diagramm_path) " +
                       "VALUES (%s, %s)",
                       [int(person_id), diag_path])

        connection.commit()

        cursor.close()
        connection.close()


def check_emotions_exists(person_id):
    value = False
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()
        cursor.execute(f"SELECT emotion_id FROM emotion WHERE person_id = '{person_id}'")
        if cursor.rowcount != 0:
            emotion_id, = cursor.fetchone()
            logger.info("Emotion of person id %s exists id DataBase", str(person_id))
            value = True
        else:
            logger.info("Emotion of person id %s doesn't exists in DataBase", str(person_id))

        connection.commit()

        cursor.close()
        connection.close()

    return value


def select_from_emotions_table(person_id):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor(cursor_factory=DictCursor)
        cursor.execute(
            "SELECT facebox, emotions_dict, top_emotion, is_recognized, need_warning " +
            "FROM emotion " +
            f"WHERE person_id = {person_id}")

        row = cursor.fetchone()

        facebox_path = row[0]
        emotions_dict = row[1]
        top_emotion = row[2]
        is_recognized = row[3]
        need_warning = row[4]

        connection.commit()

        cursor.close()
        connection.close()

        if is_recognized:
            return facebox_path, emotions_dict, top_emotion, need_warning
        else:
            return False


def insert_to_emotions_table(emotion_row):
    try:
        connection = ps.connect(dbname='passersby', host='127.0.0.1', port='5432', user='postgres', password='postgres')
    except ps.Error as e:
        logger.critical('Connection to DataBase is failed')
        logger.critical(e)
    else:
        cursor = connection.cursor()

        if emotion_row[4]:  # is recognized
            cursor.execute("INSERT INTO emotion (person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) " +
                           "VALUES (%s, %s, %s, %s, %s, %s)",
                           [int(emotion_row[0]), emotion_row[1], Json(emotion_row[2]), emotion_row[3], emotion_row[4], emotion_row[5]])
        else:
            cursor.execute("INSERT INTO emotion (person_id, is_recognized) " +
                           "VALUES (%s, %s)",
                           [int(emotion_row[0]), emotion_row[4]])

        connection.commit()

        cursor.close()
        connection.close()


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
                cursor.execute(f"DELETE FROM emotion WHERE person_id = {person_id[0]}")


        cursor.execute(f"DELETE FROM person WHERE video_id = {video_id}")
        cursor.execute(f"DELETE FROM video WHERE video_id = {video_id}")
        connection.commit()

        logger.info("Raws in DataBase with video_id = %s was deleted", str(video_id))

        cursor.close()
        connection.close()
