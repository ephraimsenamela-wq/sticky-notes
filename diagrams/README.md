# Sticky Notes — Software Design

Bootcamp design artefacts (Step 1 of the project). PNG renders are in this
folder; PlantUML sources below can be pasted at https://www.plantuml.com/plantuml
if you need vector/UML-standard versions.

## 1. Use case diagram (`use_case_diagram.png`)

```plantuml
@startuml
left to right direction
actor User
rectangle "Sticky Notes System" {
  usecase "Create Note" as UC1
  usecase "View All Notes" as UC2
  usecase "View Note Detail" as UC3
  usecase "Edit Note" as UC4
  usecase "Delete Note" as UC5
}
User --> UC1
User --> UC2
User --> UC3
User --> UC4
User --> UC5
@enduml
```

**Reading:** a single actor (User, no login required in this version) can do
full CRUD on the board. View All is the landing board page; Detail/Edit/Delete
all operate on a `Note pk`.

## 2. Sequence diagram (`sequence_diagram.png`) — Create Note

```plantuml
@startuml
actor User
participant "Browser (Template)" as B
participant "NoteCreateView" as V
participant "NoteForm" as F
participant "Note Model" as M
database "SQLite DB" as DB

User -> B : GET /note/new/
B -> V : GET
V -> B : render empty NoteForm
User -> B : fill title/content/colour, submit
B -> V : POST data
V -> F : is_valid()
F -> M : save()
M -> DB : INSERT
DB --> M : OK
M --> V : instance + pk
V -> B : 302 redirect to /
B -> User : board with new note
@enduml
```

Edit follows the same flow with `NoteUpdateView` + `UPDATE`; Delete uses
`NoteDeleteView` (GET = confirm page, POST = `DELETE` + redirect);
List/Detail are GET-only (`SELECT` → render).

## 3. Class diagram (`class_diagram.png`)

```plantuml
@startuml
class Note {
  + title: CharField(200)
  + content: TextField
  + color: CharField(choices)
  + created_at: DateTime
  + updated_at: DateTime
  + __str__(): str
}
class NoteForm {
  + Meta.model = Note
  + fields: title, content, color
  + is_valid()
  + save()
}
class NoteListView
class NoteDetailView
class NoteCreateView
class NoteUpdateView
class NoteDeleteView

NoteForm --> Note : validates / saves
NoteCreateView --> NoteForm : uses
NoteUpdateView --> NoteForm : uses
NoteListView --> Note : queries
NoteDetailView --> Note : queries
NoteDeleteView --> Note : deletes
@enduml
```

**Design principles applied:** single-responsibility (Model = data, Form =
validation, CBVs = HTTP, Templates = presentation), DRY (one `base.html`,
one `NoteForm`, generic CBVs instead of repeated function views),
MVC/MVT separation, and explicit URL naming (`notes:note-list`, etc.).
