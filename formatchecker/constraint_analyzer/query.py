# Q 0 : # Article.all
Query(Article)

# Q 1 : # where(author: nil)
Query(Article)
.where("author = ?")
