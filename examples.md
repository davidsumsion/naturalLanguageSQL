### Can you tell me which student had the least amount of classes enrolled in?
```
SELECT s.student_id, s.student_name, COUNT(e.class_id) AS class_count
FROM student s
LEFT JOIN enrollment e ON s.student_id = e.student_id
GROUP BY s.student_id, s.student_name
ORDER BY class_count ASC
LIMIT 1;
```

```(4, 'Emily Davis', 0)```

### How many students are there?

```
SELECT COUNT(*) AS total_students
FROM student;
```
```(10,)```

### How many enrolled classes are there at the JKB?
```
SELECT COUNT(DISTINCT e.class_id) AS enrolled_classes_count
FROM enrollment e
JOIN class c ON e.class_id = c.class_id
JOIN class_building cb ON c.class_id = cb.class_id
JOIN building b ON cb.building_id = b.building_id
WHERE b.building_abbreviation = 'JKB';
```
```(2,)```

### Which building houses the most amount of classes?

```
SELECT b.building_description, COUNT(cb.class_id) AS class_count
FROM building b
JOIN class_building cb ON b.building_id = cb.building_id
GROUP BY b.building_id
ORDER BY class_count DESC
LIMIT 1;
```
This returned the description of the TMCB rather than the code of the building.
```('How is everyone sick already?', 3)```

### Which building houses the least amount of classes?
```
SELECT b.building_description
FROM building b
JOIN class_building cb ON b.building_id = cb.building_id
GROUP BY b.building_id, b.building_description
ORDER BY COUNT(cb.class_id) ASC
LIMIT 1;
```
This returned the description of the JKB rather than the code of the building.
```('I am lost',)```

### Which building has the highest amount of students attending class?

```
SELECT b.building_description, COUNT(e.student_id) AS student_count
FROM building b
JOIN class_building cb ON b.building_id = cb.building_id
JOIN class c ON cb.class_id = c.class_id
JOIN enrollment e ON c.class_id = e.class_id
GROUP BY b.building_id, b.building_description
ORDER BY student_count DESC
LIMIT 1;
```

```('How is everyone sick already?', 6)```