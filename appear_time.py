import logging
import pandas as pd

logger = logging.getLogger(__name__)


class EntryTime:
    """
    This class is designed to calculate the time of object appears in the video
    based on the time at the beginning of the video
    """
    def __init__(self, hh_mm_ss, fps, tracker_id, dataframe):
        """
        Create a new instance of EntryTime class
        :param hh_mm_ss: time in string format hh:mm:ss
        :param fps: fps on the video
        :param tracker_id: object id on the video
        :param dataframe: created by yolo dataframe
        """
        self._hours = int(hh_mm_ss.split(':')[0])
        self._minutes = int(hh_mm_ss.split(':')[1])
        self._seconds = int(hh_mm_ss.split(':')[2])
        self._fps = fps
        self._tracker_id = tracker_id
        self._df = dataframe
        self._first_frame = None

    def get_entry_time(self):
        """
        Main function, include calculate_first_time(),
        calculate_time(), __format_to_time()
        :return: formatted string entry_time hh:mm:ss
        """
        self.calculate_first_frame()
        self.calculate_time()
        entry_time = self.__format_to_time()
        return entry_time

    def __format_to_time(self):
        """
        Formats the time attributes self._hours, self._minutes, self._seconds
        in hh:mm:ss format
        :return: hh:mm:ss string
        """
        if self._hours // 10 == 0:
            format_hours = '0' + str(self._hours)
        else:
            format_hours = str(self._hours)

        if self._minutes // 10 == 0:
            format_minutes = '0' + str(self._minutes)
        else:
            format_minutes = str(self._minutes)

        if self._seconds // 10 == 0:
            format_seconds = '0' + str(self._seconds)
        else:
            format_seconds = str(self._seconds)

        result_string = format_hours + ':' + format_minutes + ':' + format_seconds
        return result_string

    def calculate_first_frame(self):
        """
        Function for calculating the number of the first frame from
        the video, on which the object with the given id appears
        """
        df_id = self._df.loc[self._df.tracker_id == self._tracker_id]
        df_id.reset_index(drop=True, inplace=True)
        self._first_frame = int(df_id.iloc[0]['frame'])

    def calculate_time(self):
        """
        Function to calculate the seconds from the beginning of the video
        to the first frame calculated by calculate_firts_frame()
        """
        seconds_to_first_frame = int(self._first_frame / self._fps)
        self.update_time(seconds_to_first_frame)

    def update_time(self, seconds):
        """
        Function for updating the time
        :param seconds: int seconds
        """
        self._seconds += seconds
        sec_to_min = self._seconds // 60
        if sec_to_min != 0:
            self._seconds -= sec_to_min * 60
            self._minutes += sec_to_min
            min_to_hours = self._minutes // 60
            if min_to_hours != 0:
                self._minutes -= min_to_hours * 60
                self._hours += min_to_hours
                if self._hours >= 24:
                    self._hours = 0


def calculate_appear_time(df, begin_video_time, fps, person_list):
    time_df = pd.DataFrame(columns=['tracker_id', 'appear_time'])
    time_df['tracker_id'] = person_list

    for person in person_list:
        entry_time = EntryTime(begin_video_time, fps, person, df)
        person_appear_time = entry_time.get_entry_time()
        del entry_time
        time_df.loc[time_df['tracker_id'] == person, 'appear_time'] = person_appear_time

    logger.info('Appear times has been calculated')
    return time_df
