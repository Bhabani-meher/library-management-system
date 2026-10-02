class Book:
    def __init__(self,book_id,title,author,category,copies ):
        self.book_id = book_id
        self.title= title
        self.author=author
        self.category=category
        self.copies=copies


class Member:
    def __init__(self,member_id,name, phone):
        self.member_id=member_id
        self.name=name
        self.phone=phone


class Loan:
    def __init__(self,loan_id,book_id,member_id,borrow_date,return_date=None):
        self.loan_id = loan_id
        self.book_id = book_id
        self.member_id = member_id
        self.borrow_date  = borrow_date
        self.return_date = return_date
    