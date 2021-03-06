
CREATE TABLE [animaux] (
    [id] INT PRIMARY KEY     NOT NULL,
    [famille_id]  INT        NOT NULL,
    sexe          TEXT       NOT NULL,
    presence      TEXT       NOT NULL,
    apprivoise    TEXT       NOT NULL,
    mort_ne       TEXT       NOT NULL,
    decede        TEXT       NOT NULL,
    FOREIGN KEY (famille_id) REFERENCES familles (id)
);

CREATE TABLE [familles] (
    [id] INT   PRIMARY KEY   NOT NULL,
    nom  TEXT     NOT NULL
);

CREATE TABLE [types] (
    [id]  INT  PRIMARY KEY   NOT NULL,
    type  TEXT  NOT NULL
);


CREATE TABLE [animaux_types] (
    [animal_id]   INT    NOT NULL,
    [type_id]     INT    NOT NULL,
    pourcentage   REAL   NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES animaux (id),
    FOREIGN KEY (type_id) REFERENCES types (id),
    PRIMARY KEY (animal_id,type_id)
);

CREATE TABLE [velages] (
    [id] INT   PRIMARY KEY   NOT NULL,
    [mere_id]  INT           NOT NULL,
    [pere_id]  INT           NOT NULL,
    date       TIMESTAMP     NOT NULL,
    FOREIGN KEY (mere_id) REFERENCES animaux (id),
    FOREIGN KEY (pere_id) REFERENCES animaux (id)
);

CREATE TABLE [animaux_velages] (
    [animal_id]   INT     NOT NULL,
    [velage_id]   INT     NOT NULL,
    FOREIGN KEY (animal_id) REFERENCES animaux (id),
    FOREIGN KEY (velage_id) REFERENCES velages (id),
    PRIMARY KEY (animal_id,velage_id)
);

CREATE TABLE [complications] (
    [id]   INT   PRIMARY KEY   NOT NULL,
    complication  TEXT         NOT NULL
);

CREATE TABLE [velages_complications] (
    [velage_id]         INTEGER   NOT NULL,
    [complication_id]   INTEGER   NOT NULL,
    FOREIGN KEY (complication_id) REFERENCES complications (id),
    FOREIGN KEY (velage_id) REFERENCES velages (id),
    PRIMARY KEY (velage_id,complication_id)
)