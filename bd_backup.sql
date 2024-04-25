--
-- PostgreSQL database dump
--

-- Dumped from database version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)
-- Dumped by pg_dump version 14.11 (Ubuntu 14.11-0ubuntu0.22.04.1)

-- Started on 2024-04-25 21:10:07 MSK

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 218 (class 1259 OID 16552)
-- Name: diagramm; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.diagramm (
    diagramm_id integer NOT NULL,
    person_id integer NOT NULL,
    diagramm_path character varying(255) NOT NULL
);


ALTER TABLE public.diagramm OWNER TO postgres;

--
-- TOC entry 217 (class 1259 OID 16551)
-- Name: diagramm_diagramm_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.diagramm ALTER COLUMN diagramm_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.diagramm_diagramm_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 215 (class 1259 OID 16538)
-- Name: emotion; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.emotion (
    emotion_id integer NOT NULL,
    person_id integer NOT NULL,
    facebox character varying(255),
    emotions_dict jsonb,
    top_emotion character varying(32),
    is_recognized boolean NOT NULL,
    need_warning boolean
);


ALTER TABLE public.emotion OWNER TO postgres;

--
-- TOC entry 216 (class 1259 OID 16550)
-- Name: emotion_emotion_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.emotion ALTER COLUMN emotion_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.emotion_emotion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 211 (class 1259 OID 16514)
-- Name: item; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.item (
    item_id integer NOT NULL,
    person_id integer NOT NULL,
    item_name character varying(32) NOT NULL,
    confidence integer NOT NULL,
    item_photo character varying(255) NOT NULL
);


ALTER TABLE public.item OWNER TO postgres;

--
-- TOC entry 214 (class 1259 OID 16536)
-- Name: item_item_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.item ALTER COLUMN item_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.item_item_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 210 (class 1259 OID 16502)
-- Name: person; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.person (
    person_id integer NOT NULL,
    photobox character varying(255) NOT NULL,
    appear_time character varying(32) NOT NULL,
    video_id integer NOT NULL,
    tracker_id integer NOT NULL,
    ui_tracker_id integer NOT NULL
);


ALTER TABLE public.person OWNER TO postgres;

--
-- TOC entry 213 (class 1259 OID 16530)
-- Name: person_person_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.person ALTER COLUMN person_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.person_person_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 222 (class 1259 OID 16576)
-- Name: target; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.target (
    target_id integer NOT NULL,
    video_id integer NOT NULL,
    target_items_path character varying(255) NOT NULL,
    target_emotions_path character varying(255) NOT NULL
);


ALTER TABLE public.target OWNER TO postgres;

--
-- TOC entry 221 (class 1259 OID 16575)
-- Name: target_analyze_target_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.target ALTER COLUMN target_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.target_analyze_target_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 209 (class 1259 OID 16482)
-- Name: video; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.video (
    video_id integer NOT NULL,
    video_path character varying(255) NOT NULL,
    data_path character varying(255) NOT NULL
);


ALTER TABLE public.video OWNER TO postgres;

--
-- TOC entry 212 (class 1259 OID 16524)
-- Name: video_video_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.video ALTER COLUMN video_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.video_video_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 220 (class 1259 OID 16563)
-- Name: videoclip; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.videoclip (
    videoclip_id integer NOT NULL,
    person_id integer NOT NULL,
    videoclip_path character varying(255) NOT NULL
);


ALTER TABLE public.videoclip OWNER TO postgres;

--
-- TOC entry 219 (class 1259 OID 16562)
-- Name: videoclip_videoclip_id_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public.videoclip ALTER COLUMN videoclip_id ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public.videoclip_videoclip_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- TOC entry 3405 (class 0 OID 16552)
-- Dependencies: 218
-- Data for Name: diagramm; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (11, 957, 'data/mall/diagramms/2-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (12, 958, 'data/mall/diagramms/3-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (13, 959, 'data/mall/diagramms/4-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (14, 962, 'data/mall/diagramms/11-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (15, 965, 'data/mall/diagramms/18-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (16, 981, 'data/mall/diagramms/52-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (18, 1038, 'data/aquarel/diagramms/16-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (20, 1081, 'data/aquarel_2/diagramms/21-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (24, 1278, 'data/thailand_35sec_4/diagramms/1-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (25, 1320, 'data/50sec/diagramms/1-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (26, 1548, 'data/thailand30sec_2/diagramms/4-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (41, 1683, 'data/1min10sec/diagramms/1-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (42, 1687, 'data/1min10sec/diagramms/8-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (43, 1688, 'data/1min10sec/diagramms/9-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (44, 1691, 'data/1min10sec/diagramms/33-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (45, 1685, 'data/1min10sec/diagramms/3-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (46, 1684, 'data/1min10sec/diagramms/2-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (47, 1690, 'data/1min10sec/diagramms/14-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (48, 1692, 'data/1min10sec/diagramms/43-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (49, 1693, 'data/1min10sec/diagramms/47-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (50, 1694, 'data/1min10sec/diagramms/50-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (51, 1695, 'data/1min10sec/diagramms/51-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (52, 1700, 'data/1min10sec/diagramms/58-diag_emotions.png');
INSERT INTO public.diagramm (diagramm_id, person_id, diagramm_path) OVERRIDING SYSTEM VALUE VALUES (53, 1697, 'data/1min10sec/diagramms/54-diag_emotions.png');


--
-- TOC entry 3402 (class 0 OID 16538)
-- Dependencies: 215
-- Data for Name: emotion; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (63, 957, 'data/mall/emotions/facebox_person2.png', '{"sad": 0.17, "fear": 0.19, "angry": 0.3, "happy": 0.05, "disgust": 0.0, "neutral": 0.21, "surprise": 0.08}', 'angry', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (64, 958, 'data/mall/emotions/facebox_person3.png', '{"sad": 0.7, "fear": 0.11, "angry": 0.06, "happy": 0.0, "disgust": 0.0, "neutral": 0.11, "surprise": 0.01}', 'sad', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (65, 959, 'data/mall/emotions/facebox_person4.png', '{"sad": 0.24, "fear": 0.11, "angry": 0.07, "happy": 0.04, "disgust": 0.0, "neutral": 0.5, "surprise": 0.04}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (66, 960, 'data/mall/emotions/facebox_person8.png', '{"sad": 0.58, "fear": 0.02, "angry": 0.1, "happy": 0.17, "disgust": 0.01, "neutral": 0.12, "surprise": 0.01}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (67, 961, 'data/mall/emotions/facebox_person9.png', '{"sad": 0.28, "fear": 0.17, "angry": 0.07, "happy": 0.06, "disgust": 0.0, "neutral": 0.32, "surprise": 0.09}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (68, 962, 'data/mall/emotions/facebox_person11.png', '{"sad": 0.16, "fear": 0.06, "angry": 0.07, "happy": 0.34, "disgust": 0.0, "neutral": 0.34, "surprise": 0.03}', 'happy', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (69, 965, 'data/mall/emotions/facebox_person18.png', '{"sad": 0.07, "fear": 0.06, "angry": 0.13, "happy": 0.7, "disgust": 0.0, "neutral": 0.02, "surprise": 0.03}', 'happy', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (70, 981, 'data/mall/emotions/facebox_person52.png', '{"sad": 0.41, "fear": 0.29, "angry": 0.04, "happy": 0.01, "disgust": 0.0, "neutral": 0.22, "surprise": 0.03}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (75, 1038, 'data/aquarel/emotions/facebox_person16.png', '{"sad": 0.08, "fear": 0.01, "angry": 0.12, "happy": 0.77, "disgust": 0.0, "neutral": 0.03, "surprise": 0.0}', 'happy', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (78, 1081, 'data/aquarel_2/emotions/facebox_person21.png', '{"sad": 0.19, "fear": 0.19, "angry": 0.21, "happy": 0.17, "disgust": 0.0, "neutral": 0.23, "surprise": 0.0}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (79, 1086, 'data/aquarel_2/emotions/facebox_person31.png', '{"sad": 0.11, "fear": 0.02, "angry": 0.13, "happy": 0.23, "disgust": 0.0, "neutral": 0.48, "surprise": 0.02}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (80, 1085, 'data/aquarel_2/emotions/facebox_person30.png', '{"sad": 0.25, "fear": 0.02, "angry": 0.11, "happy": 0.34, "disgust": 0.0, "neutral": 0.28, "surprise": 0.0}', 'happy', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (81, 1083, 'data/aquarel_2/emotions/facebox_person28.png', '{"sad": 0.08, "fear": 0.06, "angry": 0.22, "happy": 0.02, "disgust": 0.0, "neutral": 0.6, "surprise": 0.01}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (82, 1080, 'data/aquarel_2/emotions/facebox_person19.png', '{"sad": 0.26, "fear": 0.19, "angry": 0.1, "happy": 0.0, "disgust": 0.0, "neutral": 0.45, "surprise": 0.0}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (83, 1075, 'data/aquarel_2/emotions/facebox_person4.png', '{"sad": 0.47, "fear": 0.17, "angry": 0.11, "happy": 0.03, "disgust": 0.0, "neutral": 0.2, "surprise": 0.02}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (84, 1084, 'data/aquarel_2/emotions/facebox_person29.png', '{"sad": 0.43, "fear": 0.41, "angry": 0.04, "happy": 0.03, "disgust": 0.0, "neutral": 0.08, "surprise": 0.0}', 'sad', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (85, 1082, 'data/aquarel_2/emotions/facebox_person26.png', '{"sad": 0.18, "fear": 0.45, "angry": 0.26, "happy": 0.05, "disgust": 0.01, "neutral": 0.04, "surprise": 0.01}', 'fear', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (86, 1073, NULL, NULL, NULL, false, NULL);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (87, 1117, NULL, NULL, NULL, false, NULL);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (88, 1217, 'data/street_25sec_1/emotions/facebox_person1.png', '{"sad": 0.3, "fear": 0.06, "angry": 0.34, "happy": 0.02, "disgust": 0.0, "neutral": 0.27, "surprise": 0.0}', 'angry', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (89, 1218, 'data/street_25sec_1/emotions/facebox_person2.png', '{"sad": 0.46, "fear": 0.16, "angry": 0.05, "happy": 0.09, "disgust": 0.0, "neutral": 0.23, "surprise": 0.02}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (90, 1307, 'data/thailand_35sec_4/emotions/facebox_person75.png', '{"sad": 0.12, "fear": 0.04, "angry": 0.06, "happy": 0.69, "disgust": 0.0, "neutral": 0.09, "surprise": 0.0}', 'happy', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (91, 1344, 'data/thailand30sec_3/emotions/facebox_person1.png', '{"sad": 0.12, "fear": 0.02, "angry": 0.85, "happy": 0.0, "disgust": 0.0, "neutral": 0.01, "surprise": 0.0}', 'angry', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (92, 1345, 'data/thailand30sec_3/emotions/facebox_person2.png', '{"sad": 0.32, "fear": 0.38, "angry": 0.11, "happy": 0.08, "disgust": 0.0, "neutral": 0.1, "surprise": 0.01}', 'fear', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (93, 1360, 'data/thailand30sec_3/emotions/facebox_person21.png', '{"sad": 0.23, "fear": 0.29, "angry": 0.35, "happy": 0.03, "disgust": 0.0, "neutral": 0.1, "surprise": 0.01}', 'angry', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (94, 1361, 'data/thailand30sec_3/emotions/facebox_person23.png', '{"sad": 0.63, "fear": 0.16, "angry": 0.12, "happy": 0.02, "disgust": 0.0, "neutral": 0.06, "surprise": 0.0}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (106, 1121, NULL, NULL, NULL, false, NULL);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (110, 1548, 'data/thailand30sec_2/emotions/facebox_person4.png', '{"sad": 0.39, "fear": 0.08, "angry": 0.11, "happy": 0.3, "disgust": 0.0, "neutral": 0.09, "surprise": 0.02}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (111, 963, 'data/mall/emotions/facebox_person16.png', '{"sad": 0.43, "fear": 0.21, "angry": 0.08, "happy": 0.03, "disgust": 0.0, "neutral": 0.21, "surprise": 0.03}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (112, 964, 'data/mall/emotions/facebox_person17.png', '{"sad": 0.63, "fear": 0.02, "angry": 0.05, "happy": 0.12, "disgust": 0.01, "neutral": 0.16, "surprise": 0.0}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (113, 967, NULL, NULL, NULL, false, NULL);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (114, 968, NULL, NULL, NULL, false, NULL);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (115, 970, 'data/mall/emotions/facebox_person32.png', '{"sad": 0.48, "fear": 0.05, "angry": 0.05, "happy": 0.21, "disgust": 0.01, "neutral": 0.19, "surprise": 0.02}', 'sad', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (123, 1655, 'data/tokyo1/emotions/facebox_person2.png', '{"sad": 0.14000000059604645, "fear": 0.18000000715255737, "angry": 0.029999999329447746, "happy": 0.07999999821186066, "disgust": 0.0, "neutral": 0.47999998927116394, "contempt": 0.03999999910593033, "surprise": 0.05000000074505806}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (124, 1656, NULL, NULL, NULL, false, NULL);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (125, 1657, 'data/tokyo1/emotions/facebox_person4.png', '{"sad": 0.5799999833106995, "fear": 0.10000000149011612, "angry": 0.019999999552965164, "happy": 0.03999999910593033, "disgust": 0.009999999776482582, "neutral": 0.20000000298023224, "contempt": 0.019999999552965164, "surprise": 0.029999999329447746}', 'sad', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (126, 1658, 'data/tokyo1/emotions/facebox_person5.png', '{"sad": 0.05999999865889549, "fear": 0.009999999776482582, "angry": 0.05999999865889549, "happy": 0.1899999976158142, "disgust": 0.019999999552965164, "neutral": 0.6200000047683716, "contempt": 0.03999999910593033, "surprise": 0.009999999776482582}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (127, 1660, 'data/tokyo1/emotions/facebox_person7.png', '{"sad": 0.07999999821186066, "fear": 0.009999999776482582, "angry": 0.11999999731779099, "happy": 0.14000000059604645, "disgust": 0.0, "neutral": 0.6100000143051147, "contempt": 0.03999999910593033, "surprise": 0.0}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (128, 1661, 'data/tokyo1/emotions/facebox_person8.png', '{"sad": 0.09000000357627869, "fear": 0.0, "angry": 0.009999999776482582, "happy": 0.5199999809265137, "disgust": 0.0, "neutral": 0.3700000047683716, "contempt": 0.009999999776482582, "surprise": 0.0}', 'happy', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (129, 1662, 'data/tokyo1/emotions/facebox_person10.png', '{"sad": 0.47999998927116394, "fear": 0.019999999552965164, "angry": 0.10000000149011612, "happy": 0.029999999329447746, "disgust": 0.029999999329447746, "neutral": 0.3100000023841858, "contempt": 0.009999999776482582, "surprise": 0.029999999329447746}', 'sad', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (130, 1663, 'data/tokyo1/emotions/facebox_person11.png', '{"sad": 0.03999999910593033, "fear": 0.07000000029802322, "angry": 0.6399999856948853, "happy": 0.009999999776482582, "disgust": 0.029999999329447746, "neutral": 0.11999999731779099, "contempt": 0.009999999776482582, "surprise": 0.07999999821186066}', 'angry', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (131, 1664, 'data/tokyo1/emotions/facebox_person12.png', '{"sad": 0.05000000074505806, "fear": 0.009999999776482582, "angry": 0.15000000596046448, "happy": 0.18000000715255737, "disgust": 0.029999999329447746, "neutral": 0.5299999713897705, "contempt": 0.03999999910593033, "surprise": 0.009999999776482582}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (132, 1666, 'data/tokyo1/emotions/facebox_person16.png', '{"sad": 0.10000000149011612, "fear": 0.009999999776482582, "angry": 0.05000000074505806, "happy": 0.20999999344348907, "disgust": 0.029999999329447746, "neutral": 0.5299999713897705, "contempt": 0.05999999865889549, "surprise": 0.009999999776482582}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (133, 1668, 'data/tokyo1/emotions/facebox_person18.png', '{"sad": 0.18000000715255737, "fear": 0.05000000074505806, "angry": 0.36000001430511475, "happy": 0.029999999329447746, "disgust": 0.07999999821186066, "neutral": 0.20999999344348907, "contempt": 0.05000000074505806, "surprise": 0.03999999910593033}', 'angry', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (134, 1669, 'data/tokyo1/emotions/facebox_person27.png', '{"sad": 0.44999998807907104, "fear": 0.019999999552965164, "angry": 0.15000000596046448, "happy": 0.009999999776482582, "disgust": 0.07000000029802322, "neutral": 0.28999999165534973, "contempt": 0.0, "surprise": 0.009999999776482582}', 'sad', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (135, 1671, 'data/tokyo1/emotions/facebox_person31.png', '{"sad": 0.20000000298023224, "fear": 0.029999999329447746, "angry": 0.14000000059604645, "happy": 0.029999999329447746, "disgust": 0.07000000029802322, "neutral": 0.5, "contempt": 0.009999999776482582, "surprise": 0.019999999552965164}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (136, 1673, 'data/tokyo1/emotions/facebox_person34.png', '{"sad": 0.05999999865889549, "fear": 0.10000000149011612, "angry": 0.12999999523162842, "happy": 0.18000000715255737, "disgust": 0.029999999329447746, "neutral": 0.3100000023841858, "contempt": 0.07999999821186066, "surprise": 0.10999999940395355}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (137, 1676, 'data/tokyo1/emotions/facebox_person44.png', '{"sad": 0.11999999731779099, "fear": 0.07000000029802322, "angry": 0.25999999046325684, "happy": 0.029999999329447746, "disgust": 0.1599999964237213, "neutral": 0.30000001192092896, "contempt": 0.019999999552965164, "surprise": 0.03999999910593033}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (138, 1678, NULL, NULL, NULL, false, NULL);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (139, 1681, 'data/tokyo1/emotions/facebox_person51.png', '{"sad": 0.15000000596046448, "fear": 0.07000000029802322, "angry": 0.10000000149011612, "happy": 0.03999999910593033, "disgust": 0.009999999776482582, "neutral": 0.5699999928474426, "contempt": 0.019999999552965164, "surprise": 0.03999999910593033}', 'neutral', true, false);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (140, 1682, 'data/tokyo1/emotions/facebox_person58.png', '{"sad": 0.05000000074505806, "fear": 0.14000000059604645, "angry": 0.09000000357627869, "happy": 0.27000001072883606, "disgust": 0.029999999329447746, "neutral": 0.25, "contempt": 0.03999999910593033, "surprise": 0.12999999523162842}', 'happy', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (155, 1692, 'data/1min10sec/emotions/facebox_person43.png', '{"sad": 0.07999999821186066, "fear": 0.029999999329447746, "angry": 0.23000000417232513, "happy": 0.20000000298023224, "disgust": 0.09000000357627869, "neutral": 0.2199999988079071, "contempt": 0.05999999865889549, "surprise": 0.10000000149011612}', 'angry', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (156, 1700, 'data/1min10sec/emotions/facebox_person58.png', '{"sad": 0.15000000596046448, "fear": 0.0, "angry": 0.10999999940395355, "happy": 0.44999998807907104, "disgust": 0.03999999910593033, "neutral": 0.1899999976158142, "contempt": 0.05000000074505806, "surprise": 0.0}', 'happy', true, true);
INSERT INTO public.emotion (emotion_id, person_id, facebox, emotions_dict, top_emotion, is_recognized, need_warning) OVERRIDING SYSTEM VALUE VALUES (157, 1712, 'data/27sec/emotions/facebox_person8.png', '{"sad": 0.05999999865889549, "fear": 0.019999999552965164, "angry": 0.05999999865889549, "happy": 0.20999999344348907, "disgust": 0.009999999776482582, "neutral": 0.5600000023841858, "contempt": 0.05000000074505806, "surprise": 0.029999999329447746}', 'neutral', true, true);


--
-- TOC entry 3398 (class 0 OID 16514)
-- Dependencies: 211
-- Data for Name: item; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (242, 958, 'cell_phone', 89, 'data/mall/items/3-cell_phone-89.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (243, 962, 'cell_phone', 41, 'data/mall/items/11-cell_phone-41.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (244, 974, 'handbag', 49, 'data/mall/items/37-handbag-49.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (245, 977, 'bottle', 26, 'data/mall/items/43-bottle-26.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (246, 978, 'handbag', 35, 'data/mall/items/46-handbag-35.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (269, 1073, 'handbag', 68, 'data/aquarel_2/items/2-handbag-68.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (270, 1073, 'book', 46, 'data/aquarel_2/items/2-book-46.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (271, 1073, 'laptop', 60, 'data/aquarel_2/items/2-laptop-60.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (275, 1217, 'skateboard', 38, 'data/street_25sec_1/items/1-skateboard-38.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (276, 1217, 'handbag', 37, 'data/street_25sec_1/items/1-handbag-37.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (277, 1255, 'skateboard', 44, 'data/thailand30sec_1/items/17-skateboard-44.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (278, 1264, 'bottle', 27, 'data/thailand30sec_1/items/34-bottle-27.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (279, 1264, 'handbag', 34, 'data/thailand30sec_1/items/34-handbag-34.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (280, 1543, 'skateboard', 51, 'data/beach30sec_2/items/8-skateboard-51.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (281, 1545, 'handbag', 63, 'data/thailand30sec_2/items/1-handbag-63.png');
INSERT INTO public.item (item_id, person_id, item_name, confidence, item_photo) OVERRIDING SYSTEM VALUE VALUES (282, 1545, 'bottle', 42, 'data/thailand30sec_2/items/1-bottle-42.png');


--
-- TOC entry 3397 (class 0 OID 16502)
-- Dependencies: 210
-- Data for Name: person; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1683, 'data/1min10sec/photoboxes/person1.png', '00:00:00', 97, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1684, 'data/1min10sec/photoboxes/person2.png', '00:00:00', 97, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1685, 'data/1min10sec/photoboxes/person3.png', '00:00:00', 97, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1686, 'data/1min10sec/photoboxes/person6.png', '00:00:00', 97, 6, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1687, 'data/1min10sec/photoboxes/person8.png', '00:00:00', 97, 8, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1688, 'data/1min10sec/photoboxes/person9.png', '00:00:00', 97, 9, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1689, 'data/1min10sec/photoboxes/person13.png', '00:00:02', 97, 13, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1690, 'data/1min10sec/photoboxes/person14.png', '00:00:03', 97, 14, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1691, 'data/1min10sec/photoboxes/person33.png', '00:00:15', 97, 33, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1692, 'data/1min10sec/photoboxes/person43.png', '00:00:22', 97, 43, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1693, 'data/1min10sec/photoboxes/person47.png', '00:00:24', 97, 47, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1694, 'data/1min10sec/photoboxes/person50.png', '00:00:26', 97, 50, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1695, 'data/1min10sec/photoboxes/person51.png', '00:00:27', 97, 51, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1696, 'data/1min10sec/photoboxes/person52.png', '00:00:30', 97, 52, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1697, 'data/1min10sec/photoboxes/person54.png', '00:00:30', 97, 54, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (956, 'data/mall/photoboxes/person1.png', '00:00:00', 66, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (957, 'data/mall/photoboxes/person2.png', '00:00:00', 66, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (958, 'data/mall/photoboxes/person3.png', '00:00:00', 66, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (959, 'data/mall/photoboxes/person4.png', '00:00:00', 66, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (960, 'data/mall/photoboxes/person8.png', '00:00:02', 66, 8, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (961, 'data/mall/photoboxes/person9.png', '00:00:01', 66, 9, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (962, 'data/mall/photoboxes/person11.png', '00:00:02', 66, 11, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (963, 'data/mall/photoboxes/person16.png', '00:00:03', 66, 16, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (964, 'data/mall/photoboxes/person17.png', '00:00:05', 66, 17, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (965, 'data/mall/photoboxes/person18.png', '00:00:04', 66, 18, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (966, 'data/mall/photoboxes/person20.png', '00:00:11', 66, 20, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (967, 'data/mall/photoboxes/person21.png', '00:00:12', 66, 21, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (968, 'data/mall/photoboxes/person28.png', '00:00:17', 66, 28, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (969, 'data/mall/photoboxes/person29.png', '00:00:19', 66, 29, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (970, 'data/mall/photoboxes/person32.png', '00:00:21', 66, 32, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (971, 'data/mall/photoboxes/person33.png', '00:00:21', 66, 33, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (972, 'data/mall/photoboxes/person34.png', '00:00:21', 66, 34, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (973, 'data/mall/photoboxes/person35.png', '00:00:22', 66, 35, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (974, 'data/mall/photoboxes/person37.png', '00:00:23', 66, 37, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (975, 'data/mall/photoboxes/person39.png', '00:00:25', 66, 39, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (976, 'data/mall/photoboxes/person41.png', '00:00:26', 66, 41, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (977, 'data/mall/photoboxes/person43.png', '00:00:27', 66, 43, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (978, 'data/mall/photoboxes/person46.png', '00:00:27', 66, 46, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (979, 'data/mall/photoboxes/person47.png', '00:00:29', 66, 47, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (980, 'data/mall/photoboxes/person48.png', '00:00:28', 66, 48, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (981, 'data/mall/photoboxes/person52.png', '00:00:29', 66, 52, 26);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (982, 'data/mall/photoboxes/person53.png', '00:00:30', 66, 53, 27);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (983, 'data/mall/photoboxes/person54.png', '00:00:30', 66, 54, 28);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (984, 'data/mall/photoboxes/person56.png', '00:00:33', 66, 56, 29);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1698, 'data/1min10sec/photoboxes/person56.png', '00:00:30', 97, 56, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1699, 'data/1min10sec/photoboxes/person57.png', '00:00:31', 97, 57, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1700, 'data/1min10sec/photoboxes/person58.png', '00:00:32', 97, 58, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1701, 'data/1min10sec/photoboxes/person63.png', '00:00:37', 97, 63, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1702, 'data/1min10sec/photoboxes/person67.png', '00:00:44', 97, 67, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1703, 'data/1min10sec/photoboxes/person68.png', '00:00:46', 97, 68, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1704, 'data/1min10sec/photoboxes/person75.png', '00:01:04', 97, 75, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1705, 'data/27sec/photoboxes/person1.png', '00:00:00', 98, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1706, 'data/27sec/photoboxes/person2.png', '00:00:00', 98, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1707, 'data/27sec/photoboxes/person3.png', '00:00:00', 98, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1708, 'data/27sec/photoboxes/person4.png', '00:00:00', 98, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1709, 'data/27sec/photoboxes/person5.png', '00:00:00', 98, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1710, 'data/27sec/photoboxes/person6.png', '00:00:00', 98, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1711, 'data/27sec/photoboxes/person7.png', '00:00:00', 98, 7, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1712, 'data/27sec/photoboxes/person8.png', '00:00:00', 98, 8, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1713, 'data/27sec/photoboxes/person9.png', '00:00:00', 98, 9, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1714, 'data/27sec/photoboxes/person10.png', '00:00:00', 98, 10, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1715, 'data/27sec/photoboxes/person11.png', '00:00:00', 98, 11, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1716, 'data/27sec/photoboxes/person12.png', '00:00:00', 98, 12, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1717, 'data/27sec/photoboxes/person13.png', '00:00:00', 98, 13, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1718, 'data/27sec/photoboxes/person14.png', '00:00:02', 98, 14, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1719, 'data/27sec/photoboxes/person15.png', '00:00:01', 98, 15, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1720, 'data/27sec/photoboxes/person17.png', '00:00:01', 98, 17, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1721, 'data/27sec/photoboxes/person19.png', '00:00:08', 98, 19, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1722, 'data/27sec/photoboxes/person20.png', '00:00:12', 98, 20, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1723, 'data/27sec/photoboxes/person26.png', '00:00:16', 98, 26, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1724, 'data/27sec/photoboxes/person28.png', '00:00:19', 98, 28, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1725, 'data/27sec/photoboxes/person30.png', '00:00:19', 98, 30, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1726, 'data/27sec/photoboxes/person31.png', '00:00:24', 98, 31, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1727, 'data/27sec/photoboxes/person33.png', '00:00:22', 98, 33, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1728, 'data/27sec/photoboxes/person34.png', '00:00:23', 98, 34, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1031, 'data/aquarel/photoboxes/person1.png', '00:00:00', 69, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1032, 'data/aquarel/photoboxes/person2.png', '00:00:00', 69, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1033, 'data/aquarel/photoboxes/person3.png', '00:00:00', 69, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1034, 'data/aquarel/photoboxes/person4.png', '00:00:00', 69, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1035, 'data/aquarel/photoboxes/person7.png', '00:00:01', 69, 7, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1036, 'data/aquarel/photoboxes/person8.png', '00:00:00', 69, 8, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1037, 'data/aquarel/photoboxes/person15.png', '00:00:02', 69, 15, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1038, 'data/aquarel/photoboxes/person16.png', '00:00:03', 69, 16, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1039, 'data/aquarel/photoboxes/person17.png', '00:00:03', 69, 17, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1040, 'data/aquarel/photoboxes/person21.png', '00:00:07', 69, 21, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1041, 'data/aquarel/photoboxes/person23.png', '00:00:07', 69, 23, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1042, 'data/aquarel/photoboxes/person25.png', '00:00:09', 69, 25, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1043, 'data/aquarel/photoboxes/person29.png', '00:00:06', 69, 29, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1044, 'data/aquarel/photoboxes/person33.png', '00:00:10', 69, 33, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1045, 'data/aquarel/photoboxes/person34.png', '00:00:11', 69, 34, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1046, 'data/aquarel/photoboxes/person36.png', '00:00:12', 69, 36, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1047, 'data/aquarel/photoboxes/person40.png', '00:00:13', 69, 40, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1072, 'data/aquarel_2/photoboxes/person1.png', '00:00:00', 71, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1073, 'data/aquarel_2/photoboxes/person2.png', '00:00:00', 71, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1074, 'data/aquarel_2/photoboxes/person3.png', '00:00:02', 71, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1075, 'data/aquarel_2/photoboxes/person4.png', '00:00:02', 71, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1076, 'data/aquarel_2/photoboxes/person5.png', '00:00:05', 71, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1077, 'data/aquarel_2/photoboxes/person6.png', '00:00:03', 71, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1078, 'data/aquarel_2/photoboxes/person12.png', '00:00:17', 71, 12, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1079, 'data/aquarel_2/photoboxes/person14.png', '00:00:20', 71, 14, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1080, 'data/aquarel_2/photoboxes/person19.png', '00:00:34', 71, 19, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1081, 'data/aquarel_2/photoboxes/person21.png', '00:00:36', 71, 21, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1082, 'data/aquarel_2/photoboxes/person26.png', '00:00:37', 71, 26, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1083, 'data/aquarel_2/photoboxes/person28.png', '00:00:39', 71, 28, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1084, 'data/aquarel_2/photoboxes/person29.png', '00:00:38', 71, 29, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1085, 'data/aquarel_2/photoboxes/person30.png', '00:00:39', 71, 30, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1086, 'data/aquarel_2/photoboxes/person31.png', '00:00:39', 71, 31, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1087, 'data/aquarel_1/photoboxes/person1.png', '00:00:00', 72, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1088, 'data/aquarel_1/photoboxes/person2.png', '00:00:00', 72, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1089, 'data/aquarel_1/photoboxes/person3.png', '00:00:00', 72, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1090, 'data/aquarel_1/photoboxes/person4.png', '00:00:00', 72, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1091, 'data/aquarel_1/photoboxes/person5.png', '00:00:00', 72, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1092, 'data/aquarel_1/photoboxes/person7.png', '00:00:00', 72, 7, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1093, 'data/aquarel_1/photoboxes/person10.png', '00:00:02', 72, 10, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1094, 'data/aquarel_1/photoboxes/person11.png', '00:00:00', 72, 11, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1095, 'data/aquarel_1/photoboxes/person13.png', '00:00:00', 72, 13, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1096, 'data/aquarel_1/photoboxes/person14.png', '00:00:01', 72, 14, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1097, 'data/aquarel_1/photoboxes/person16.png', '00:00:02', 72, 16, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1098, 'data/aquarel_1/photoboxes/person17.png', '00:00:01', 72, 17, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1099, 'data/aquarel_1/photoboxes/person18.png', '00:00:02', 72, 18, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1100, 'data/aquarel_1/photoboxes/person19.png', '00:00:02', 72, 19, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1101, 'data/aquarel_1/photoboxes/person22.png', '00:00:03', 72, 22, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1102, 'data/aquarel_1/photoboxes/person23.png', '00:00:04', 72, 23, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1103, 'data/aquarel_1/photoboxes/person24.png', '00:00:05', 72, 24, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1104, 'data/aquarel_1/photoboxes/person27.png', '00:00:06', 72, 27, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1105, 'data/aquarel_1/photoboxes/person28.png', '00:00:06', 72, 28, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1106, 'data/aquarel_1/photoboxes/person31.png', '00:00:07', 72, 31, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1107, 'data/aquarel_1/photoboxes/person32.png', '00:00:07', 72, 32, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1108, 'data/aquarel_1/photoboxes/person33.png', '00:00:08', 72, 33, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1109, 'data/aquarel_1/photoboxes/person40.png', '00:00:09', 72, 40, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1110, 'data/aquarel_1/photoboxes/person62.png', '00:00:10', 72, 62, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1111, 'data/aquarel_1/photoboxes/person63.png', '00:00:10', 72, 63, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1112, 'data/aquarel_1/photoboxes/person64.png', '00:00:10', 72, 64, 26);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1113, 'data/aquarel_1/photoboxes/person65.png', '00:00:10', 72, 65, 27);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1114, 'data/aquarel_1/photoboxes/person70.png', '00:00:11', 72, 70, 28);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1115, 'data/aquarel_1/photoboxes/person74.png', '00:00:15', 72, 74, 29);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1116, 'data/aquarel_1/photoboxes/person79.png', '00:00:14', 72, 79, 30);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1117, 'data/beach1min/photoboxes/person1.png', '00:00:08', 73, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1118, 'data/beach1min/photoboxes/person5.png', '00:00:16', 73, 5, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1119, 'data/beach1min/photoboxes/person6.png', '00:00:16', 73, 6, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1120, 'data/beach1min/photoboxes/person7.png', '00:00:22', 73, 7, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1121, 'data/beach1min/photoboxes/person8.png', '00:00:26', 73, 8, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1122, 'data/beach1min/photoboxes/person9.png', '00:00:27', 73, 9, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1123, 'data/beach1min/photoboxes/person10.png', '00:00:28', 73, 10, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1124, 'data/beach1min/photoboxes/person11.png', '00:00:32', 73, 11, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1125, 'data/beach1min/photoboxes/person12.png', '00:00:32', 73, 12, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1126, 'data/beach1min/photoboxes/person16.png', '00:00:35', 73, 16, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1127, 'data/beach1min/photoboxes/person19.png', '00:00:38', 73, 19, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1128, 'data/beach1min/photoboxes/person25.png', '00:00:47', 73, 25, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1129, 'data/krasnaya_polyana_40sec/photoboxes/person1.png', '00:00:00', 74, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1130, 'data/krasnaya_polyana_40sec/photoboxes/person2.png', '00:00:00', 74, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1131, 'data/krasnaya_polyana_40sec/photoboxes/person3.png', '00:00:00', 74, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1132, 'data/krasnaya_polyana_40sec/photoboxes/person6.png', '00:00:01', 74, 6, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1133, 'data/krasnaya_polyana_40sec/photoboxes/person8.png', '00:00:04', 74, 8, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1134, 'data/krasnaya_polyana_40sec/photoboxes/person14.png', '00:00:07', 74, 14, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1135, 'data/krasnaya_polyana_40sec/photoboxes/person18.png', '00:00:16', 74, 18, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1136, 'data/krasnaya_polyana_40sec/photoboxes/person20.png', '00:00:18', 74, 20, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1137, 'data/krasnaya_polyana_40sec/photoboxes/person22.png', '00:00:21', 74, 22, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1138, 'data/krasnaya_polyana_40sec/photoboxes/person23.png', '00:00:27', 74, 23, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1139, 'data/krasnaya_polyana_40sec/photoboxes/person35.png', '00:00:27', 74, 35, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1140, 'data/krasnaya_polyana_40sec/photoboxes/person44.png', '00:00:31', 74, 44, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1141, 'data/krasnaya_polyana_40sec/photoboxes/person45.png', '00:00:30', 74, 45, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1142, 'data/krasnaya_polyana_40sec/photoboxes/person47.png', '00:00:31', 74, 47, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1143, 'data/krasnaya_polyana_40sec/photoboxes/person48.png', '00:00:31', 74, 48, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1144, 'data/krasnaya_polyana_40sec/photoboxes/person49.png', '00:00:31', 74, 49, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1145, 'data/krasnaya_polyana_40sec/photoboxes/person50.png', '00:00:32', 74, 50, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1146, 'data/krasnaya_polyana_40sec/photoboxes/person51.png', '00:00:36', 74, 51, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1147, 'data/krasnaya_polyana_40sec/photoboxes/person52.png', '00:00:36', 74, 52, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1148, 'data/square30sec/photoboxes/person1.png', '00:00:00', 75, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1149, 'data/square30sec/photoboxes/person2.png', '00:00:00', 75, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1150, 'data/square30sec/photoboxes/person4.png', '00:00:00', 75, 4, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1151, 'data/square30sec/photoboxes/person5.png', '00:00:00', 75, 5, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1152, 'data/square30sec/photoboxes/person6.png', '00:00:00', 75, 6, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1153, 'data/square30sec/photoboxes/person7.png', '00:00:00', 75, 7, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1154, 'data/square30sec/photoboxes/person8.png', '00:00:00', 75, 8, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1155, 'data/square30sec/photoboxes/person9.png', '00:00:00', 75, 9, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1156, 'data/square30sec/photoboxes/person21.png', '00:00:03', 75, 21, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1157, 'data/square30sec/photoboxes/person29.png', '00:00:02', 75, 29, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1158, 'data/square30sec/photoboxes/person34.png', '00:00:06', 75, 34, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1159, 'data/square30sec/photoboxes/person41.png', '00:00:06', 75, 41, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1160, 'data/square30sec/photoboxes/person55.png', '00:00:13', 75, 55, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1161, 'data/square30sec/photoboxes/person58.png', '00:00:09', 75, 58, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1162, 'data/square30sec/photoboxes/person59.png', '00:00:09', 75, 59, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1163, 'data/square30sec/photoboxes/person64.png', '00:00:11', 75, 64, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1164, 'data/square30sec/photoboxes/person69.png', '00:00:16', 75, 69, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1165, 'data/square30sec/photoboxes/person71.png', '00:00:20', 75, 71, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1166, 'data/square30sec/photoboxes/person73.png', '00:00:23', 75, 73, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1167, 'data/square30sec/photoboxes/person79.png', '00:00:24', 75, 79, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1168, 'data/square30sec/photoboxes/person80.png', '00:00:24', 75, 80, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1169, 'data/square30sec/photoboxes/person81.png', '00:00:29', 75, 81, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1170, 'data/square30sec/photoboxes/person82.png', '00:00:27', 75, 82, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1171, 'data/square30sec/photoboxes/person87.png', '00:00:29', 75, 87, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1196, 'data/30sec/photoboxes/person1.png', '00:00:00', 77, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1197, 'data/30sec/photoboxes/person2.png', '00:00:00', 77, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1198, 'data/30sec/photoboxes/person3.png', '00:00:00', 77, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1199, 'data/30sec/photoboxes/person4.png', '00:00:00', 77, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1200, 'data/30sec/photoboxes/person5.png', '00:00:00', 77, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1201, 'data/30sec/photoboxes/person6.png', '00:00:00', 77, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1202, 'data/30sec/photoboxes/person7.png', '00:00:00', 77, 7, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1203, 'data/30sec/photoboxes/person8.png', '00:00:00', 77, 8, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1204, 'data/30sec/photoboxes/person9.png', '00:00:00', 77, 9, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1205, 'data/30sec/photoboxes/person10.png', '00:00:02', 77, 10, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1206, 'data/30sec/photoboxes/person11.png', '00:00:05', 77, 11, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1207, 'data/30sec/photoboxes/person13.png', '00:00:04', 77, 13, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1208, 'data/30sec/photoboxes/person14.png', '00:00:05', 77, 14, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1209, 'data/30sec/photoboxes/person15.png', '00:00:09', 77, 15, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1210, 'data/30sec/photoboxes/person16.png', '00:00:09', 77, 16, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1211, 'data/30sec/photoboxes/person18.png', '00:00:10', 77, 18, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1212, 'data/30sec/photoboxes/person20.png', '00:00:20', 77, 20, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1213, 'data/30sec/photoboxes/person21.png', '00:00:22', 77, 21, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1214, 'data/30sec/photoboxes/person23.png', '00:00:22', 77, 23, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1215, 'data/30sec/photoboxes/person28.png', '00:00:23', 77, 28, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1216, 'data/30sec/photoboxes/person29.png', '00:00:24', 77, 29, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1217, 'data/street_25sec_1/photoboxes/person1.png', '00:00:00', 78, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1218, 'data/street_25sec_1/photoboxes/person2.png', '00:00:00', 78, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1219, 'data/street_25sec_1/photoboxes/person3.png', '00:00:00', 78, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1220, 'data/street_25sec_1/photoboxes/person4.png', '00:00:00', 78, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1221, 'data/street_25sec_1/photoboxes/person5.png', '00:00:00', 78, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1222, 'data/street_25sec_1/photoboxes/person6.png', '00:00:00', 78, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1223, 'data/street_25sec_1/photoboxes/person11.png', '00:00:05', 78, 11, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1224, 'data/street_25sec_1/photoboxes/person13.png', '00:00:07', 78, 13, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1225, 'data/1min20sec/photoboxes/person1.png', '00:00:00', 79, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1226, 'data/1min20sec/photoboxes/person2.png', '00:00:00', 79, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1227, 'data/1min20sec/photoboxes/person3.png', '00:00:00', 79, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1228, 'data/1min20sec/photoboxes/person4.png', '00:00:00', 79, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1229, 'data/1min20sec/photoboxes/person5.png', '00:00:00', 79, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1230, 'data/1min20sec/photoboxes/person6.png', '00:00:02', 79, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1231, 'data/1min20sec/photoboxes/person7.png', '00:00:05', 79, 7, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1232, 'data/1min20sec/photoboxes/person11.png', '00:00:08', 79, 11, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1233, 'data/1min20sec/photoboxes/person12.png', '00:00:10', 79, 12, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1234, 'data/1min20sec/photoboxes/person16.png', '00:00:19', 79, 16, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1235, 'data/1min20sec/photoboxes/person17.png', '00:00:20', 79, 17, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1236, 'data/1min20sec/photoboxes/person18.png', '00:00:30', 79, 18, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1237, 'data/1min20sec/photoboxes/person19.png', '00:00:32', 79, 19, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1238, 'data/1min20sec/photoboxes/person20.png', '00:00:35', 79, 20, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1239, 'data/1min20sec/photoboxes/person21.png', '00:00:42', 79, 21, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1240, 'data/1min20sec/photoboxes/person25.png', '00:00:59', 79, 25, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1241, 'data/1min20sec/photoboxes/person27.png', '00:01:00', 79, 27, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1242, 'data/1min20sec/photoboxes/person28.png', '00:01:00', 79, 28, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1243, 'data/1min20sec/photoboxes/person29.png', '00:01:01', 79, 29, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1244, 'data/thailand30sec_1/photoboxes/person1.png', '00:00:00', 80, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1245, 'data/thailand30sec_1/photoboxes/person2.png', '00:00:00', 80, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1246, 'data/thailand30sec_1/photoboxes/person3.png', '00:00:00', 80, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1247, 'data/thailand30sec_1/photoboxes/person4.png', '00:00:00', 80, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1248, 'data/thailand30sec_1/photoboxes/person5.png', '00:00:02', 80, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1249, 'data/thailand30sec_1/photoboxes/person6.png', '00:00:00', 80, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1250, 'data/thailand30sec_1/photoboxes/person7.png', '00:00:00', 80, 7, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1251, 'data/thailand30sec_1/photoboxes/person8.png', '00:00:01', 80, 8, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1252, 'data/thailand30sec_1/photoboxes/person10.png', '00:00:06', 80, 10, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1253, 'data/thailand30sec_1/photoboxes/person12.png', '00:00:04', 80, 12, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1254, 'data/thailand30sec_1/photoboxes/person14.png', '00:00:08', 80, 14, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1255, 'data/thailand30sec_1/photoboxes/person17.png', '00:00:09', 80, 17, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1256, 'data/thailand30sec_1/photoboxes/person19.png', '00:00:11', 80, 19, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1257, 'data/thailand30sec_1/photoboxes/person21.png', '00:00:14', 80, 21, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1258, 'data/thailand30sec_1/photoboxes/person22.png', '00:00:14', 80, 22, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1259, 'data/thailand30sec_1/photoboxes/person25.png', '00:00:13', 80, 25, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1260, 'data/thailand30sec_1/photoboxes/person30.png', '00:00:19', 80, 30, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1261, 'data/thailand30sec_1/photoboxes/person31.png', '00:00:21', 80, 31, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1262, 'data/thailand30sec_1/photoboxes/person32.png', '00:00:20', 80, 32, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1263, 'data/thailand30sec_1/photoboxes/person33.png', '00:00:20', 80, 33, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1264, 'data/thailand30sec_1/photoboxes/person34.png', '00:00:22', 80, 34, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1265, 'data/thailand30sec_1/photoboxes/person35.png', '00:00:22', 80, 35, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1266, 'data/thailand30sec_1/photoboxes/person44.png', '00:00:29', 80, 44, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1267, 'data/thailand30sec_1/photoboxes/person47.png', '00:00:30', 80, 47, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1268, 'data/thailand30sec_1/photoboxes/person49.png', '00:00:28', 80, 49, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1269, 'data/25sec/photoboxes/person1.png', '00:00:00', 81, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1270, 'data/25sec/photoboxes/person2.png', '00:00:00', 81, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1271, 'data/25sec/photoboxes/person3.png', '00:00:00', 81, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1272, 'data/25sec/photoboxes/person4.png', '00:00:01', 81, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1273, 'data/25sec/photoboxes/person7.png', '00:00:02', 81, 7, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1274, 'data/25sec/photoboxes/person8.png', '00:00:02', 81, 8, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1275, 'data/25sec/photoboxes/person9.png', '00:00:15', 81, 9, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1276, 'data/25sec/photoboxes/person10.png', '00:00:16', 81, 10, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1277, 'data/25sec/photoboxes/person12.png', '00:00:23', 81, 12, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1278, 'data/thailand_35sec_4/photoboxes/person1.png', '00:00:00', 82, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1279, 'data/thailand_35sec_4/photoboxes/person2.png', '00:00:00', 82, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1280, 'data/thailand_35sec_4/photoboxes/person3.png', '00:00:00', 82, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1281, 'data/thailand_35sec_4/photoboxes/person4.png', '00:00:00', 82, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1282, 'data/thailand_35sec_4/photoboxes/person5.png', '00:00:00', 82, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1283, 'data/thailand_35sec_4/photoboxes/person6.png', '00:00:00', 82, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1284, 'data/thailand_35sec_4/photoboxes/person8.png', '00:00:00', 82, 8, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1285, 'data/thailand_35sec_4/photoboxes/person15.png', '00:00:02', 82, 15, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1286, 'data/thailand_35sec_4/photoboxes/person16.png', '00:00:00', 82, 16, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1287, 'data/thailand_35sec_4/photoboxes/person18.png', '00:00:01', 82, 18, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1288, 'data/thailand_35sec_4/photoboxes/person22.png', '00:00:02', 82, 22, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1289, 'data/thailand_35sec_4/photoboxes/person25.png', '00:00:04', 82, 25, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1290, 'data/thailand_35sec_4/photoboxes/person33.png', '00:00:05', 82, 33, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1291, 'data/thailand_35sec_4/photoboxes/person35.png', '00:00:06', 82, 35, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1292, 'data/thailand_35sec_4/photoboxes/person36.png', '00:00:06', 82, 36, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1293, 'data/thailand_35sec_4/photoboxes/person37.png', '00:00:08', 82, 37, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1294, 'data/thailand_35sec_4/photoboxes/person38.png', '00:00:08', 82, 38, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1295, 'data/thailand_35sec_4/photoboxes/person39.png', '00:00:08', 82, 39, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1296, 'data/thailand_35sec_4/photoboxes/person44.png', '00:00:10', 82, 44, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1297, 'data/thailand_35sec_4/photoboxes/person45.png', '00:00:11', 82, 45, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1298, 'data/thailand_35sec_4/photoboxes/person48.png', '00:00:13', 82, 48, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1299, 'data/thailand_35sec_4/photoboxes/person54.png', '00:00:15', 82, 54, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1300, 'data/thailand_35sec_4/photoboxes/person63.png', '00:00:16', 82, 63, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1301, 'data/thailand_35sec_4/photoboxes/person65.png', '00:00:16', 82, 65, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1302, 'data/thailand_35sec_4/photoboxes/person66.png', '00:00:19', 82, 66, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1303, 'data/thailand_35sec_4/photoboxes/person68.png', '00:00:18', 82, 68, 26);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1304, 'data/thailand_35sec_4/photoboxes/person69.png', '00:00:19', 82, 69, 27);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1305, 'data/thailand_35sec_4/photoboxes/person70.png', '00:00:22', 82, 70, 28);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1306, 'data/thailand_35sec_4/photoboxes/person71.png', '00:00:21', 82, 71, 29);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1307, 'data/thailand_35sec_4/photoboxes/person75.png', '00:00:22', 82, 75, 30);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1308, 'data/thailand_35sec_4/photoboxes/person76.png', '00:00:23', 82, 76, 31);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1309, 'data/thailand_35sec_4/photoboxes/person81.png', '00:00:23', 82, 81, 32);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1310, 'data/thailand_35sec_4/photoboxes/person84.png', '00:00:27', 82, 84, 33);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1311, 'data/thailand_35sec_4/photoboxes/person86.png', '00:00:28', 82, 86, 34);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1312, 'data/thailand_35sec_4/photoboxes/person87.png', '00:00:28', 82, 87, 35);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1313, 'data/thailand_35sec_4/photoboxes/person91.png', '00:00:29', 82, 91, 36);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1314, 'data/thailand_35sec_4/photoboxes/person93.png', '00:00:29', 82, 93, 37);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1315, 'data/thailand_35sec_4/photoboxes/person97.png', '00:00:29', 82, 97, 38);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1316, 'data/thailand_35sec_4/photoboxes/person98.png', '00:00:29', 82, 98, 39);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1317, 'data/thailand_35sec_4/photoboxes/person99.png', '00:00:32', 82, 99, 40);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1318, 'data/thailand_35sec_4/photoboxes/person100.png', '00:00:31', 82, 100, 41);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1319, 'data/thailand_35sec_4/photoboxes/person106.png', '00:00:34', 82, 106, 42);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1320, 'data/50sec/photoboxes/person1.png', '00:00:00', 83, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1321, 'data/50sec/photoboxes/person2.png', '00:00:00', 83, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1322, 'data/50sec/photoboxes/person3.png', '00:00:00', 83, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1323, 'data/50sec/photoboxes/person4.png', '00:00:00', 83, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1324, 'data/50sec/photoboxes/person8.png', '00:00:02', 83, 8, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1325, 'data/50sec/photoboxes/person9.png', '00:00:05', 83, 9, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1326, 'data/50sec/photoboxes/person10.png', '00:00:09', 83, 10, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1327, 'data/50sec/photoboxes/person11.png', '00:00:09', 83, 11, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1328, 'data/50sec/photoboxes/person12.png', '00:00:11', 83, 12, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1329, 'data/50sec/photoboxes/person13.png', '00:00:13', 83, 13, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1330, 'data/50sec/photoboxes/person16.png', '00:00:13', 83, 16, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1331, 'data/50sec/photoboxes/person17.png', '00:00:13', 83, 17, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1332, 'data/50sec/photoboxes/person18.png', '00:00:18', 83, 18, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1333, 'data/50sec/photoboxes/person19.png', '00:00:16', 83, 19, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1334, 'data/50sec/photoboxes/person22.png', '00:00:20', 83, 22, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1335, 'data/50sec/photoboxes/person24.png', '00:00:21', 83, 24, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1336, 'data/50sec/photoboxes/person28.png', '00:00:24', 83, 28, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1337, 'data/50sec/photoboxes/person29.png', '00:00:27', 83, 29, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1338, 'data/50sec/photoboxes/person30.png', '00:00:27', 83, 30, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1339, 'data/50sec/photoboxes/person35.png', '00:00:28', 83, 35, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1340, 'data/50sec/photoboxes/person40.png', '00:00:33', 83, 40, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1341, 'data/50sec/photoboxes/person41.png', '00:00:33', 83, 41, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1342, 'data/50sec/photoboxes/person44.png', '00:00:34', 83, 44, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1343, 'data/50sec/photoboxes/person59.png', '00:00:49', 83, 59, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1344, 'data/thailand30sec_3/photoboxes/person1.png', '00:00:00', 84, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1345, 'data/thailand30sec_3/photoboxes/person2.png', '00:00:00', 84, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1346, 'data/thailand30sec_3/photoboxes/person3.png', '00:00:00', 84, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1347, 'data/thailand30sec_3/photoboxes/person4.png', '00:00:00', 84, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1348, 'data/thailand30sec_3/photoboxes/person5.png', '00:00:00', 84, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1349, 'data/thailand30sec_3/photoboxes/person6.png', '00:00:00', 84, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1350, 'data/thailand30sec_3/photoboxes/person7.png', '00:00:00', 84, 7, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1351, 'data/thailand30sec_3/photoboxes/person8.png', '00:00:00', 84, 8, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1352, 'data/thailand30sec_3/photoboxes/person9.png', '00:00:00', 84, 9, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1353, 'data/thailand30sec_3/photoboxes/person10.png', '00:00:03', 84, 10, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1354, 'data/thailand30sec_3/photoboxes/person11.png', '00:00:01', 84, 11, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1355, 'data/thailand30sec_3/photoboxes/person13.png', '00:00:03', 84, 13, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1356, 'data/thailand30sec_3/photoboxes/person15.png', '00:00:04', 84, 15, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1357, 'data/thailand30sec_3/photoboxes/person16.png', '00:00:04', 84, 16, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1358, 'data/thailand30sec_3/photoboxes/person18.png', '00:00:05', 84, 18, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1359, 'data/thailand30sec_3/photoboxes/person19.png', '00:00:05', 84, 19, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1360, 'data/thailand30sec_3/photoboxes/person21.png', '00:00:06', 84, 21, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1361, 'data/thailand30sec_3/photoboxes/person23.png', '00:00:07', 84, 23, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1362, 'data/thailand30sec_3/photoboxes/person25.png', '00:00:07', 84, 25, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1363, 'data/thailand30sec_3/photoboxes/person31.png', '00:00:09', 84, 31, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1364, 'data/thailand30sec_3/photoboxes/person32.png', '00:00:09', 84, 32, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1365, 'data/thailand30sec_3/photoboxes/person33.png', '00:00:10', 84, 33, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1366, 'data/thailand30sec_3/photoboxes/person34.png', '00:00:10', 84, 34, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1367, 'data/thailand30sec_3/photoboxes/person38.png', '00:00:14', 84, 38, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1368, 'data/thailand30sec_3/photoboxes/person40.png', '00:00:12', 84, 40, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1369, 'data/thailand30sec_3/photoboxes/person41.png', '00:00:12', 84, 41, 26);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1370, 'data/thailand30sec_3/photoboxes/person43.png', '00:00:15', 84, 43, 27);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1371, 'data/thailand30sec_3/photoboxes/person44.png', '00:00:14', 84, 44, 28);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1372, 'data/thailand30sec_3/photoboxes/person45.png', '00:00:14', 84, 45, 29);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1373, 'data/thailand30sec_3/photoboxes/person51.png', '00:00:17', 84, 51, 30);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1374, 'data/thailand30sec_3/photoboxes/person52.png', '00:00:19', 84, 52, 31);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1375, 'data/thailand30sec_3/photoboxes/person54.png', '00:00:20', 84, 54, 32);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1376, 'data/thailand30sec_3/photoboxes/person55.png', '00:00:20', 84, 55, 33);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1377, 'data/thailand30sec_3/photoboxes/person57.png', '00:00:24', 84, 57, 34);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1378, 'data/thailand30sec_3/photoboxes/person58.png', '00:00:24', 84, 58, 35);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1379, 'data/thailand30sec_3/photoboxes/person59.png', '00:00:22', 84, 59, 36);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1380, 'data/thailand30sec_3/photoboxes/person65.png', '00:00:24', 84, 65, 37);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1381, 'data/thailand30sec_3/photoboxes/person67.png', '00:00:24', 84, 67, 38);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1382, 'data/thailand30sec_3/photoboxes/person68.png', '00:00:26', 84, 68, 39);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1383, 'data/thailand30sec_3/photoboxes/person69.png', '00:00:26', 84, 69, 40);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1384, 'data/thailand30sec_3/photoboxes/person70.png', '00:00:26', 84, 70, 41);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1385, 'data/thailand30sec_3/photoboxes/person77.png', '00:00:28', 84, 77, 42);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1386, 'data/thailand30sec_3/photoboxes/person78.png', '00:00:28', 84, 78, 43);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1387, 'data/beach30sec_1/photoboxes/person1.png', '00:00:00', 85, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1388, 'data/beach30sec_1/photoboxes/person3.png', '00:00:05', 85, 3, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1389, 'data/beach30sec_1/photoboxes/person4.png', '00:00:00', 85, 4, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1390, 'data/beach30sec_1/photoboxes/person5.png', '00:00:00', 85, 5, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1391, 'data/beach30sec_1/photoboxes/person6.png', '00:00:02', 85, 6, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1392, 'data/beach30sec_1/photoboxes/person7.png', '00:00:00', 85, 7, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1393, 'data/beach30sec_1/photoboxes/person9.png', '00:00:00', 85, 9, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1394, 'data/beach30sec_1/photoboxes/person11.png', '00:00:02', 85, 11, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1395, 'data/beach30sec_1/photoboxes/person12.png', '00:00:01', 85, 12, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1396, 'data/beach30sec_1/photoboxes/person15.png', '00:00:01', 85, 15, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1397, 'data/beach30sec_1/photoboxes/person17.png', '00:00:02', 85, 17, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1398, 'data/beach30sec_1/photoboxes/person21.png', '00:00:07', 85, 21, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1399, 'data/beach30sec_1/photoboxes/person24.png', '00:00:05', 85, 24, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1400, 'data/beach30sec_1/photoboxes/person33.png', '00:00:06', 85, 33, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1401, 'data/beach30sec_1/photoboxes/person35.png', '00:00:05', 85, 35, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1402, 'data/beach30sec_1/photoboxes/person36.png', '00:00:07', 85, 36, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1403, 'data/beach30sec_1/photoboxes/person40.png', '00:00:08', 85, 40, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1404, 'data/beach30sec_1/photoboxes/person42.png', '00:00:07', 85, 42, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1405, 'data/beach30sec_1/photoboxes/person44.png', '00:00:07', 85, 44, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1406, 'data/beach30sec_1/photoboxes/person46.png', '00:00:08', 85, 46, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1407, 'data/beach30sec_1/photoboxes/person47.png', '00:00:08', 85, 47, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1408, 'data/beach30sec_1/photoboxes/person51.png', '00:00:11', 85, 51, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1409, 'data/beach30sec_1/photoboxes/person56.png', '00:00:12', 85, 56, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1410, 'data/beach30sec_1/photoboxes/person57.png', '00:00:12', 85, 57, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1411, 'data/beach30sec_1/photoboxes/person59.png', '00:00:13', 85, 59, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1412, 'data/beach30sec_1/photoboxes/person62.png', '00:00:13', 85, 62, 26);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1413, 'data/beach30sec_1/photoboxes/person64.png', '00:00:14', 85, 64, 27);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1414, 'data/beach30sec_1/photoboxes/person71.png', '00:00:15', 85, 71, 28);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1415, 'data/beach30sec_1/photoboxes/person75.png', '00:00:19', 85, 75, 29);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1416, 'data/beach30sec_1/photoboxes/person76.png', '00:00:21', 85, 76, 30);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1417, 'data/beach30sec_1/photoboxes/person80.png', '00:00:21', 85, 80, 31);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1418, 'data/beach30sec_1/photoboxes/person84.png', '00:00:26', 85, 84, 32);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1419, 'data/beach30sec_1/photoboxes/person85.png', '00:00:23', 85, 85, 33);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1420, 'data/beach30sec_1/photoboxes/person89.png', '00:00:25', 85, 89, 34);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1421, 'data/beach30sec_1/photoboxes/person90.png', '00:00:27', 85, 90, 35);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1422, 'data/beach30sec_1/photoboxes/person91.png', '00:00:25', 85, 91, 36);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1423, 'data/beach30sec_1/photoboxes/person98.png', '00:00:26', 85, 98, 37);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1424, 'data/square1min/photoboxes/person1.png', '00:00:00', 86, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1425, 'data/square1min/photoboxes/person2.png', '00:00:00', 86, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1426, 'data/square1min/photoboxes/person3.png', '00:00:00', 86, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1427, 'data/square1min/photoboxes/person4.png', '00:00:01', 86, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1428, 'data/square1min/photoboxes/person7.png', '00:00:00', 86, 7, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1429, 'data/square1min/photoboxes/person9.png', '00:00:03', 86, 9, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1430, 'data/square1min/photoboxes/person18.png', '00:00:01', 86, 18, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1431, 'data/square1min/photoboxes/person20.png', '00:00:08', 86, 20, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1432, 'data/square1min/photoboxes/person24.png', '00:00:02', 86, 24, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1433, 'data/square1min/photoboxes/person31.png', '00:00:08', 86, 31, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1434, 'data/square1min/photoboxes/person35.png', '00:00:07', 86, 35, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1435, 'data/square1min/photoboxes/person38.png', '00:00:07', 86, 38, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1436, 'data/square1min/photoboxes/person39.png', '00:00:08', 86, 39, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1437, 'data/square1min/photoboxes/person44.png', '00:00:09', 86, 44, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1438, 'data/square1min/photoboxes/person47.png', '00:00:10', 86, 47, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1439, 'data/square1min/photoboxes/person48.png', '00:00:12', 86, 48, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1440, 'data/square1min/photoboxes/person56.png', '00:00:14', 86, 56, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1441, 'data/square1min/photoboxes/person57.png', '00:00:13', 86, 57, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1442, 'data/square1min/photoboxes/person60.png', '00:00:14', 86, 60, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1443, 'data/square1min/photoboxes/person61.png', '00:00:18', 86, 61, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1444, 'data/square1min/photoboxes/person70.png', '00:00:17', 86, 70, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1445, 'data/square1min/photoboxes/person73.png', '00:00:22', 86, 73, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1446, 'data/square1min/photoboxes/person74.png', '00:00:18', 86, 74, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1447, 'data/square1min/photoboxes/person76.png', '00:00:17', 86, 76, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1448, 'data/square1min/photoboxes/person78.png', '00:00:18', 86, 78, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1449, 'data/square1min/photoboxes/person79.png', '00:00:19', 86, 79, 26);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1450, 'data/square1min/photoboxes/person82.png', '00:00:21', 86, 82, 27);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1451, 'data/square1min/photoboxes/person83.png', '00:00:21', 86, 83, 28);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1452, 'data/square1min/photoboxes/person85.png', '00:00:22', 86, 85, 29);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1453, 'data/square1min/photoboxes/person86.png', '00:00:24', 86, 86, 30);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1454, 'data/square1min/photoboxes/person87.png', '00:00:23', 86, 87, 31);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1455, 'data/square1min/photoboxes/person92.png', '00:00:28', 86, 92, 32);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1456, 'data/square1min/photoboxes/person102.png', '00:00:25', 86, 102, 33);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1457, 'data/square1min/photoboxes/person103.png', '00:00:26', 86, 103, 34);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1458, 'data/square1min/photoboxes/person105.png', '00:00:27', 86, 105, 35);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1459, 'data/square1min/photoboxes/person113.png', '00:00:29', 86, 113, 36);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1460, 'data/square1min/photoboxes/person115.png', '00:00:32', 86, 115, 37);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1461, 'data/square1min/photoboxes/person118.png', '00:00:32', 86, 118, 38);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1462, 'data/square1min/photoboxes/person120.png', '00:00:34', 86, 120, 39);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1463, 'data/square1min/photoboxes/person124.png', '00:00:33', 86, 124, 40);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1464, 'data/square1min/photoboxes/person129.png', '00:00:36', 86, 129, 41);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1465, 'data/square1min/photoboxes/person130.png', '00:00:38', 86, 130, 42);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1466, 'data/square1min/photoboxes/person133.png', '00:00:36', 86, 133, 43);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1467, 'data/square1min/photoboxes/person136.png', '00:00:39', 86, 135, 44);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1468, 'data/square1min/photoboxes/person139.png', '00:00:36', 86, 136, 45);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1469, 'data/square1min/photoboxes/person142.png', '00:00:45', 86, 139, 46);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1470, 'data/square1min/photoboxes/person144.png', '00:00:39', 86, 142, 47);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1471, 'data/square1min/photoboxes/person146.png', '00:00:40', 86, 144, 48);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1472, 'data/square1min/photoboxes/person147.png', '00:00:41', 86, 146, 49);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1473, 'data/square1min/photoboxes/person153.png', '00:00:45', 86, 147, 50);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1474, 'data/square1min/photoboxes/person154.png', '00:00:46', 86, 153, 51);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1475, 'data/square1min/photoboxes/person156.png', '00:00:48', 86, 154, 52);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1476, 'data/square1min/photoboxes/person158.png', '00:00:46', 86, 156, 53);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1477, 'data/square1min/photoboxes/person159.png', '00:00:47', 86, 158, 54);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1478, 'data/square1min/photoboxes/person163.png', '00:00:47', 86, 159, 55);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1479, 'data/square1min/photoboxes/person165.png', '00:00:48', 86, 163, 56);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1480, 'data/square1min/photoboxes/person175.png', '00:00:48', 86, 165, 57);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1481, 'data/square1min/photoboxes/person177.png', '00:00:53', 86, 175, 58);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1482, 'data/square1min/photoboxes/person185.png', '00:00:53', 86, 177, 59);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1483, 'data/square1min/photoboxes/person187.png', '00:00:53', 86, 185, 60);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1484, 'data/square1min/photoboxes/person192.png', '00:00:59', 86, 187, 61);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1485, 'data/square1min/photoboxes/person193.png', '00:00:58', 86, 192, 62);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1486, 'data/square1min/photoboxes/person196.png', '00:00:55', 86, 193, 63);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1516, 'data/37sec/photoboxes/person1.png', '00:00:00', 88, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1517, 'data/37sec/photoboxes/person2.png', '00:00:00', 88, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1518, 'data/37sec/photoboxes/person3.png', '00:00:00', 88, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1519, 'data/37sec/photoboxes/person4.png', '00:00:00', 88, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1520, 'data/37sec/photoboxes/person5.png', '00:00:02', 88, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1521, 'data/37sec/photoboxes/person7.png', '00:00:02', 88, 7, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1522, 'data/37sec/photoboxes/person12.png', '00:00:02', 88, 12, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1523, 'data/37sec/photoboxes/person14.png', '00:00:05', 88, 14, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1524, 'data/37sec/photoboxes/person15.png', '00:00:05', 88, 15, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1525, 'data/37sec/photoboxes/person16.png', '00:00:10', 88, 16, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1526, 'data/37sec/photoboxes/person17.png', '00:00:12', 88, 17, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1527, 'data/37sec/photoboxes/person21.png', '00:00:15', 88, 21, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1528, 'data/37sec/photoboxes/person25.png', '00:00:21', 88, 22, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1529, 'data/37sec/photoboxes/person28.png', '00:00:19', 88, 25, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1530, 'data/37sec/photoboxes/person31.png', '00:00:19', 88, 28, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1531, 'data/37sec/photoboxes/person36.png', '00:00:20', 88, 31, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1532, 'data/37sec/photoboxes/person39.png', '00:00:22', 88, 36, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1533, 'data/37sec/photoboxes/person46.png', '00:00:24', 88, 39, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1534, 'data/37sec/photoboxes/person48.png', '00:00:28', 88, 46, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1535, 'data/37sec/photoboxes/person50.png', '00:00:29', 88, 48, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1536, 'data/37sec/photoboxes/person52.png', '00:00:31', 88, 50, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1537, 'data/37sec/photoboxes/person63.png', '00:00:32', 88, 52, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1538, 'data/37sec/photoboxes/person65.png', '00:00:35', 88, 63, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1539, 'data/37sec/photoboxes/person67.png', '00:00:35', 88, 65, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1540, 'data/beach30sec_2/photoboxes/person1.png', '00:00:00', 89, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1541, 'data/beach30sec_2/photoboxes/person3.png', '00:00:07', 89, 3, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1542, 'data/beach30sec_2/photoboxes/person5.png', '00:00:12', 89, 5, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1543, 'data/beach30sec_2/photoboxes/person8.png', '00:00:11', 89, 8, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1544, 'data/beach30sec_2/photoboxes/person12.png', '00:00:18', 89, 12, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1545, 'data/thailand30sec_2/photoboxes/person1.png', '00:00:00', 90, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1546, 'data/thailand30sec_2/photoboxes/person2.png', '00:00:00', 90, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1547, 'data/thailand30sec_2/photoboxes/person3.png', '00:00:00', 90, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1548, 'data/thailand30sec_2/photoboxes/person4.png', '00:00:00', 90, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1549, 'data/thailand30sec_2/photoboxes/person5.png', '00:00:00', 90, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1550, 'data/thailand30sec_2/photoboxes/person6.png', '00:00:00', 90, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1551, 'data/thailand30sec_2/photoboxes/person7.png', '00:00:00', 90, 7, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1552, 'data/thailand30sec_2/photoboxes/person12.png', '00:00:02', 90, 12, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1553, 'data/thailand30sec_2/photoboxes/person18.png', '00:00:04', 90, 18, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1554, 'data/thailand30sec_2/photoboxes/person22.png', '00:00:05', 90, 22, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1555, 'data/thailand30sec_2/photoboxes/person23.png', '00:00:06', 90, 23, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1556, 'data/thailand30sec_2/photoboxes/person24.png', '00:00:09', 90, 24, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1557, 'data/thailand30sec_2/photoboxes/person28.png', '00:00:08', 90, 28, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1558, 'data/thailand30sec_2/photoboxes/person30.png', '00:00:11', 90, 30, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1559, 'data/thailand30sec_2/photoboxes/person33.png', '00:00:10', 90, 33, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1560, 'data/thailand30sec_2/photoboxes/person34.png', '00:00:15', 90, 34, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1561, 'data/thailand30sec_2/photoboxes/person35.png', '00:00:12', 90, 35, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1562, 'data/thailand30sec_2/photoboxes/person39.png', '00:00:14', 90, 39, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1563, 'data/thailand30sec_2/photoboxes/person40.png', '00:00:15', 90, 40, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1564, 'data/thailand30sec_2/photoboxes/person44.png', '00:00:16', 90, 44, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1565, 'data/thailand30sec_2/photoboxes/person45.png', '00:00:16', 90, 45, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1566, 'data/thailand30sec_2/photoboxes/person47.png', '00:00:16', 90, 47, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1567, 'data/thailand30sec_2/photoboxes/person49.png', '00:00:19', 90, 49, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1568, 'data/thailand30sec_2/photoboxes/person50.png', '00:00:19', 90, 50, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1569, 'data/thailand30sec_2/photoboxes/person59.png', '00:00:23', 90, 59, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1570, 'data/thailand30sec_2/photoboxes/person63.png', '00:00:27', 90, 63, 26);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1571, 'data/thailand30sec_2/photoboxes/person64.png', '00:00:26', 90, 64, 27);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1759, 'data/10sec/photoboxes/person1.png', '00:00:00', 101, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1760, 'data/10sec/photoboxes/person2.png', '00:00:00', 101, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1761, 'data/10sec/photoboxes/person3.png', '00:00:00', 101, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1762, 'data/10sec/photoboxes/person4.png', '00:00:00', 101, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1763, 'data/10sec/photoboxes/person6.png', '00:00:00', 101, 6, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1764, 'data/10sec/photoboxes/person7.png', '00:00:00', 101, 7, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1765, 'data/10sec/photoboxes/person8.png', '00:00:01', 101, 8, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1766, 'data/10sec/photoboxes/person10.png', '00:00:01', 101, 10, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1767, 'data/10sec/photoboxes/person11.png', '00:00:01', 101, 11, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1768, 'data/10sec/photoboxes/person16.png', '00:00:06', 101, 16, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1769, 'data/10sec/photoboxes/person17.png', '00:00:04', 101, 17, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1770, 'data/10sec/photoboxes/person18.png', '00:00:06', 101, 18, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1771, 'data/10sec/photoboxes/person19.png', '00:00:07', 101, 19, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1772, 'data/10sec/photoboxes/person20.png', '00:00:05', 101, 20, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1773, 'data/10sec/photoboxes/person21.png', '00:00:09', 101, 21, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1654, 'data/tokyo1/photoboxes/person1.png', '00:00:00', 96, 1, 1);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1655, 'data/tokyo1/photoboxes/person2.png', '00:00:00', 96, 2, 2);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1656, 'data/tokyo1/photoboxes/person3.png', '00:00:00', 96, 3, 3);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1657, 'data/tokyo1/photoboxes/person4.png', '00:00:00', 96, 4, 4);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1658, 'data/tokyo1/photoboxes/person5.png', '00:00:01', 96, 5, 5);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1659, 'data/tokyo1/photoboxes/person6.png', '00:00:04', 96, 6, 6);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1660, 'data/tokyo1/photoboxes/person7.png', '00:00:03', 96, 7, 7);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1661, 'data/tokyo1/photoboxes/person8.png', '00:00:03', 96, 8, 8);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1662, 'data/tokyo1/photoboxes/person10.png', '00:00:08', 96, 10, 9);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1663, 'data/tokyo1/photoboxes/person11.png', '00:00:08', 96, 11, 10);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1664, 'data/tokyo1/photoboxes/person12.png', '00:00:14', 96, 12, 11);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1665, 'data/tokyo1/photoboxes/person14.png', '00:00:16', 96, 14, 12);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1666, 'data/tokyo1/photoboxes/person16.png', '00:00:17', 96, 16, 13);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1667, 'data/tokyo1/photoboxes/person17.png', '00:00:18', 96, 17, 14);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1668, 'data/tokyo1/photoboxes/person18.png', '00:00:19', 96, 18, 15);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1669, 'data/tokyo1/photoboxes/person27.png', '00:00:22', 96, 27, 16);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1670, 'data/tokyo1/photoboxes/person29.png', '00:00:23', 96, 29, 17);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1671, 'data/tokyo1/photoboxes/person31.png', '00:00:24', 96, 31, 18);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1672, 'data/tokyo1/photoboxes/person33.png', '00:00:25', 96, 33, 19);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1673, 'data/tokyo1/photoboxes/person34.png', '00:00:25', 96, 34, 20);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1674, 'data/tokyo1/photoboxes/person37.png', '00:00:28', 96, 37, 21);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1675, 'data/tokyo1/photoboxes/person42.png', '00:00:28', 96, 42, 22);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1676, 'data/tokyo1/photoboxes/person44.png', '00:00:29', 96, 44, 23);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1677, 'data/tokyo1/photoboxes/person46.png', '00:00:30', 96, 46, 24);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1678, 'data/tokyo1/photoboxes/person47.png', '00:00:31', 96, 47, 25);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1679, 'data/tokyo1/photoboxes/person48.png', '00:00:32', 96, 48, 26);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1680, 'data/tokyo1/photoboxes/person50.png', '00:00:33', 96, 50, 27);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1681, 'data/tokyo1/photoboxes/person51.png', '00:00:34', 96, 51, 28);
INSERT INTO public.person (person_id, photobox, appear_time, video_id, tracker_id, ui_tracker_id) OVERRIDING SYSTEM VALUE VALUES (1682, 'data/tokyo1/photoboxes/person58.png', '00:00:36', 96, 53, 29);


--
-- TOC entry 3409 (class 0 OID 16576)
-- Dependencies: 222
-- Data for Name: target; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.target (target_id, video_id, target_items_path, target_emotions_path) OVERRIDING SYSTEM VALUE VALUES (2, 81, 'data/25sec/target_items.csv', 'data/25sec/target_emotions.csv');
INSERT INTO public.target (target_id, video_id, target_items_path, target_emotions_path) OVERRIDING SYSTEM VALUE VALUES (9, 101, 'data/10sec/target_items.csv', 'data/10sec/target_emotions.csv');
INSERT INTO public.target (target_id, video_id, target_items_path, target_emotions_path) OVERRIDING SYSTEM VALUE VALUES (12, 98, 'data/27sec/target_items.csv', 'data/27sec/target_emotions.csv');
INSERT INTO public.target (target_id, video_id, target_items_path, target_emotions_path) OVERRIDING SYSTEM VALUE VALUES (13, 66, 'data/mall/target_items.csv', 'data/mall/target_emotions.csv');


--
-- TOC entry 3396 (class 0 OID 16482)
-- Dependencies: 209
-- Data for Name: video; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (85, '/home/slava/projects/nir_7sem/videos/beach30sec_1.mp4', 'data/beach30sec_1');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (86, '/home/slava/projects/nir_7sem/videos/square1min.mp4', 'data/square1min');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (88, '/home/slava/projects/nir_7sem/videos/37sec.mkv', 'data/37sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (89, '/home/slava/projects/nir_7sem/videos/beach30sec_2.mp4', 'data/beach30sec_2');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (90, '/home/slava/projects/nir_7sem/videos/thailand30sec_2.mp4', 'data/thailand30sec_2');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (96, '/home/slava/projects/nir_7sem/videos/tokyo1.mp4', 'data/tokyo1');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (97, '/home/slava/projects/nir_7sem/videos/1min10sec.mkv', 'data/1min10sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (98, '/home/slava/projects/nir_7sem/videos/27sec.mkv', 'data/27sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (101, '/home/slava/projects/nir_7sem/videos/10sec.mkv', 'data/10sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (66, '/home/slava/projects/nir_7sem/videos/mall.mp4', 'data/mall');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (69, '/home/slava/projects/nir_7sem/videos/aquarel.mp4', 'data/aquarel');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (71, '/home/slava/projects/nir_7sem/videos/aquarel_2.mp4', 'data/aquarel_2');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (72, '/home/slava/projects/nir_7sem/videos/aquarel_1.mp4', 'data/aquarel_1');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (73, '/home/slava/projects/nir_7sem/videos/beach1min.mp4', 'data/beach1min');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (74, '/home/slava/projects/nir_7sem/videos/krasnaya_polyana_40sec.mp4', 'data/krasnaya_polyana_40sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (75, '/home/slava/projects/nir_7sem/videos/square30sec.mp4', 'data/square30sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (77, '/home/slava/projects/nir_7sem/videos/30sec.mkv', 'data/30sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (78, '/home/slava/projects/nir_7sem/videos/street_25sec_1.mp4', 'data/street_25sec_1');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (79, '/home/slava/projects/nir_7sem/videos/1min20sec.mkv', 'data/1min20sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (80, '/home/slava/projects/nir_7sem/videos/thailand30sec_1.mp4', 'data/thailand30sec_1');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (81, '/home/slava/projects/nir_7sem/videos/25sec.mkv', 'data/25sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (82, '/home/slava/projects/nir_7sem/videos/thailand_35sec_4.mp4', 'data/thailand_35sec_4');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (83, '/home/slava/projects/nir_7sem/videos/50sec.mp4', 'data/50sec');
INSERT INTO public.video (video_id, video_path, data_path) OVERRIDING SYSTEM VALUE VALUES (84, '/home/slava/projects/nir_7sem/videos/thailand30sec_3.mp4', 'data/thailand30sec_3');


--
-- TOC entry 3407 (class 0 OID 16563)
-- Dependencies: 220
-- Data for Name: videoclip; Type: TABLE DATA; Schema: public; Owner: postgres
--

INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (7, 957, 'data/mall/videoclips/person2.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (8, 958, 'data/mall/videoclips/person3.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (9, 962, 'data/mall/videoclips/person11.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (10, 965, 'data/mall/videoclips/person18.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (11, 981, 'data/mall/videoclips/person52.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (13, 1039, 'data/aquarel/videoclips/person17.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (14, 1038, 'data/aquarel/videoclips/person16.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (16, 1081, 'data/aquarel_2/videoclips/person21.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (19, 1254, 'data/thailand30sec_1/videoclips/person14.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (20, 1369, 'data/thailand30sec_3/videoclips/person41.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (21, 1541, 'data/beach30sec_2/videoclips/person3.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (22, 1544, 'data/beach30sec_2/videoclips/person12.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (23, 1557, 'data/thailand30sec_2/videoclips/person28.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (24, 1320, 'data/50sec/videoclips/person1.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (25, 1548, 'data/thailand30sec_2/videoclips/person4.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (30, 1695, 'data/1min10sec/videoclips/person51.mp4');
INSERT INTO public.videoclip (videoclip_id, person_id, videoclip_path) OVERRIDING SYSTEM VALUE VALUES (31, 1700, 'data/1min10sec/videoclips/person58.mp4');


--
-- TOC entry 3415 (class 0 OID 0)
-- Dependencies: 217
-- Name: diagramm_diagramm_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.diagramm_diagramm_id_seq', 53, true);


--
-- TOC entry 3416 (class 0 OID 0)
-- Dependencies: 216
-- Name: emotion_emotion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.emotion_emotion_id_seq', 157, true);


--
-- TOC entry 3417 (class 0 OID 0)
-- Dependencies: 214
-- Name: item_item_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.item_item_id_seq', 287, true);


--
-- TOC entry 3418 (class 0 OID 0)
-- Dependencies: 213
-- Name: person_person_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.person_person_id_seq', 1773, true);


--
-- TOC entry 3419 (class 0 OID 0)
-- Dependencies: 221
-- Name: target_analyze_target_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.target_analyze_target_id_seq', 13, true);


--
-- TOC entry 3420 (class 0 OID 0)
-- Dependencies: 212
-- Name: video_video_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.video_video_id_seq', 101, true);


--
-- TOC entry 3421 (class 0 OID 0)
-- Dependencies: 219
-- Name: videoclip_videoclip_id_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public.videoclip_videoclip_id_seq', 31, true);


--
-- TOC entry 3246 (class 2606 OID 16556)
-- Name: diagramm diagramm_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diagramm
    ADD CONSTRAINT diagramm_pkey PRIMARY KEY (diagramm_id);


--
-- TOC entry 3244 (class 2606 OID 16544)
-- Name: emotion emotion_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emotion
    ADD CONSTRAINT emotion_pkey PRIMARY KEY (emotion_id);


--
-- TOC entry 3242 (class 2606 OID 16518)
-- Name: item item_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT item_pkey PRIMARY KEY (item_id);


--
-- TOC entry 3240 (class 2606 OID 16508)
-- Name: person person_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT person_pkey PRIMARY KEY (person_id);


--
-- TOC entry 3250 (class 2606 OID 16582)
-- Name: target target_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.target
    ADD CONSTRAINT target_pkey PRIMARY KEY (target_id);


--
-- TOC entry 3238 (class 2606 OID 16486)
-- Name: video video_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.video
    ADD CONSTRAINT video_pkey PRIMARY KEY (video_id);


--
-- TOC entry 3248 (class 2606 OID 16567)
-- Name: videoclip videoclip_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.videoclip
    ADD CONSTRAINT videoclip_pkey PRIMARY KEY (videoclip_id);


--
-- TOC entry 3254 (class 2606 OID 16557)
-- Name: diagramm person_diagramm_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.diagramm
    ADD CONSTRAINT person_diagramm_fk FOREIGN KEY (person_id) REFERENCES public.person(person_id);


--
-- TOC entry 3253 (class 2606 OID 16545)
-- Name: emotion person_emotion_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.emotion
    ADD CONSTRAINT person_emotion_fk FOREIGN KEY (person_id) REFERENCES public.person(person_id);


--
-- TOC entry 3252 (class 2606 OID 16531)
-- Name: item person_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.item
    ADD CONSTRAINT person_fk FOREIGN KEY (person_id) REFERENCES public.person(person_id) NOT VALID;


--
-- TOC entry 3255 (class 2606 OID 16568)
-- Name: videoclip person_videoclip_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.videoclip
    ADD CONSTRAINT person_videoclip_fk FOREIGN KEY (person_id) REFERENCES public.person(person_id);


--
-- TOC entry 3251 (class 2606 OID 16525)
-- Name: person video_fkey; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.person
    ADD CONSTRAINT video_fkey FOREIGN KEY (video_id) REFERENCES public.video(video_id) NOT VALID;


--
-- TOC entry 3256 (class 2606 OID 16583)
-- Name: target video_target_fk; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.target
    ADD CONSTRAINT video_target_fk FOREIGN KEY (video_id) REFERENCES public.video(video_id);


-- Completed on 2024-04-25 21:10:07 MSK

--
-- PostgreSQL database dump complete
--

