class BookDatas():
    #장르와 이미지들
    genres = ["Essay", "Poem", "Novel", "Play","self_help_book"]
    images = ["cover1.jpeg","cover2.jpeg","cover3.jpeg","cover4.jpeg","cover5.jpeg"]
    def getImageByGenre(genre):
        return BookDatas.images[BookDatas.genres.index(genre)]
