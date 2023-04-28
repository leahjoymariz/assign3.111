


CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(256),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);


INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash Dishes",
    "Do the Laundry"
   
);

INSERT INTO task (
    summary,
    description,
) VALUES (
    "Wash Dishes",
    "Do the Laundry"
   
);

INSERT INTO task (
    summary,
    description
) VALUES (
    "Wash the car",
    "Give the car a good scrubbing"
);