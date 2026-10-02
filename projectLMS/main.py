from database import connection, cursor
from  models import Book,Member,Loan

#addbooks funcation
def add_book():
    title=input("Enter Title:")
    author=input("Enter Author:")
    category=input("Enter Category:")

    while True:
     try:
      copies=int(input("Enter copies:"))
      if copies < 0:
            print("Copies cannot be negative")
            continue

        
      break
     except ValueError:
       print("enter valid number")
    

    
    cursor.execute("""
    INSERT INTO books(title,author,category,copies)
    VALUES(?,?,?,?)
    """,(title,author,category,copies)
                   )

    connection.commit()
    print("books add succesfully")

def view_books():
   cursor.execute("""
   SELECT books.id,
   books.title,
   books.author,
   books.category,
   books.copies
   FROM books
   """)
   results= cursor.fetchall()

   if not results:
      print("not any books")
      return
   for result in results:
    book=Book(
      result[0],
      result[1],
      result[2],
      result[3],
      result[4]
   )

    print("\n=======")
    print("Book ID:",book.book_id)
    print("Title:",book.title)
    print("Author:",book.author)
    print("Category:",book.category)
    print("Copies:",book.copies)
    

def search_book():
    try:
     book_id = int(input("Enter Book ID: "))
    except ValueError:
       print("Enter valid number!")
       return

    cursor.execute("""
        SELECT
            id,
            title,
            author,
            category,
            copies
        FROM books
        WHERE id = ?
    """, (book_id,))

    result = cursor.fetchone()

    if result is None:
        print("Book not found")
        return
    
    book=Book(
      result[0],
      result[1],
      result[2],
      result[3],
      result[4]
   )

    print("=======")
    print("Book ID:",book.book_id)
    print("Title:",book.title)
    print("Author:",book.author)
    print("Category:",book.category)
    print("Copies:",book.copies)
   


def update_book():
   try:
    book_id=input("Enter book_id:")
   except ValueError:
      print("Enter valid number!")
      return

   cursor.execute(
      """
    SELECT id
    FROM books
    WHERE id =?
    """,(book_id,)
   )

   results=cursor.fetchone()
   if results is None:
      print("Not exist")
      return

   new_title=input("Enter Title:")
   new_author=input("Enter author:")
   new_category=input("Enter category:")
   while True:
    try:
       new_copies=int(input("Enter copies:"))
       
       if new_copies < 0:
               print("Copies cannot be negative")
               continue
       break
    except ValueError:
     print("Enter valid number")


   cursor.execute(
       """
     UPDATE books
    SET title=?,
        author=?,
        category=?,
        copies=?
    WHERE id = ?
    """,(new_title,
         new_author,
         new_category,
         new_copies,
         book_id)
    )

   connection.commit()

   print("Successfully update")

def delete_book():
   try:
    book_id=input("Enter book_id:")
   except ValueError:
      print("Enter valid number!")
      return
   cursor.execute(
      """
   SELECT id 
   FROM books
   WHERE id =?
   """,(book_id,)
   )

   results=cursor.fetchone()

   if results is None:
      print("Not exist")
      return

   cursor.execute("""
   DELETE FROM books
   WHERE id=?
   """,(book_id,))

   connection.commit()
   print("Succesfully delect")

def add_member():
   name=input("Enter your good name:")
   

   while True:
    phone=input("Enter your mobile number:")

    if len(phone) != 10 or not phone.isdigit():
     print("Enter a valid 10-digit mobile number")
     continue
    break

   cursor.execute(
      """
   INSERT INTO members(name,phone)
   VALUES(?,?)
   """,(name,phone)
   )

   connection.commit()
   print("Succesfully add member")

def view_member():
   cursor.execute(
      """
   SELECT members.id,
          members.name,
          members.phone
   FROM members
   """
   )

   results=cursor.fetchall()

   if not  results:
      print("Not exist")
      return

   for result in results:
      member=Member(
         result[0],
         result[1],
         result[2]
      )

      print("id:",member.member_id)
      print("name:",member.name)
      print("phone:",member.phone)

def search_member():
   try:
    member_id=input("Enter book_id:")
   except ValueError:
      print("Enter valid number!")
      return
   cursor.execute(
         """
   SELECT members.id,
             members.name,
             members.phone
   FROM members
   WHERE id=?
      """,(member_id,)
   )

   results= cursor.fetchone()
   
   if not  results:
         print("Not exist")
         return
   
   member=Member(
      results[0],
      results[1],
      results[2]
   )
   
   print("======")
   print("id:",member.member_id)
   print("name:",member.name)
   print("phone:",member.phone)

def update_member():
   try:
      member_id=input("Enter book_id:")
   except ValueError:
         print("Enter valid number!")
         return
   cursor.execute(
      """
   SELECT id
   FROM members
   WHERE id = ?
   """,(member_id,)
   )

   results=cursor.fetchone()

   if  results is None:
      print("Not exists")
      return

   new_name=input("Enter your name :")

   while True:
      phone=input("Enter your Mobile number:")

      if len(phone) != 10 or not phone.isdigit():
         print("again valid 10 digit mobile number")
         continue
      break

   cursor.execute(
      """
   UPDATE members
   SET name=?,
       phone=?
   WHERE ID =?
   """,(new_name,
        phone,
        member_id)
   )

   connection.commit()

   print("Update member successfully")

def delete_member():
   try:
    member_id=input("Enter book_id:")
   except ValueError:
      print("Enter valid number!")
      return
   cursor.execute(
         """
      SELECT id 
      FROM members
      WHERE id =?
      """,(member_id,)
      )
   
   results=cursor.fetchone()
   
   if results is None:
         print("Not exist")
         return
   
   cursor.execute("""
      DELETE FROM members
      WHERE id=?
      """,(member_id,))
   
   connection.commit()
   print("Succesfully delect")

def borrow_book():
   try:
    book_id=int(input("Enter your book id:"))
   except ValueError:
      print("Enter valid number!")
      return
   cursor.execute("""
   SELECT id,copies
   FROM books
   WHERE id =?
   """,(book_id,))

   result_book=cursor.fetchone()

   if result_book is None:
    print("Book not found")
    return

   member_id=int(input("ENter your member id:"))

   cursor.execute(
     """
   SELECT id
   FROM members
   WHERE id =?
    """,(member_id,)
   )
   result_member=cursor.fetchone()

   if result_member is None:
      print("not exist")
      return

   if result_book[1] == 0:
       print("Book is not available")
       return

   

   cursor.execute(
      """
   INSERT INTO loans(book_id,member_id)
   VALUES(?,?)
   """,(book_id,member_id)
   )

   cursor.execute(
      """
   UPDATE books
   SET copies = copies - 1
   WHERE id = ? 
   """,(book_id,)
   )

   connection.commit()
   print("Succesfully Run ")

def return_book():
   try:
    loan_id=int(input("Enter your lone id:"))
   except ValueError:
      print("Enter valid number!")
      return
   cursor.execute(
      """
   SELECT book_id,return_date
   FROM loans
   WHERE id =?
   """,(loan_id,)
   )

   result=cursor.fetchone()
   if result is None:
    print("Loan not found")
    return

   if result[1] is not None:
    print("already return")
    return

   book_id=result[0]
   cursor.execute(
      """
   UPDATE loans
   SET return_date = CURRENT_DATE
   WHERE id = ?
   """,(loan_id,)
   )
   cursor.execute(
         """
      UPDATE books
      SET copies = copies + 1
      WHERE id = ? 
      """,(book_id,)
      )

   connection.commit()
   print("successfuly retun book")

def report_libary():
   print("==LIBRARY REPORT==")

   cursor.execute(
      """
   SELECT COUNT(*) FROM books
   """
   )

   result=cursor.fetchone()

   print("Total books:",result[0])

   cursor.execute(
         """
      SELECT
      COUNT(*) FROM members
      """
      )

   result=cursor.fetchone()

   print("Total members:",result[0])

   cursor.execute(
      """
   SELECT 
   COUNT(*) FROM loans
   """
   )

   result=cursor.fetchone()

   print("Total loan:",result[0])

   cursor.execute(
      """
   SELECT
   COUNT(*) FROM loans
   WHERE return_date IS NULL
   """
   )

   result=cursor.fetchone()

   print("Active loans:",result[0])
   cursor.execute(
            """
         SELECT
         COUNT(*) FROM loans
         WHERE return_date IS NOT NULL
         """
         )

   result=cursor.fetchone()

   print("Return loans",result[0])

   cursor.execute(
            """
         SELECT
         SUM(copies) FROM books
         """
         )

   
   result=cursor.fetchone()

   print("Copies:",result[0])

   cursor.execute(
      """
   SELECT b.title , COUNT(*)
   FROM books as b
   JOIN loans as l
   ON b.id = l.book_id
   GROUP BY b.id
   """
   )

   results=cursor.fetchall()

   for result in results:
      print(result)
# manu
def display_manu():
    print("\n=== LIBRARY MANAGEMENT SYSTEM ===")

    print("BOOK")
    print("1.Add Book")
    print("2.View Books")
    print("3.Search Book")
    print("4.Update Book")
    print("5.Delete Book")

    print("\nMEMBER")
    print("6.Add Member")
    print("7.View Member")
    print("8.Seach Member")
    print("9.Update Member")
    print("10.Delect Member")
    print("11.Borrow Book")
    print("12.Return Book")
    print("13.Reports")
    print("14.Exit")



while True:
    display_manu()

    try:
     choise=int(input("Enter your choise:"))
    except ValueError:
       print("Enter above valid number!")
       continue

    if choise == 1:
       add_book()

    elif choise == 2:
       view_books()
    elif choise == 3:
       search_book()
    elif choise == 4:
       update_book()
    elif choise == 5:
       delete_book()
    elif choise == 6:
         add_member()
    elif choise == 7:
       view_member()
    elif choise == 8:
       search_member()
    elif choise==9:
       update_member()
    elif choise == 10:
       delete_member()
    elif choise == 11:
      borrow_book()
    elif choise == 12:
      return_book()
    elif choise == 13:
       report_libary()
    elif choise==14:
        print("Thank for visit")
        break
    else:

     print("Feature coming soon...")
