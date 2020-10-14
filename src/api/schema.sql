CREATE TABLE alarms (
	id INTEGER PRIMARY KEY,
	hours Integer NOT NULL,
	minutes INTEGER NOT NULL,
	active BOOLEAN NOT NULL CHECK (active IN (0,1))
);