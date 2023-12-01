SELECT person.person_id, person.photobox, person.appear_time, person.videoclip_begin,
person.videoclip_middle, person.videoclip_end,
video.video_path, item.item_name, item.confidence, item.item_photo
FROM person
INNER JOIN video ON person.video_id = video.video_id
LEFT JOIN item ON item.person_id = person.person_id
