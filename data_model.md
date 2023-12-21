```mermaid
erDiagram
    users ||--o{ teachers : ""
    users ||--o{ student_enrollments : ""
    users ||--o{ student_schedule_preferences : ""
    users ||--o{ student_class_agendas : ""
    classes ||--o{ class_schedule : ""
    teachers ||--o{ teacher_default_schedule : ""
    teacher_default_schedule ||--o{ class_schedule : ""
    class_schedule ||--o{ student_enrollments : ""
    weeks ||--o{ class_schedule : ""
    weeks ||--o{ student_class_agendas : ""

    users {
        varchar email PK
        varchar first_name
        varchar last_name
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }

    classes {
        integer class_id PK
        varchar class_name
        time start_time
        interval duration
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }

    teachers {
        integer teacher_id PK
        varchar user_email FK
        varchar teacher_name
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }

    teacher_default_schedule {
        integer default_schedule_id PK
        integer teacher_id FK
        integer class_id FK
        integer default_day
        time default_time
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }

    weeks {
        integer week_id PK
        integer year
        integer week_number
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }

    class_schedule {
        integer schedule_id PK
        integer class_id FK
        integer teacher_id FK
        integer week_id FK
        integer day_of_week
        integer active_slots
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }

    student_enrollments {
        integer enrollment_id PK
        varchar user_email FK
        integer schedule_id FK
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }

    student_schedule_preferences {
        integer preference_id PK
        varchar user_email FK
        integer class_id FK
        integer preferred_day
        time preferred_time
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }

    student_class_agendas {
        integer agenda_id PK
        varchar user_email FK
        integer schedule_id FK
        integer week_id FK
        integer day_of_week
        date class_date
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }
```
