--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET lock_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: user; Type: TABLE; Schema: public; Owner: chris.bates; Tablespace: 
--

CREATE TABLE user (
    time_created timestamp without time zone,
    id integer NOT NULL,
    phone_number character varying(256)
);


ALTER TABLE public.user OWNER TO "chris.bates";

--
-- Name: user_id_seq; Type: SEQUENCE; Schema: public; Owner: chris.bates
--

CREATE SEQUENCE user_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_id_seq OWNER TO "chris.bates";

--
-- Name: user_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: chris.bates
--

ALTER SEQUENCE user_id_seq OWNED BY user.id;


--
-- Name: application_type; Type: TABLE; Schema: public; Owner: chris.bates; Tablespace: 
--

CREATE TABLE journal (
    time_created timestamp without time zone,
    id integer NOT NULL,
    emotion_id integer,
    emotion character varying(256),
    description character varying(1000),
);


ALTER TABLE public.journal OWNER TO "chris.bates";

--
-- Name: journal_id_seq; Type: SEQUENCE; Schema: public; Owner: chris.bates
--

CREATE SEQUENCE journal_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.journal_id_seq OWNER TO "chris.bates";

--
-- Name: journal_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: chris.bates
--

ALTER SEQUENCE journal_id_seq OWNED BY journal.id;


--
-- Name: emotion; Type: TABLE; Schema: public; Owner: chris.bates; Tablespace: 
--

CREATE TABLE emotion (
    time_created timestamp without time zone,
    id integer NOT NULL,
    name character varying(256)
);


ALTER TABLE public.emotion OWNER TO "chris.bates";

--
-- Name: emotion_id_seq; Type: SEQUENCE; Schema: public; Owner: chris.bates
--

CREATE SEQUENCE emotion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.emotion_id_seq OWNER TO "chris.bates";

--
-- Name: emotion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: chris.bates
--

ALTER SEQUENCE emotion_id_seq OWNED BY emotion.id;


--
-- Name: public; Type: ACL; Schema: -; Owner: chris.bates
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM "chris.bates";
GRANT ALL ON SCHEMA public TO "chris.bates";
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

