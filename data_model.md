```mermaid
erDiagram
    users ||--o{ auth_relations : ""
    users {
        varchar email PK
        varchar first_name
        varchar last_name
        timestamp created_at
        timestamp updated_at
        varchar created_by
        varchar last_updated_by
    }
    auth_relations {
        varchar auth_id PK
        varchar email FK
        varchar provider
    }
