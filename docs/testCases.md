# Test Case
## Kevin Ying
### Take the following tree for example:
* documents = [taxes, homework, books]
  * taxes = [1040.pdf, w2.pdf, w4.pdf]
  * homework = [math.pdf, english.pdf, science.pdf, history.pdf]
  * books = [harryPotter.pdf, animalFarm.pdf, warAndPeace.pdf]

1. Calling size(documents) will call a recursive algorithm that will go down the tree
2. It will call size(taxes), size(homework), and size(books)
3. From there it will call size(1040.pdf), size(w2.pdf), etc.
4. Since those are base cases they will directly return their file size
5. The iteration of the second layer will sum those and return the total file size found in the subfolders
6. Finally the size(documents) iteration will sum those returns to get the final file size
