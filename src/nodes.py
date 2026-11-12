file111 = 3
file211 = 4
file221 = 5
file222 = 6

folder11 = [file111]
folder21 = [file211]
folder22 = [file221, file222]

folder1 = [folder11]
folder2 = [folder21, folder22]
folder[folder1, folder2]

def nodes(files):
  count = 0
  try:
    for file in files:
      count += node(file)
    return count
  except:
    return files



print(nodes(folder))
print(nodes(folder1))
print(nodes(folder2))
