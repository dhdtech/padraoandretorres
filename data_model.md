erDiagram
    users ||--o{ student_enrollments : ""
    classes ||--o{ class_schedule : ""
    class_schedule ||--o{ student_enrollments : ""

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

    class_schedule {
        integer schedule_id PK
        integer class_id FK
        integer day_of_week
        integer available_slots
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
