class BookDatas():
    #장르와 이미지들
    genres = ["에세이", "시", "소설", "만화","자기계발서"]
    images = ["cover1.jpeg","cover2.jpeg","cover3.jpeg","cover4.jpeg","cover5.jpeg"]
    def getImageByGenre(genre):
        return BookDatas.images[BookDatas.genres.index(genre)]
