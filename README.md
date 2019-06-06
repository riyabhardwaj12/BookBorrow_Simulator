Simulator for our BookBorrow table

Initially "Borrowed" table was there which was created using borrow.java, BorrowedDo.java and Sample3.java but this had issues like no rating column was there which was needed for the ml part and also book_id was of string type while in our books table we made it as number,so this was causing problems in using these two tables simultaneously .

All these problems were considered and new final table "BookBorrow" was made using correction.py and the table generated above.
