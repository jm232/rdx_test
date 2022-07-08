# Notes on Movie list application
## Bugs and improvements
### General
1. Dashboard page or empty List Movies of simple application is blank
2. UX design is poor, e.g. List Movies without any title, Create Movie with title(huge font)
3. Selected page is not highlighted on links in header
### Create Movie page
1. Rating clarification needed (max/min) + hint to range of numbers
2. 'Name' input field without any validation of maximum characters
3. 'Time' input field without any validation of what characters are allowed (only numbers should be allowed) + no specification of time values (hours/minutes/seconds)
4. 'Cancel' button redirects to 'List Movies' page, why?
5. No clarification which field is required to fill in
6. Clicking on 'Add Movie' on empty page is without any response
7. Adding a movie shows browser event window, with title "localhost:3000 says", there should be better message
### List  Movies page
1. Typo "Upadate"
2. List Movies page without any title
3. No filtering for 'Time' column
4. Filtering doesn't work properly, it matches string only if the first character of value is being filtered, e.g movie "abc", will not filtered with "bc"
5. On empty page API throws 404 error: {"Movie not found", success: false}, but it is valid use case, it should be 200
6. Delete functionality is broken, it doesn't delete item, repeatedly, but not always, hard to determine the behaviour, occasionally it deletes the other item
7. Typo "Do tou want to delete ..." in event window for deleting item

## Functionality to improve/change
### Delete
Delete functionality in 'List Movies' page could be improved in a way, that items present on the page would be selectable. It means to add checkboxes before each row. 'Delete' button would be independent on table, set e.g. at the bottom of table, disabled when none of items selected. That way could user delete multiple items at once.

