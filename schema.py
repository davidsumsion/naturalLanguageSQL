sql_create_student_table = """
    CREATE TABLE student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(30)
    );
"""

sql_create_enrollment_table = """
    CREATE TABLE enrollment (
    class_id INT,
    student_id INT,
    PRIMARY KEY (class_id, student_id)
    );
"""

sql_create_class_table = """
    CREATE TABLE class (
        class_id INT PRIMARY KEY ,
        class_code VARCHAR(6),
        class_name VARCHAR(30)
    );
"""
sql_create_class_student_table = """
    CREATE TABLE class_building (
        class_id INT,
        building_id INT,
        PRIMARY KEY (class_id, building_id)
    );
"""

sql_create_building_table = """
    CREATE TABLE building (
    building_id INT PRIMARY KEY ,
    building_description VARCHAR(30),
    building_abbreviation VARCHAR(5)
);
"""