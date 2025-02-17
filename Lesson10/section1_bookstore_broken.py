# This program is as imple bookstore demo
books = [
  ["Luis Paints the World","$53.00","3 stars"],
  ["The Bear and the Piano","$36.89", "1 stars"],
  ["The Day the Crayons Came Home (Crayons)","$26.33", "5 stars"],
  ["The Whale","$35.96","4 stars"],
  ["The Wild Robot","$56.07", "3 stars"]
]


#It prints out the star rating for a given book
def get_star_count(book):

  star_count_text = book[1]
  star_count = 0

  if star_count_text == '1 stars':
    star_count = 1
  if star_count_text == '2 stars':
    star_count = 2
  if star_count_text == '3 stars':
    star_count = 3
  if star_count_text == '4 stars':
    star_count = 4
  if star_count_text == '5 stars':
    star_count = 5

  return star_count


#displays the books from the books list
def inventory_display(books):
  print("***Our Book Collection***\n-------------------------\n\n")
  for book in books:
    print(f"Title:{book[0]} \nPrice:{book[1]} \nRating:{get_star_count(book)}")
    print("---------------------------------------------\n")



inventory_display(books)
