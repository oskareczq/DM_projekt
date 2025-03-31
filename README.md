## Dataset Description

### Student Demographics
- **`school`**: Student's school (binary: 'GP' - Gabriel Pereira or 'MS' - Mousinho da Silveira)
- **`sex`**: Student's sex (binary: 'F' - female or 'M' - male)
- **`age`**: Student's age (numeric: from 15 to 22)
- **`address`**: Student's home address type (binary: 'U' - urban or 'R' - rural)
- **`famsize`**: Family size (binary: 'LE3' - less or equal to 3 or 'GT3' - greater than 3)
- **`Pstatus`**: Parent's cohabitation status (binary: 'T' - living together or 'A' - apart)

### Parental Information
- **`Medu`**: Mother's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education, or 4 – higher education)
- **`Fedu`**: Father's education (numeric: 0 - none, 1 - primary education (4th grade), 2 – 5th to 9th grade, 3 – secondary education, or 4 – higher education)
- **`Mjob`**: Mother's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g., administrative or police), 'at_home', or 'other')
- **`Fjob`**: Father's job (nominal: 'teacher', 'health' care related, civil 'services' (e.g., administrative or police), 'at_home', or 'other')

### School and Study Information
- **`reason`**: Reason to choose this school (nominal: close to 'home', school 'reputation', 'course' preference, or 'other')
- **`guardian`**: Student's guardian (nominal: 'mother', 'father', or 'other')
- **`traveltime`**: Home-to-school travel time (numeric: 1 - <15 min., 2 - 15 to 30 min., 3 - 30 min. to 1 hour, or 4 - >1 hour)
- **`studytime`**: Weekly study time (numeric: 1 - <2 hours, 2 - 2 to 5 hours, 3 - 5 to 10 hours, or 4 - >10 hours)
- **`failures`**: Number of past class failures (numeric: n if 1<=n<3, else 4)

### Support and Activities
- **`schoolsup`**: Extra educational support (binary: yes or no)
- **`famsup`**: Family educational support (binary: yes or no)
- **`paid`**: Extra paid classes within the course subject (Math or Portuguese) (binary: yes or no)
- **`activities`**: Extra-curricular activities (binary: yes or no)
- **`nursery`**: Attended nursery school (binary: yes or no)
- **`higher`**: Wants to take higher education (binary: yes or no)
- **`internet`**: Internet access at home (binary: yes or no)
- **`romantic`**: In a romantic relationship (binary: yes or no)

### Behavioral and Health Metrics
- **`famrel`**: Quality of family relationships (numeric: from 1 - very bad to 5 - excellent)
- **`freetime`**: Free time after school (numeric: from 1 - very low to 5 - very high)
- **`goout`**: Going out with friends (numeric: from 1 - very low to 5 - very high)
- **`Dalc`**: Workday alcohol consumption (numeric: from 1 - very low to 5 - very high)
- **`Walc`**: Weekend alcohol consumption (numeric: from 1 - very low to 5 - very high)
- **`health`**: Current health status (numeric: from 1 - very bad to 5 - very good)
- **`absences`**: Number of school absences (numeric: from 0 to 93)

### Academic Performance
- **`G1`**: First period grade (numeric: from 0 to 20)
- **`G2`**: Second period grade (numeric: from 0 to 20)
- **`G3`**: Final grade (numeric: from 0 to 20, output target)

### Additional Variables After Data Preprocessing
- **`G1_por`**, **`G2_por`**, **`G3_por`**: Grades for Portuguese subject
- **`G1_mat`**, **`G2_mat`**, **`G3_mat`**: Grades for Math subject
- **`przedmiot`**: Indicates which subjects the student has data for (values: 'matematyka', 'portugalski', or 'oba')
- **`G3_avg`**: Average final grade (`G3`) - if the student has both subjects, it's the average of `G3_por` and `G3_mat`; if the student has only one subject, it's the value of that subject's `G3`