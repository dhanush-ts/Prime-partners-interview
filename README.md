# Prime Partners LLC - Take-Home Assignment

### Python Bug Fixes
* **Security:** Replaced a vulnerable string-formatted SQL query with a parameterized query (`?`) to prevent SQL injection attacks.
* **Logic (Off-by-one):** Removed the `- 1` from the line items `range` iteration to ensure the final item in the invoice list is calculated.
* **Precision/Rounding:** Refactored the financial calculations to use Python's `Decimal` module instead of `float`, preventing floating-point precision loss, and properly rounded to two decimal places instead of rounding to a whole integer.

### React Bug Fixes
* **State Lag:** Removed the redundant `filtered` state variable, instead computing the filtered array directly during render so the UI stays perfectly in sync with the `searchTerm`.
* **List Rendering:** Added a unique `key` prop to the mapped `<li>` elements to satisfy React's reconciliation requirements and prevent rendering bugs.

### Assumptions
* Assumed the React `invoice` objects have a unique `.id` property to use as the list key.

### What I'd do with more time
* Implement proper error handling and database connection pooling/cleanup (`try/finally` or context managers) in the Python SQL function.
* Add debouncing to the React search input to optimize performance if the invoice list scales to thousands of records.
* Add unit tests (e.g., Pytest, Jest) to verify the math logic and component rendering.
