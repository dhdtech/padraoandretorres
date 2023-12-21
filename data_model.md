# Descrição Simplificada do Modelo de Dados

Esta descrição tem como objetivo explicar o modelo de dados da Academia de uma forma que seja fácil de entender, mesmo para aqueles sem conhecimento técnico. O modelo é projetado para gerenciar aulas, professores, alunos e agendamentos de forma eficiente.

## Visão Geral

O sistema é composto por várias 'tabelas' que armazenam diferentes tipos de informações. Cada tabela tem uma função específica, como armazenar dados sobre os usuários (alunos e professores), aulas, agendamentos e preferências. Essas tabelas estão interconectadas para formar o sistema completo da Academia.

## Tabela `users`

- **Propósito:** Armazena informações básicas sobre todos os usuários, sejam eles alunos ou professores.
- **Campos Principais:**
  - `email`: O endereço de e-mail do usuário, usado como identificação única.
  - `first_name`: O primeiro nome do usuário.
  - `last_name`: O sobrenome do usuário.
  - `created_at`: A data e hora em que o usuário foi adicionado ao sistema.
  - `updated_at`: A última data e hora em que as informações do usuário foram atualizadas.
  - `created_by`: Quem criou o registro do usuário.
  - `last_updated_by`: Quem atualizou o registro do usuário pela última vez.

### Casos de Uso para `users`

1. **Cadastro de Aluno/Professor:** Quando um novo aluno ou professor é adicionado à academia, suas informações são registradas nesta tabela.
2. **Atualização de Dados:** Se um usuário precisa atualizar seu nome ou outro detalhe, isso é refletido nesta tabela.
3. **Identificação do Usuário:** O sistema usa o e-mail para identificar e diferenciar cada usuário, seja para fazer login ou para atribuir aulas e agendamentos.


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
