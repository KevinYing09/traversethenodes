# traversethenodes
# Project Mini-Project: Folder and File Tree Recursive Traversal

## Scenario Description
This project implements a **Folder and File Tree** data structure to model a project workspace. The primary goal is to use recursion to traverse the directory hierarchy, calculate the total cumulative file size, and count the total number of files within any given folder.

---

## Node Structure
The file system is built using an object-oriented node hierarchy:
* **`Node` (Abstract/Base):** Shares common properties like `name`.
* **`FileNode` (Terminal Node):** Represents an individual file. Stores a `name` and a `size` (in bytes). It has no children.
* **`FolderNode` (Container Node):** Represents a directory. Stores a `name` and a list of `children` (which can be `FileNode` or other `FolderNode` objects).

---

## Recursive Method & Design
* **Method Signature:** `calculate_total_size(node)`
* **Base Case:** When the method encounters a `FileNode`, it stops descending and returns the file's `size` directly.
* **Recursive Step:** When the method encounters a `FolderNode`, it loops through its list of children, recursively calls `calculate_total_size(child)` for each one, and sums up the returned values.
* **Result Combination:** The accumulated sizes bubble back up through the call stack to return the total size of the root directory.

---

## Sample Directory Structure (3 Levels, 7+ Nodes)
Our test sample mimics the following workspace tree:
```text
project_root/ (Folder) [Level 0]
├── README.md (File - 2 KB) [Level 1]
├── src/ (Folder) [Level 1]
│   ├── main.py (File - 5 KB) [Level 2]
│   └── utils.py (File - 3 KB) [Level 2]
└── tests/ (Folder) [Level 1]
    └── test_main.py (File - 4 KB) [Level 2]
