
# Project scope

Goal: be able to login as a basic user or an admin user. setup permissions

How is the database:

- There are groups, permissions, and users

- User Table
  - id
  - username
  - password
  - is_super_user
Example:
id | username | password | is_super_user
1  | admin    | admin    | True
2  | user     | user     | False

- Permissions Table
  - id
  - name
  - codename ( can_view, can_edit, can_delete)
  - content_type_id (FK)  # not unique
Example:
id | name | codename |  
1  | Can View | can_view |
2  | Can Edit | can_edit |

- Group Table
  - id
  - name
Example:
id | name
1  | Admin
2  | User
3  | Super User
4  | Basic User
5  | Guest

<!-- Connect Group and Permissions -->
GroupPermission Table

- id
- group_id (FK) # not unique what group
- permission_id (FK) # not unique what permissions the group has
Example:
id | group_id | permission_id
1  | 1        | 1
2  | 1        | 2
3  | 2        | 1

<!-- Connect the User and Group -->
- UserGroup Table
  - id
  - user_id (FK) # not unique what is the user
  - group_id (FK) # not unique what group the user belongs to

Example Queries in SQLAlchemy ORM:

    ```python
    user Select(User).filter(User.username == 'john').first()

    # groups 
    user_group = Select(UserGroup).filter(UserGroup.user_id == user.id).first()

    # get the users permissions of the groups
    user_permissions = Select( GroupPermission ).filter( user_group.group_id == user.group_id ).all()
    ```

## Summary of how permissions are set up

- User belongs to a group
- Group has permissions
- User has permissions based on the group they belong to
- User can have multiple groups
- Each group has multiple permissions
  
### diagram of the database

```
User Table
+----+----------+----------+----------------+
| id | username | password | is_super_user  |
+----+----------+----------+----------------+
| 1  | admin    | admin    | True           |
| 2  | user     | user     | False          |
+----+----------+----------+----------------+

Permissions Table
+----+----------+----------+
| id | name     | codename | 
+----+----------+----------+
| 1  | Can View | can_view_resource |             
| 2  | Can Edit | can_edit_resource |             
| 2  | create Edit | create_resource |             
+----+----------+----------+


Group Table
+----+----------+
| id | name     | 
+----+----------+
| 1  | Admin    |
| 2  | User     |
| 3  | Super User |
| 4  | Basic User |
| 5  | Guest    |
+----+----------+
---------------------------------------------- Join Tables ----------------------------------------------
GroupPermission Table
+----+----------+----------------+
| id | group_id | permission_id  | (group_id, permission_id) is unique and FK to Group and Permission
+----+----------+----------------+
| 1  | 1        | 1              |
| 2  | 1        | 2              |
| 3  | 2        | 1              |
+----+----------+----------------+

UserGroup Table
+----+----------+----------------+
| id | user_id  | group_id       | (user_id, group_id) is unique and FK to User and Group
+----+----------+----------------+
| 1  | 1        | 1              |
| 2  | 2        | 2              |
+----+----------+----------------+
```

## Endpoints to create

- /User/create
  - Create a user
  - Create a user and assign them to a group

- Notes/create
  - Users can create notes

- Notes/delete:
  - Admins can delete notes
  -

- /create-group
  - Create a group
  
- /create-permission
  - Create a permission

- /User/get-group-and-permissions
  - Get the groups and permissions of the user

    - Houw to queey
    - first you get user
    - then u find the fgroup in the grup table
    - then u find the eprmstion in the permition table

- I was thinking a super user would be able to do the create permition and creat group no one else and everytin else
-Laso admins can create users only
- Users can vire thinsg
  
- Create tests for suiers groups ?

- Notes view/edit/delete list

- Groups have permissions to access resources but users are part of groups
-

- Every user must be part of a groups  

---

- you want do permissions
  - be able to login as two different users and have things available to me
  - do permissions with groups
- using fastapi
  - and sqlalchemy
- migrations are important to you
  - spend time learning how to do this
- don't spend time on login - only permissions for users
- jwt is maybe in scope
- how to have persistent user login maybe?
- learn sql alchemy
- logging
DO not spend time on:
- login
- clean code
- organization of code  
- no dev container
- no log feels no precommit hooks
-  

---

- make it somewhat useful for something

# DIRECT_URL = f"postgresql://{user_name}:{password}@{host}:{port}/{database_name}"
